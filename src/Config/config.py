import json
import os
from pathlib import Path
from .utils import get_config_path

supported_lang = ['cpp', 'python']

def get_lang():
    config_file_path = get_config_path()
  
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    
    return config['language']

def is_lang_supported(lang):
    return lang in supported_lang