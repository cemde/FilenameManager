"""This module defines the Parameter class."""
import re
from typing import Any


class Parameter:
    """The Parameter class encodes and decodes individual parameters to and from strings.

    Attributes:
        name (str): The name of the parameter.
        format (str): The format.
        pattern (str): The regular expression pattern.
    """

    def __init__(self, name: str, format: str) -> None:
        """Create a parameter class.

        This parameter can encode and decode values to and from strings. Specify
        the format of each parameter and generate a file name.
            "fp*.*" for floating point parameters. E.g. "fp4.3" formats 1.2 as "0001.200"
            "str" for string parameters.
            "str*" for string parameters with * characters padded with 0 in the end.
            "*str" for string parameters with * characters padded with 0 in the beginning.
            "bool" for boolean parameters.
            "*int" for integer parameters with * leading zeros.

        Args:
            name (str): The name of the parameter.
            format (str): The format.
        """
        self.name = name
        self.format = format

        if "fp" in format:
            m = re.match(r'fp(\d+).(\d+)', format)
            assert m is not None, f"Invalid format: {format}"
            g1, g2 = int(m.group(1)), int(m.group(2))
            self.pattern = fr'-?\d{{{g1}}}.\d{{{g2}}}'
            self._decode_fn = float
            self._encode_fn = lambda x: f"{x:0{g1+g2+1}.{g2}f}"

        elif "bool" in format:
            self.pattern = 'True|False'
            self._decode_fn = lambda x: x == "True"  # type: ignore
            self._encode_fn = lambda x: str(x)

        elif "int" in format:
            if "int" == format:
                self.pattern = r'\d+'
                self._decode_fn = int  # type: ignore
                self._encode_fn = lambda x: str(x)
            else:
                n_digits = format[0]
                self.pattern = fr'\d{{{n_digits}}}'
                self._decode_fn = int  # type: ignore
                self._encode_fn = lambda x: f"{x:0{n_digits}d}"

        elif "str" in format:
            if format == "str":
                self.pattern = r'\w+'
                self._decode_fn = str  # type: ignore
                self._encode_fn = lambda x: x

            else:
                n_char = int(re.findall(r'\d+', format)[0])
                self.pattern = fr'\w{{{n_char}}}'
                self._decode_fn = lambda x: x.replace("0", "")  # type: ignore
                pad_at_back = format.startswith("str")

                def encfn(x):
                    pad_str = "0" * (n_char - len(x))
                    if pad_at_back:
                        return x + pad_str
                    else:
                        return pad_str + x

                self._encode_fn = encfn

    def encode(self, val: Any) -> str:
        """Convert parameters to a file name.

        Args:
            val (Any): value to be encoded.

        Returns:
            str: encoded value.
        """
        return self._encode_fn(val)

    def decode(self, val: str) -> Any:
        """Convert string to raw value.

        Args:
            val (str): Input string.

        Returns:
            Any: Decoded raw value.
        """
        return self._decode_fn(val)
