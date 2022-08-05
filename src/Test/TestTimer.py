from threading import Timer
from datetime import datetime

import click

class TestTimer(Timer):
    def __init__(self, interval: float) -> None:
        def func():
            click.echo('Test finished!')
            
        super().__init__(interval, func)
        self.start_time = datetime.now()

    def __get_elapsed_time(self):
        delta = datetime.now() - self.start_time
        return delta.seconds

    def get_rem_time(self):
        time_elapsed = self.__get_elapsed_time()
        return self.interval - time_elapsed