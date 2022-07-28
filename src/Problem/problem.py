class Test:
    def __init__(self, input, output) -> None:
        self.input = input
        self.output = output

class Problem:
    def __init__(self, name, tests = []) -> None:
        self.name = name
        self.tests = tests