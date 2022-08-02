import json
import os
from pathlib import Path

supported_lang = ['cpp', 'python']

def get_lang():
    config_file_path = Path(os.path.dirname(os.path.realpath(__file__)), 'config.json')
  
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    
    return config['language']

def is_lang_supported(lang):
    return lang in supported_lang