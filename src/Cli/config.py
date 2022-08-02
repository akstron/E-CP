import json
import os
from pathlib import Path
import click
from ..Runner.error import UnsupportedLanguage
from ..Config.config import is_lang_supported

@click.command()
@click.argument('lang', type=str)
def set_lang(lang):
    try:
        if(not is_lang_supported(lang)):
            raise UnsupportedLanguage(lang)
            
        config_file_path = Path(os.path.dirname(os.path.realpath(__file__)), '..', 'Config', 'config.json')
    
        with open(config_file_path, 'r') as config_file:
            config = json.load(config_file)

        config['language'] = lang

        with open(config_file_path, 'w') as config_file:
            config_file.write(json.dumps(config))

    except UnsupportedLanguage as e:
        click.echo(e)
    except Exception as e:
        click.echo(e)