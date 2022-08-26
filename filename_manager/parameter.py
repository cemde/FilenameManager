import re
from typing import Any


class Parameter:
    def __init__(self, name: str, format: str):
        self.name = name
        self.format = format

        if "fp" in format:
            m = re.match(r'fp(\d+).(\d+)', format)
            g1, g2 = int(m.group(1)), int(m.group(2))
            self.pattern = f'\d{{{g1}}}.\d{{{g2}}}'
            self.decode_fn = float
            self.encode_fn = lambda x: f"{x:0{g1+g2+1}.{g2}f}"

        elif "bool" in format:
            self.pattern = 'True|False'
            self.decode_fn = bool
            self.encode_fn = lambda x: str(x)

        elif "int" in format:
            if "int" == format:
                self.pattern = '\d+'
                self.decode_fn = int
                self.encode_fn = lambda x: str(x)
            else:
                n_digits = format[0]
                self.pattern = f'\d{{{n_digits}}}'
                self.decode_fn = int
                self.encode_fn = lambda x: f"{x:0{n_digits}d}"

        elif "str" in format:
            if format == "str":
                self.pattern = '\w+'
                self.decode_fn = str
                self.encode_fn = lambda x: x

            else:
                n_char = int(re.findall(r'\d+', format)[0])
                self.pattern = f'\w{{{n_char}}}'
                self.decode_fn = lambda x: x.replace("0", "")
                pad_at_back = format.startswith("str")

                def encfn(x):
                    pad_str = "0" * (n_char - len(x))
                    if pad_at_back:
                        return x + pad_str
                    else:
                        return pad_str + x

                self.encode_fn = encfn

    def encode(self, val: Any) -> str:
        """Convert parameters to a file name.

        Args:
            val (Any): value to be encoded.

        Returns:
            str: encoded value.
        """
        return self.encode_fn(val)

    def decode(self, val: str) -> Any:
        """Convert string to raw value.

        Args:
            val (str): Input string.

        Returns:
            Any: Decoded raw value.
        """
        return self.decode_fn(val)
