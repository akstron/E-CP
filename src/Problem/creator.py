from pathlib import Path
import click
import os
from Scrapers.cf_scraper import get_problem as get_cf_problem

#TODO: Add default dest = '.'
@click.command()
@click.argument('url', type=str)
@click.argument('dest', type=str, default='.')
def problem(dest, url):
    problem = get_cf_problem(url)

    # Create directory
    dir = Path(dest, problem.name)

    # If directory is not already created
    if(not dir.exists()):
        os.mkdir(dir)

    # Create test files
    tests = problem.tests
    index = 1
    for test in tests:
        input_test_file = Path(dir, f'input_{index}.txt')
        with open(input_test_file, 'w') as file:
            file.write(test.input)
        
        output_test_file = Path(dir, f'output_{index}.txt')
        with open(output_test_file, 'w') as file:
            file.write(test.output)

        index += 1

    # Create code file -> Default to cpp
    # TODO: Change default

    code_file = Path(dir, f'code.cpp')
    ''' 
        'w' with overwrite the file, even if we don't write anything 
        https://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w#:~:text=w%2B-,Opens%20a%20file%20for%20both%20writing%20and%20reading.,file%20for%20reading%20and%20writing.
    '''
    with open(code_file, 'a') as file:
        pass

    
