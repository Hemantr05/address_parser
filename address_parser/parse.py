import pandas as pd
from . import utils

dataset = pd.read_csv('address_parser/all_india_pin_code.csv', encoding='iso-8859-1')

def find_pincode(text):
	"""Best match for pincode
	
		Args:
			text (str): 

		Returns:
			return (int): 
	"""
	pincode = None
	text = text.split(" ")
	for idx in range(len(text)-1, 0, -1):
		if len(text[idx]) == 6:
			try:
				code = int(text[idx].strip())
				pincode = code
				break
			except:
				continue
		continue
	return pincode

def find(text, candidates):
	"""Find entities based on similarity
	
		Args:
			text (str):
			candidates (str/list):
			
		Returns:
			value (str):
	"""

	result = utils.token_similarity(text, candidates)
	if result:
		value, score, index = result[0]
		return value.capitalize()
	return None
	
def extract_from_image(image):
	image = load_image(image)
	
	# TODO: 
	# 1. Extract text from image using OCR (perhaps, tesseract)
	# 2. Group them by line or paragraph blocks
	# 	2.1. Check for bounding box consistency
	# 	2.2. If too much white space between y coordinates of words, new paragraph
	# 	Note: Refer to glib's approach for Block extraction

def extract(text_blob):
	"""Extract individual address entities (zipcode, city, etc)
		from a blob of text

		Args:
			text_blob (str):

		Returns:
			entities (dict): 
	"""
	entities = {
				"Building/Apartment": None,
				"HouseNo": None,
				"Area": None,
				"Landmark": None,
				"Town": None,
				"City": None,
				"State": None,
				"Zipcode": None,
				}
	text_blob = utils.clean_text(text_blob)
	pincode = find_pincode(text_blob)
	values = dataset.loc[dataset['pincode']==pincode]
	office_type = [utils.clean_text(name) for name in values["officeType"]]
	office_name = [utils.clean_text(name) for name in values["officename"]]
	city_name = [utils.clean_text(name) for name in values["Districtname"]]
	state_name = [utils.clean_text(name) for name in values["statename"]]
	area = find(text_blob, office_name)
	city = find(text_blob, city_name)
	state = find(text_blob, state_name)
	entities["Zipcode"] = pincode
	entities["Area"] = area
	entities["City"] = city
	entities["State"] = state
	return entities
