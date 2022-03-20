import re
import cv2
import pandas as pd
from rapidfuzz import process, fuzz

def token_similarity(source, target):
	"""Find similarity score between both strings

		Args:
			source (str):
			target (str):

		Returns:
			source/result (float/list):
	"""
	if isinstance(source, str) and isinstance(target, str):
		score = fuzz.token_sort_ratio(source, target)
		return score
	elif isinstance(source, str) and isinstance(target, list):
		result = process.extract(source, target, scorer=fuzz.token_sort_ratio, limit=1)
		return result
	else:
		return None

def clean_text(source):
	"""Remove unicodes, lowercase input text,
	   remove extra whitespaces

		Args:
			source (str):

		Returns:
			text (str):
	"""
	text = source.split('-')
	text = list2str(text)
	text = re.sub(r'[^\w\s]', '', text)
	text = re.sub(r'\s\s+', '', text)
	text = text.strip()
	text = text.lower()
	text = text.split(' ')
	text = list2str(text)
	return text

def list2str(source):
	"""Convert list inputs to string
	
		Args:
			source (str):

		Returns:
			target (str):
	"""
	target = ' '.join(map(str, source))
	return target

def load_image(image_path):
	image = cv2.imread(image_path)
	return image

# def search_entity(source_entity, target_entity, dataset_path):
# 	"""Search entity from custom dataset
	
# 		Args:
# 			source_entity (str): 
# 			target_entity (str): 
# 			dataset_path (str): 

# 		Returns:
# 			result ()
# 	"""
# 	if dataset_path:
# 		filename, extn = dataset_path.split('/')[-1].split('.')
# 		if extn == 'csv':
# 			result =  extract_from_csv(source_entity, target_entity, dataset_path)
# 		elif extn == 'excel':
# 			result = extract_from_excel(source_entity, target_entity, dataset_path)
# 		elif extn == 'json':
# 			result = extract_from_json(source_entity, target_entity, dataset_path)
# 		return result
# 	else:
# 		result =  extract_from_csv(source_entity, target_entity, "../data/all_india_pin_code.csv")
# 		return result

# def extract_from_csv(source_entity, target_entity, dataset_path): pass
# def extract_from_excel(source_entity, target_entity, dataset_path): pass
# def extract_from_json(source_entity, target_entity, dataset_path): pass
