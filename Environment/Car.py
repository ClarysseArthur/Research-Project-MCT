import numpy as np

class Car:
    def __init__(self, approach, exit):
        self.spproach = approach
        self.exit = exit
        self._time = np.random.rand()
        self._waiting_time = 0
    
    @property
    def time(self):
        return self._time

    @property
    def waiting_time(self):
        return self._waiting_time

    @waiting_time.setter
    def waiting_time(self, value):
        self._waiting_time = value