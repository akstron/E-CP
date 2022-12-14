'''
   Test related commands
'''

import click
from ..Test.exceptions.TestNotFound import TestNotFound
from ..Test.exceptions.TestInProgress import TestInProgress
from ..Test.Test import Test

@click.group()
def test():
   pass

@click.command()
@click.argument('time', type=int, default=30)
def start(time):
   try:
      test = Test()
      test.start_test(time)
      click.echo(click.style('Test started...', fg='green'))
   except TestInProgress as e:
      print(e)
   except Exception as e:
      print(e)

@click.command()
def end():
   try:
      test = Test()
      test.stop_test()
   except TestInProgress as e:
      print(e)
   except Exception as e:
      print(e)

@click.command()
def time():
   try:
      test = Test()
      test.get_rem_time()
   except TestNotFound as e:
      print(e)
   except Exception as e:
      print(e)

test.add_command(start)
test.add_command(end)
test.add_command(time)