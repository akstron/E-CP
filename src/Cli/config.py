import click
from ..Config.Config import Config
from ..Runner.exceptions.UnsupportedLanguage import UnsupportedLanguage

@click.command()
@click.argument('lang', type=str)
def set_lang(lang):
    try:
        # if(not is_lang_supported(lang)):
        #     raise UnsupportedLanguage(lang)
            
        # config_file_path = Path(os.path.dirname(os.path.realpath(__file__)), '..', 'Config', 'config.json')
    
        # with open(config_file_path, 'r') as config_file:
        #     config = json.load(config_file)

        # config['language'] = lang

        # with open(config_file_path, 'w') as config_file:
        #     config_file.write(json.dumps(config))

        config = Config()
        config.set_lang(lang)

    except UnsupportedLanguage as e:
        click.echo(e)
    except Exception as e:
        click.echo(e)