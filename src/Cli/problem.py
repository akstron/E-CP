from pathlib import Path
import click
import os
from ..Scrapers.cf_scraper import get_problem as get_cf_problem
from ..Problem.utils import create_code_file, create_test_files

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
    create_test_files(dir, problem.tests)
    
    # Create code file
    create_code_file(dir)