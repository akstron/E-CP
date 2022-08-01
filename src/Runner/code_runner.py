'''
    Using subprocess module: https://docs.python.org/3/library/subprocess.html
'''
import os
from pathlib import Path
import subprocess
import click
from Runner.error import CodeError

@click.command()
@click.argument('dest', type=str, default='./code.cpp')
def run_cpp_code(dest):
    try:
        # Create executable file
        compile_result = subprocess.run(['g++', dest, '-o', 'a'], capture_output=True, text=True)

        if compile_result.returncode != 0:
            raise CodeError(compile_result.stderr, 'compile error',compile_result.returncode)

        current_dir = os.listdir('.')

        for file_name in current_dir:
            if len(file_name) >= 5:
                if file_name[:5] == 'input' and file_name[-4:] == '.txt':
                    input_file_name = file_name
                    
                    input_file_path = Path(input_file_name)
                    with open(input_file_path, 'r') as content:   
                        # Run executable file with sample input files
                        exec_result = subprocess.run(['./a'], capture_output=True, text=True, stdin=content)

                        if exec_result.returncode != 0:
                            raise CodeError(exec_result.stderr, 'runtime error', exec_result.returncode)

                        output_file_path = Path(f'output{file_name[5:]}')

                        # Write output obtained from to output_file
                        with open(output_file_path, 'w') as output_file:
                            output_file.write(exec_result.stdout.strip()) 
    except (CodeError) as e:
        click.echo(f'Error type: {e.error_type}')
        click.echo(f'Return code: {e.return_code}')
        click.echo(e)

    except Exception:
        print('Something went wrong')