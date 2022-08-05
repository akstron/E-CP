import os
from pathlib import Path

def get_config_path() -> Path:
    config_file_path = Path(os.path.dirname(os.path.realpath(__file__)), 'config.json')
    return config_file_path