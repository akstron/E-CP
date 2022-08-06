from abc import ABC, abstractmethod

'''
    Scraper abstract class
'''

class Scraper:
    def __init__(self, url) -> None:
        self.url = url

    @abstractmethod
    def get_problem_name(self):
        pass

    @abstractmethod
    def get_problem_tests(self):
        pass
