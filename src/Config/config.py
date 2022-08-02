import json
import os
from pathlib import Path

def get_lang():
    config_file_path = Path(os.path.dirname(os.path.realpath(__file__)), 'config.json')
  
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    
    return config['language']