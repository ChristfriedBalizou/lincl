![Upload Python Package](https://github.com/ChristfriedBalizou/lincl/workflows/Upload%20Python%20Package/badge.svg)

# lincl
Linux commands line as python methods

This project is ccreate to help avoiding calling `subprocess`.
While working on another script project I was doing lot o system calls. Having
to always import subprocess with Popen, checkoutput, checkcall with ugly
arguments to pass as `--show-lines` or `--include=A,B,C`, I decided to
implement something `python` readable.


## Usage

Pythonic approch and very simple to use:

```python
from lincl import cp as copy

copy(src, dest, recursive=True, force=True)
>> cp --recursive --force src dest

# Or

from lincl import deboostrap

deboostrap("stable", "destination", variant="buildd" include=["A", "B", "C"])
>> deboostrap --variant=buildd --include=A,B,C stable destination
```


## Requirements

To use this package you need:
- Python 3.7 or higher (Tested with python3.7. Let me know for lowers)
- Linux based is prefered (Tested on Debian buster)
- You still need sudo for sudo syscall


## Installation

There is no pip package if you are interested in having one feel free to
suggest. Otherwize install using:

```bash
pip install git+https://github.com/ChristfriedBalizou/lincl.git#egg=lincl

# or

git clone https://github.com/ChristfriedBalizou/lincl.git
cd lincl && python setup.py install
```
