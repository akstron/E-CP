import click
from ..Runner.exceptions.UnsupportedLanguage import UnsupportedLanguage
from ..Config.Config import Config
from ..Runner.mapper import runner_map

@click.command()
@click.argument('dest', type=str, default='.')
@click.option('-c', is_flag = True, default = False)
def run(dest, c):
    try:
        config = Config()
        lang = config.get_lang()
        if(lang not in runner_map):
            raise UnsupportedLanguage(lang)

        runner = runner_map[lang]
        runner(dest, c)
    except UnsupportedLanguage as e:
        click.echo(e)
    except Exception as e:
        click.echo(e)