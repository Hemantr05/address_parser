from address_parser import __version__
from address_parser.parse import extract

def test_version():
    assert __version__ == '0.1.0'

def find_zipcode():
    text = "This is a zipcode 560094 for RMV II tage, Bangalore"
    pincode = "560094"
    area = "Rmv II stage"
    city = "Bangalore"
    
    extracted_addr = extract(text)
    assert extracted_addr['Zipcode'] == pincode
    assert extracted_addr['Area'] == area
    assert extracted_addr['City'] == city