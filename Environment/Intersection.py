from queue import Queue
from Car import Car

import numpy as np


class Intersection():
    def __init__(self, approaches, exits, traffic_light_groups):
        self.approaches = approaches
        self.exits = exits
        self.traffic_light_groups = traffic_light_groups

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

    def get_cars_per_lane(self):
        cars = {}
        for approach in self.approaches:
            cars_per_approach = []
            for lane in approach.lanes:
                cars_per_approach.append(lane.get_cars())
            cars[approach.side] = cars_per_approach
        return cars

    # Input = range 0 - number of traffic light groups
    def step(self, option):
        # Check if other traffic light groups are not the same as the current one
        check_list = []
        for i in range(len(self.traffic_light_groups)):
            if i != option:
                check_list.append(self.traffic_light_groups[i].get_state())

        if check_list.count(not self.traffic_light_groups[option].get_state()) == 0 or self.traffic_light_groups[option].get_state() == True:
            self.traffic_light_groups[option].toggle()
        else:
            print('Traffic light group is not allowed to change')
        
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

    def toggle_traffic_light(self):
        self.traffic_light.toggle_state()

    @property
    def direction(self):
        return self._direction

class Trafficlight():
    # @param direction  S = 0, R = 1, L = 2
    def __init__(self, id, time_green, time_red, direction = 0, top_bulb_color = 0, middle_bulb_color = 1, bottom_bulb_color = 2):
        self.id = id
        self.time_green = time_green
        self.time_red = time_red

        self.state = False

        self.top_bulb = TrafficlightBulb(top_bulb_color, direction)
        self.middle_bulb = TrafficlightBulb(middle_bulb_color, direction)
        self.bottom_bulb = TrafficlightBulb(bottom_bulb_color, direction)

    def get_state(self):
        return self.state

    def toggle_state(self):
        self.state = not self.state

    def __str__():
        return f"Trafficlight {self.id}, state: {self.state}, time_green: {self.time_green}, time_red: {self.time_red}"

class TrafficlightBulb():
    # @param direction  S = 0, R = 1, L = 2
    # @param color      R = 0, Y = 1, G = 2
    def __init__(self, color, direction = 0):
        self.color = color
        self.direction = direction

class TrafficLightGroup():
    def __init__(self, traffic_lights):
        self.traffic_lights = traffic_lights

    def check_compatibilty(self, traffic_light):
        if traffic_light in self.traffic_lights:
            return True
        else:
            return False

    def toggle(self):
        for traffic_light in self.traffic_lights:
            traffic_light.toggle_state()

    def get_state(self):
        if True in [traffic_light.get_state() for traffic_light in self.traffic_lights]:
            return True
        else:
            return False
