import pandas as pd

from utils import *

def find(str: entity, str: text_blob):
    """Find entity such as city, zipcode, state, etc.
       from block of text
    """
    pass

def extract(str: text_blob):
    """Extract individual address entities (zipcode, city, etc)
       from a blob of text
    """
    entities = {
		"State": None,
		"City": None,
		"Zipcode": None,
		"Town": None,
		"Area": None,
		"HouseNo": None,
		"Landmark": None,
		"Building/Apartment": None,
		}
    pass
