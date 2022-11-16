import numpy as np

class Car:
    def __init__(self, approach, exit):
        self.spproach = approach
        self.exit = exit
        self._time = np.random.rand()
    
    @property
    def time(self):
        return self._time