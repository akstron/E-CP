from pathlib import Path

import click
from ..Runner.mapper import ext_map
from ..Runner.error import UnsupportedLanguage
from ..Config.config import get_lang

def create_test_files(dir, tests):
    index = 1
    for test in tests:
        input_test_file = Path(dir, f'input_{index}.txt')
        with open(input_test_file, 'w') as file:
            file.write(test.input)
        
        output_test_file = Path(dir, f'expected_{index}.txt')
        with open(output_test_file, 'w') as file:
            file.write(test.output)

        index += 1

def create_code_file(dir):
    try:
        lang = get_lang()
        if lang not in ext_map:
            raise UnsupportedLanguage('lang')

        code_file = Path(dir, f'code.{ext_map[lang]}')
        
        ''' 
            'w' with overwrite the file, even if we don't write anything 
            https://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w#:~:text=w%2B-,Opens%20a%20file%20for%20both%20writing%20and%20reading.,file%20for%20reading%20and%20writing.
        '''
        with open(code_file, 'a') as file:
            pass

    except UnsupportedLanguage as e:
        click.echo(e)
    except Exception as e:
        click.echo(e)