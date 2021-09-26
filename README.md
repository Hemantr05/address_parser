# address_parser
A python package to find, token and format addresses from a blob of text

<!-- [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) -->
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![example workflow](https://github.com/Hemantr05/address_parser/actions/workflows/python-app.yml/badge.svg)
[![PyPi license](https://badgen.net/pypi/license/pip/)](https://pypi.com/project/pip/)


## Getting Started
### Installation
address_parser is written in 100% python and can be quickly installed using pip.
```sh
git clone https://github.com/Hemantr05/address_parser && cd address_parser

pip install poetry

poetry install
```

### Usage
```python
from address_parser.parse import extract

text = "#101, Whispering Meadows, Dollars Colony, RMV 2nd Stage, Bangalore-560094 sd"
result = extract(text)
print(result)
```
