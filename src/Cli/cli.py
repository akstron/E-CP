import click
from .problem import problem
from .runner import run
from .config import set_lang
from .test import start_test, stop_test, time

@click.group()
def entry_point():
    pass

entry_point.add_command(problem)
entry_point.add_command(run)
entry_point.add_command(set_lang)
entry_point.add_command(start_test)
entry_point.add_command(stop_test)
entry_point.add_command(time)