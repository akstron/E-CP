import click
from .problem import problem
from .runner import run
from .config import set_lang

@click.group()
def entry_point():
    pass

entry_point.add_command(problem)
entry_point.add_command(run)
entry_point.add_command(set_lang)