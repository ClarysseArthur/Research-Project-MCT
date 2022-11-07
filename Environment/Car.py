import numpy as np

class Car:
    def __init__(self, start, lane):
        self.start = start
        self.lane = lane
        self.destination = self.define_destination()
        self._time = np.random.rand()

    def define_destination(self):
        #['N-ESW', 'E-NW', 'E-S', 'S-NEW', 'W-ES', 'W-N'])
        if self.start == 'N':
            if self.lane == 0:
                return 'E'
            else:
                return 'W'
        elif self.start == 'E':
            if self.lane == 0:
                if np.random.rand() < 0.5:
                    return 'N'
                else:
                    return 'W'
            elif self.lane == 1:
                return 'W'
            else:
                return 'S'
        elif self.start == 'S':
            if self.lane == 0:
                return 'E'
            else:
                return 'W'
        elif self.start == 'W':
            if self.lane == 0:
                if np.random.rand() < 0.5:
                    return 'E'
                else:
                    return 'S'
            elif self.lane == 1:
                return 'E'
            else:
                return 'N'

    
    @property
    def time(self):
        return self._time