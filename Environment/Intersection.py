from queue import Queue
from Car import Car

import numpy as np


class Intersection():
    def __init__(self, approaches, exits):
        self.approaches = approaches
        self.exits = exits

    def generate_traffic(self, number_of_cars_to_generate):
        approach_lanes = sorted((set([approach.get_length() for approach in self.approaches])), reverse=True)
        number_of_directions = [approach.get_directions() for approach in self.approaches]

        split = 0
        match len(approach_lanes):
            case 1:
                split = [1, 0, 0, 0]
            case 2:
                split = [0.75, 1, 0, 0]
            case 3:
                split = [0.5, 0.8, 1, 0]
            case 4:
                split = [0.4, 0.7, 0.9, 1]

        for i in range(number_of_cars_to_generate):
            rand = np.random.rand()

            if rand <= split[0]:
                approach = np.random.choice([approach for approach in self.approaches if approach.get_length() == approach_lanes[0]])
                lane = np.random.choice(approach.lanes)
                lane.add_vehicle(Car(approach.side, np.random.choice(lane.direction)))

            elif rand <= split[1]:
                approach = np.random.choice([approach for approach in self.approaches if approach.get_length() == approach_lanes[1]])
                lane = np.random.choice(approach.lanes)
                lane.add_vehicle(Car(approach.side, np.random.choice(lane.direction)))

            elif rand <= split[2]:
                approach = np.random.choice([approach for approach in self.approaches if approach.get_length() == approach_lanes[2]])
                lane = np.random.choice(approach.lanes)
                lane.add_vehicle(Car(approach.side, np.random.choice(lane.direction)))
                
            elif rand <= split[3]:
                approach = np.random.choice([approach for approach in self.approaches if approach.get_length() == approach_lanes[3]])
                lane = np.random.choice(approach.lanes)
                lane.add_vehicle(Car(approach.side, np.random.choice(lane.direction)))
                

        # if np.random.rand() > 0.75:
        #     if np.random.rand() < 0.5: 
        #         #!------North------!#
        #         lane = np.random.randint(0, 2)
        #         self.north_lane[lane].put(Car('N', self.possible[0][lane]))
        #     else:
        #         #!------South------!#
        #         lane = np.random.randint(0, 2)
        #         self.south_lane[lane].put(Car('S', self.possible[2][lane]))

        # else:
        #     if np.random.rand() < 0.5:
        #         #!------East------!#
        #         lane = np.random.randint(0, 3)
        #         self.east_lane[lane].put(Car('E', self.possible[1][lane]))
        #     else:
        #         #!------west------!#
        #         lane = np.random.randint(0, 3)
        #         self.west_lane[lane].put(Car('W', self.possible[3][lane]))

    def get_cars_per_lane(self):
        cars = {}
        for approach in self.approaches:
            cars_per_approach = []
            for lane in approach.lanes:
                cars_per_approach.append(lane.get_cars())
            cars[approach.side] = cars_per_approach
        return cars

class Approach:
    def __init__(self, side, lanes, angle):
        self.side = side
        self.angle = angle
        self._lanes = lanes

    def get_length(self):
        return len(self.lanes)

    def get_directions(self):
        return [lane.direction for lane in self.lanes]

    def get_lane_with_direction(self, direction):
        return [lane for lane in self.lanes if lane.direction == direction]

    @property
    def lanes(self):
        return self._lanes

class Exit():
    def __init__(self, side, lanes):
        self.side = side
        self.lanes = lanes

class Lane:
    # @param direction  S = 0, R = 1, L = 2
    def __init__(self, direction, traffic_light, is_exit, exits):
        self._direction = direction
        self.traffic_light = traffic_light
        self.is_exit = is_exit
        self.exits = exits
        self.queue = Queue()

    def add_vehicle(self, vehicle):
        self.queue.put(vehicle)

    def get_cars(self):
        return self.queue.qsize()

    @property
    def direction(self):
        return self._direction

# ---
class Trafficlight():
    # @param direction  S = 0, R = 1, L = 2
    def __init__(self, id, time_green, time_red, direction = 0, top_bulb_color = 0, middle_bulb_color = 1, bottom_bulb_color = 2):
        self.id = id
        self.time_green = time_green
        self.time_red = time_red

        self.top_bulb = TrafficlightBulb(top_bulb_color, direction)
        self.middle_bulb = TrafficlightBulb(middle_bulb_color, direction)
        self.bottom_bulb = TrafficlightBulb(bottom_bulb_color, direction)


class TrafficlightBulb():
    # @param direction  S = 0, R = 1, L = 2
    # @param color      R = 0, Y = 1, G = 2
    def __init__(self, color, direction = 0):
        self.color = color
        self.direction = direction