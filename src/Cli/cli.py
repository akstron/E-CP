import click
from .problem import problem
from .runner import run_cpp_code

@click.group()
def entry_point():
    pass

entry_point.add_command(problem)
entry_point.add_command(run_cpp_code)