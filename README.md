# Filename-Manager


[![pypi](https://img.shields.io/pypi/v/FilenameManager.svg)](https://pypi.org/project/FilenameManager/)
[![python](https://img.shields.io/pypi/pyversions/FilenameManager.svg)](https://pypi.org/project/FilenameManager/)
[![Build Status](https://github.com/cemde/FilenameManager/actions/workflows/dev.yml/badge.svg)](https://github.com/cemde/FilenameManager/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/cemde/FilenameManager/branch/main/graphs/badge.svg)](https://codecov.io/github/cemde/FilenameManager)



A simple Python library to handle filenames automatically for artifacts.


[//]: <> (* Documentation: <https://cemde.github.io/FilenameManager>)
* GitHub: <https://github.com/cemde/FilenameManager>
* PyPI: <https://pypi.org/project/FilenameManager/>

## Install

```bash
pip install filenamemanager
```

## Features

This library helps to convert a set of parameters into filenames and vice versa.

When running a script depending on parameters `par1` (str) and `par2` (float), you might want to save artifacts with a filename generated by these parameters.

You can decide how to format each parameter in the saved filename, e.g. `fp4.4` will padd the float with leading `0`s and with 4 digits. For example, `1.2` will be `0001.2000`.

### Save artifacts
```python
from filename_manager import FilenameManager

fm = FilenameManager({"par1": "str", "par2": "fp.4.4}"}, prefix="subfolder/prefix", postfix=".csv")

# define your parameters
par1 = "Hello"
par2 = "3.11"

# super fancy script
results = "placeholder"

# create filename
filename=fm.encode(par1=par1, par2=par2)

# save
...

```

the filename will be `subfolder/prefix_par1_Hello_par2_0003.1100.csv`.

### Load artifacts

```python
from filename_manager import FilenameManager

fm = FilenameManager({"par1": "str", "par2": "fp.4.4}"}, prefix="subfolder/prefix", postfix=".csv")

# get your filename
filename = "subfolder/prefix_par1_Hello_par2_0003.1100.csv"

# parse filename
pars = fm.decode(filename)
```

The variable `pars` is a dictionary with `{"par1": "Hello", "par2": 3.11}`.


## Documentation

The documentation is given in the docstrings. Only two classes exist. `Parameter` and `FilenameManager`.

The supported formats are

- `fp*.*` for floating point parameters. E.g. "fp4.3" formats 1.2 as "0001.200"
- `str` for string parameters.
- `str*` for string parameters with * characters padded with 0 in the end.
- `*str` for string parameters with * characters padded with 0 in the beginning.
- `bool` for boolean parameters.
- `*int` for integer parameters with * leading zeros.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.
