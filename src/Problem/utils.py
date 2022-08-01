from pathlib import Path

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