'''
    Using subprocess module: https://docs.python.org/3/library/subprocess.html
'''
import os
from pathlib import Path
import subprocess
import click
from .error import CodeError
from .comparator import validate_output
from abc import ABC, abstractmethod

class Runner(ABC):
    def __init__(self, dest, code_file) -> None:
        self.dest = dest
        self.code_file = code_file

    @abstractmethod
    def run_on_test_files(self):
        pass

    @abstractmethod
    def run_on_custom(self):
        pass

class CppRunner(Runner):
    def __init__(self, dest, code_file) -> None:
        super().__init__(dest, code_file)
        self.exec_file = self.__compile_code()

    def __compile_code(self):
        return subprocess.run(['g++', self.code_file, '-o', 'a'], capture_output=True, text=True)

    def __execute_code(self, exec_file, stdin = None):
        return subprocess.run([exec_file], capture_output=True, text=True, stdin=stdin)

    def run_on_test_files(self):
        current_dir = os.listdir(self.dest)

        for file_name in current_dir:
            if len(file_name) >= 5:
                if file_name[:5] == 'input' and file_name[-4:] == '.txt':
                    input_file_name = file_name
                    
                    input_file_path = Path(input_file_name)
                    with open(input_file_path, 'r') as content:   
                        # Run executable file with sample input files
                        exec_result = self.__execute_code('./a', content)

                        if exec_result.returncode != 0:
                            raise CodeError(exec_result.stderr, 'runtime error', exec_result.returncode)

                        output_file_path = Path(f'output{file_name[5:]}')

                        # Write output obtained from to output_file
                        with open(output_file_path, 'w') as output_file:
                            output_file.write(exec_result.stdout.strip()) 

    def run_on_custom(self):
        exec_result = self.__execute_code(Path(self.dest, 'a'))
        click.echo(exec_result.stdout)

class PythonRunner(Runner):
    def __init__(self, dest, code_file) -> None:
        super().__init__(dest, code_file)
    
    def __execute_code(self, stdin = subprocess.PIPE):
        return subprocess.run(['python', 'code.py'], capture_output=True, text=True, stdin=stdin)

    def run_on_test_files(self):
        current_dir = os.listdir(self.dest)

        for file_name in current_dir:
            if len(file_name) >= 5:
                if file_name[:5] == 'input' and file_name[-4:] == '.txt':
                    input_file_name = file_name
                    
                    input_file_path = Path(input_file_name)
                    with open(input_file_path, 'r') as content:   
                        # Run executable file with sample input files
                        exec_result = self.__execute_code(content)

                        if exec_result.returncode != 0:
                            raise CodeError(exec_result.stderr, 'runtime error', exec_result.returncode)

                        output_file_path = Path(f'output{file_name[5:]}')

                        # Write output obtained from to output_file
                        with open(output_file_path, 'w') as output_file:
                            output_file.write(exec_result.stdout.strip()) 
    
    def run_on_custom(self):
        exec_result = self.__execute_code()
        click.echo(exec_result.stdout)

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
        
