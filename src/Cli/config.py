import json
import os
from pathlib import Path
import click

@click.command()
@click.argument('lang', type=str)
def set_lang(lang):
    config_file_path = Path(os.path.dirname(os.path.realpath(__file__)), '..', 'Config', 'config.json')
  
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)

    config['language'] = lang

    with open(config_file_path, 'w') as config_file:
        config_file.write(json.dumps(config))
