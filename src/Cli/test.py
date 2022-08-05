import click

from src.Test.exceptions.TestNotFound import TestNotFound

from ..Test.exceptions.TestInProgress import TestInProgress
from ..Test.Test import Test

@click.command()
def start_test():
   try:
      test = Test()
      test.start_test()
   except TestInProgress as e:
      print(e)
   except Exception as e:
      print(e)

@click.command()
def stop_test():
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