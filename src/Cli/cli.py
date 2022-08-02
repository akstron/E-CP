import click
from .problem import problem
from .runner import run_code
from .config import set_lang

@click.group()
def entry_point():
    pass

entry_point.add_command(problem)
entry_point.add_command(run_code)
entry_point.add_command(set_lang)