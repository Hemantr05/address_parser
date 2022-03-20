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

<br><br>
For owner only:

TODO:

- [ ] Tests for presently extracted datapoints
  - [ ] assert type(zipcode) == int
  - [ ] if entity present by not capture, assert type(entity) == " "
  - [ ] if entity not present, assert type(entity) == None

- [ ] Extract other datapoints
  - [ ] house/flat number
  - [ ] town
  - [ ] landmark
  
- [ ] Auto-fill address based on few datapoints

- [ ] Unstructured address extraction
  - [ ] Collect documents containing Indian addresses
  - [ ] Convert them into images and collect OCR for them
  - [ ] Annotate addresses in the image, with corresponding text
  - [ ] Train a Model to learn address representation (LayoutLMv2 or BERT or a Visual Language Model - ViT)  

- [ ] Detect and reformat address in textblob from OCR outputs


- [ ] Develop API (using FastAPI)
  - [ ] Dockerfile
  - [ ] Type of input 
   - [ ] Text
   - [ ] Images (document or poster)
  - [ ] Output response
  - [ ] Auth Tokens (for each user) 
