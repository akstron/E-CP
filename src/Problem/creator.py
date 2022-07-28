import click
import os
from Scrapers.cf_scraper import get_problem as get_cf_problem

#TODO: Handle directory name collision
@click.command()
@click.argument('dest', type=str)
@click.argument('url', type=str)
def problem(dest, url):
    problem = get_cf_problem(url)
    dir = f'{dest}\\{problem.name}'
    # os.mkdir(dir)