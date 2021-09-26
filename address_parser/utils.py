import re
import pandas as pd
from RapidFuzz import fuzz

def similarity(str: source, str: target):
    """Find similarity score between both strings"""
    score = fuzz.token_sort_ratio(source, target)
    return score

def clean_text(str: source):
    """Remove unicodes, lowercase input text,
       remove extra whitespaces"""
    text = re.sub(r'[^\w\s]', '', source)
    text = re.sub(r'\s\s+', '', text)
    text = text.strip()
    text = text.lower()
    return text

def list2string(list: source):
    """Convert list inputs to string"""
    target = ' '.join(map(str, source))
    return target

def search_entity(str: source_entity, str: target_entity, str: dataset_path):
    """Search entity from dataset"""
    if dataset_path:
        filename, extn = dataset_path.split('/')[-1].split('.')
        if extn == 'csv':
            result =  extract_from_csv(source_entity, target_entity, dataset_path)
        elif extn == 'excel':
            result = extract_from_excel(source_entity, target_entity, dataset_path)
        elif extn == 'json':
            result = extract_from_json(source_entity, target_entity, dataset_path)
	return result
    else:
        result =  extract_from_csv(source_entity, target_entity, "../data/all_india_pin_code.csv")
	return result

def extract_from_csv(str: source_entity, str: target_entity, str: dataset_path): pass
def extract_from_excel(str: source_entity, str: target_entity, str: dataset_path): pass
def extract_from_json(str: source_entity, str: target_entity, str: dataset_path): pass
