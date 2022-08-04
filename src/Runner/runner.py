from pathlib import Path
import click
from .exceptions.CodeError import CodeError
from .comparator import validate_output
from .runners.CppRunner import CppRunner
from .runners.PythonRunner import PythonRunner

# dest is the directory path
def run_cpp_code(dest, custom):
    try:
        code_file = Path(dest, 'code.cpp')
        runner = CppRunner(dest, code_file)

        if custom:
            runner.run_on_custom()
        else :
            runner.run_on_test_files()
            validate_output(dest)
        
    except CodeError as e:
        click.echo(e)

    except Exception as e:
        click.echo(e)

def run_python_code(dest, custom):
    try:
        code_file = Path(dest, 'code.py')
        runner = PythonRunner(dest, code_file)

        if custom:
            runner.run_on_custom()
        else :
            runner.run_on_test_files()
            validate_output(dest)

    except CodeError as e:
        click.echo(e)
    except Exception as e:
        click.echo(e)
        
