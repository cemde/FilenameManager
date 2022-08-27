"""Main module."""

import re
from typing import Any, Dict, List, Union

from .parameter import Parameter


class FilenameManager:
    """The FilenameManager generates and reads filenames automatically.

    Attributes:
        parameters (List[Parameter]): List of parameters.
        prefix (str): Prefix of the filename.
        postfix (str): Postfix of the filename.
        pattern (str): Regex pattern of the filename.
    """

    def __init__(self, parameters: Union[List[Parameter], Dict[str, str]], prefix: str = '', postfix: str = ''):
        """This will encode and decode filenames composed of parameters.

        Specify the format of each parameter and generate a file name.
            "fp*.*" for floating point parameters. E.g. "fp4.3" formats 1.2 as "0001.200"
            "str" for string parameters.
            "str*" for string parameters with * characters padded with 0 in the end.
            "*str" for string parameters with * characters padded with 0 in the beginning.
            "bool" for boolean parameters.
            "*int" for integer parameters with * leading zeros.

        Args:
            parameters (Union[List[Parameter], Dict[str, str]]): specifies the parameters with names and formats.
            prefix (str, optional): Prefix, e.g. path to file. Defaults to ''.
            postfix (str, optional): Postfix, e.g. file type. Defaults to ''.
        """
        if isinstance(parameters, dict):
            parameters = [Parameter(n, f) for n, f in parameters.items()]
        self.parameters: List[Parameter] = parameters

        pattern = [f"{p.name}_({p.pattern})" for p in parameters]
        self.prefix, self.postfix = prefix, postfix
        self.pattern = prefix + '_'.join(pattern) + postfix

    def encode(self, **kwargs) -> str:
        """Convert parameters to a file name.

        Args:
            **kwargs: parameters to be encoded.

        Returns:
            str: file name.
        """
        # check if kwargs is missing parameters
        missing_kwargs = [k.name for k in self.parameters if k.name not in kwargs]
        if len(missing_kwargs) > 0:
            raise ValueError(f"Missing parameters: {missing_kwargs}")

        # check if kwargs contains extra parameters not known
        missing_pars = [p for p in kwargs if p not in [k.name for k in self.parameters]]
        if len(missing_pars) > 0:
            raise ValueError(f"Unknown parameters: {missing_pars}")

        s = [f"{p.name}_{p.encode(kwargs[p.name])}" for p in self.parameters]
        return self.prefix + '_'.join(s) + self.postfix

    def decode(self, string: str) -> Dict[str, Any]:
        """Convert file name to parameters.

        Args:
            string (str): File name string.

        Returns:
            Dict[str, Any]: Parameters.
        """
        m = re.match(self.pattern, string)
        if m is None:
            raise ValueError(f"Filename {string} does not match pattern {self.pattern}")
        args = {}
        for i, p in enumerate(self.parameters):
            args[p.name] = p.decode(m.group(i + 1))
        return args
