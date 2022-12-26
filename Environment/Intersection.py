from queue import Queue
import time
from Environment.Car import Car
from threading import Thread
from collections import Counter

import numpy as np
from Environment.Render_CMD import render_cmd


class Intersection():
    def __init__(self, approaches, exits, traffic_light_groups):
        self.approaches = approaches
        self.exits = exits
        self.traffic_light_groups = traffic_light_groups

        self.init_approaches = approaches
        self.init_exits = exits
        self.init_traffic_light_groups = traffic_light_groups

        self.waiting_cars_at_start = 0

        self.metrics = []

        self.done = False
        self.steps = 0

    def generate_traffic(self, number_of_cars_to_generate):
        approach_lanes = sorted((set([approach.get_length() for approach in self.approaches])), reverse=True)
        number_of_directions = [approach.get_directions() for approach in self.approaches]
        number_of_approaches_per_lane = Counter([approach.get_length() for approach in self.approaches])

        intersection_lane_info = []
        for x in approach_lanes:
            intersection_lane_info.append([x, number_of_approaches_per_lane[x] - 1])

        split = self.calculate_natural_traffic(intersection_lane_info)

        for i in range(number_of_cars_to_generate):
            rand = np.random.rand()

            if rand <= split[0]:
                approach = np.random.choice(
                    [approach for approach in self.approaches if approach.get_length() == approach_lanes[0]])
                lane = np.random.choice(approach.lanes)
                lane.add_vehicle(
                    Car(approach.side, np.random.choice(lane.direction)))

            elif rand <= split[1]:
                approach = np.random.choice(
                    [approach for approach in self.approaches if approach.get_length() == approach_lanes[1]])
                lane = np.random.choice(approach.lanes)
                lane.add_vehicle(
                    Car(approach.side, np.random.choice(lane.direction)))

            elif rand <= split[2]:
                approach = np.random.choice(
                    [approach for approach in self.approaches if approach.get_length() == approach_lanes[2]])
                lane = np.random.choice(approach.lanes)
                lane.add_vehicle(
                    Car(approach.side, np.random.choice(lane.direction)))

            elif rand <= split[3]:
                approach = np.random.choice(
                    [approach for approach in self.approaches if approach.get_length() == approach_lanes[3]])
                lane = np.random.choice(approach.lanes)
                lane.add_vehicle(
                    Car(approach.side, np.random.choice(lane.direction)))

    def calculate_natural_traffic(self, intersection_info):
        if len(intersection_info) == 1:
            return [1, 0, 0, 0]

        elif len(intersection_info) == 2:
            split_values = [[0, 0, 0.4, 0.6], [0, 0, 0.65, 0.70], [0, 0, 0.8, 0.9]]
            return [split_values[intersection_info[0][1]][intersection_info[0][0]], 1, 0, 0]

        elif len(intersection_info) == 3:
            split_values_max = [[0, 0, 0.35, 0.45], [0, 0, 0.45, 0.5]]
            split_values_min = [[0, 0, 0.7, 0.8], [0, 0, 0.8, 0.9]]
            return [split_values_max[intersection_info[0][1]][intersection_info[0][0]], split_values_min[intersection_info[1][1]][intersection_info[1][0]], 1, 0]

        elif len(intersection_info) == 4:
            return [0.45, 0.65, 0.85, 1]

    def get_total_cars_waiting(self):
        total = 0
        for approach in self.approaches:
            for lane in approach.lanes:
                total += lane.get_cars()
        return total

    def get_cars_per_lane(self):
        cars = []
        for approach in self.approaches:
            cars_per_approach = []
            for lane in approach.lanes:
                cars_per_approach.append(lane.get_cars())
            for x in cars_per_approach:
                cars.append(x)
        return np.array(cars)

    # Input = range 0 - number of traffic light groups
    def step(self, option):
        check_list = []
        wrong_option = 0

        if self.steps < 100:
            self.steps += 1
        else:
            self.done = True

        if np.random.random() < 0.5:
            self.generate_traffic(np.random.randint(1, 3))

        if option != 0:
            option = option - 1

            for i in range(len(self.traffic_light_groups)):
                if i != option:
                    check_list.append(self.traffic_light_groups[i].get_state())

            if check_list.count(not self.traffic_light_groups[option].get_state()) == 0 or self.traffic_light_groups[option].get_state() == True:
                self.waiting_cars_at_start = self.get_total_cars_waiting()
                self.traffic_light_groups[option].toggle()

            else:
                print('Traffic light group is not allowed to change')
                wrong_option = -100

        for approach in self.approaches:
            for lane in approach.lanes:
                lane.step()

        total_cars_cleared = self.waiting_cars_at_start - self.get_total_cars_waiting()

        self.metrics.append(self.get_total_cars_waiting())

        # return: state - reward - done - info
        #                 └> reward = total_Cars_cleared - total_cars_waiting * time
        return self.get_cars_per_lane(), total_cars_cleared - self.get_total_cars_waiting() - wrong_option, self.done, {}

    def close(self):
        return self.metrics

    def render(self):
        render_cmd(self.approaches, self.exits)

    def reset(self):
        self.approaches = self.init_approaches
        self.exits = self.init_exits
        self.traffic_light_groups = self.init_traffic_light_groups
        self.metrics = []
        self.waiting_cars_at_start = 0

        return self.get_cars_per_lane()

    def __str__(self):
        return f'Approaches: {self.approaches}, Exits: {self.exits}, Traffic light groups: {self.traffic_light_groups}'


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

    def step(self):
        for lane in self.lanes:
            lane.clear_queue()

    def __str__(self):
        return f'Side: {self.side}, Angle: {self.angle}, Lanes: {self.lanes}'

    @property
    def lanes(self):
        return self._lanes


class Exit():
    def __init__(self, side, lanes):
        self.side = side
        self.lanes = lanes

    def get_length(self):
        return len(self.lanes)

    def __str__(self):
        return f'Side: {self.side}, Lanes: {self.lanes}'


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

    def step(self):
        if self.traffic_light.state and self.queue.qsize() > 0:
            self.queue.get()

    def __str__(self):
        return f'Direction: {self.direction}, Traffic light: {self.traffic_light}, Is exit: {self.is_exit}, Exits: {self.exits}'

    @property
    def direction(self):
        return self._direction


class Trafficlight():
    # @param direction  S = 0, R = 1, L = 2
    def __init__(self, id, direction=0, top_bulb_color=0, middle_bulb_color=1, bottom_bulb_color=2):
        self.id = id
        self._state = False

        self.top_bulb = TrafficlightBulb(top_bulb_color, direction)
        self.middle_bulb = TrafficlightBulb(middle_bulb_color, direction)
        self.bottom_bulb = TrafficlightBulb(bottom_bulb_color, direction)

    def toggle_state(self):
        self._state = not self._state
        # print(f'State changed from {not self.state} to {self.state}')

    def __str__(self):
        return f"Trafficlight {self.id}, State: {self.state}, Light bulbs: {self.top_bulb}, {self.middle_bulb}, {self.bottom_bulb}"

    @property
    def state(self):
        return self._state


class TrafficlightBulb():
    # @param direction  S = 0, R = 1, L = 2
    # @param color      R = 0, Y = 1, G = 2
    def __init__(self, color, direction=0):
        self.color = color
        self.direction = direction

    def __str__(self):
        return f"Color: {self.color}, Direction: {self.direction}"


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
        if True in [traffic_light.state for traffic_light in self.traffic_lights]:
            return True
        else:
            return False

    def __str__(self):
        return f"Traffic lights: {self.traffic_lights}"
