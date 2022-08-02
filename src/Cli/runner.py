import click
from ..Runner.error import UnsupportedLanguage
from ..Config.config import get_lang
from ..Runner.mapper import runner_map

@click.command()
@click.argument('dest', type=str, default='.')
def run_code(dest):
    try:
        lang = get_lang()
        if(lang not in runner_map):
            raise UnsupportedLanguage(lang)

        runner = runner_map[lang]
        runner(dest)
    except UnsupportedLanguage as e:
        click.echo(e)
    except Exception as e:
        click.echo(e)