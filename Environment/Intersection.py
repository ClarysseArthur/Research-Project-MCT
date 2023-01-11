from queue import Queue
import time
from Car import Car
from threading import Thread
from collections import Counter

import numpy as np
import math
from Render_CMD import render_cmd
from Render_3D import render_3d


class Intersection():
    # @param u: Uitstroomvector
    # @param i: Instroomvector
    # @param V: Lichtcombinatie matrix
    def __init__(self, approaches, exits, traffic_light_groups, u, i, V, a_max):
        self.approaches = approaches
        self.exits = exits
        self.traffic_light_groups = traffic_light_groups

        self.init_approaches = approaches
        self.init_exits = exits
        self.init_traffic_light_groups = traffic_light_groups

        self.waiting_cars_at_start = 0

        self.metrics = []

        self.done = False
        self.steps_done = 0

        self.u = np.array(u)
        self.i = np.array(i)
        self.V = np.array(V)
        self.l = len(u)
        self.prev_n = self.get_cars_per_lane()
        self.a_max = a_max
        self.prev_drukte = 0

        self.lanes = []
        for approach in self.approaches:
            for lane in approach.lanes:
                self.lanes.append(lane)

        self._drukte_hist = []

    def generate_random_traffic(self, number_of_cars_to_generate):
        for x in self.lanes:
            for i in range(50):
                x.add_vehicle(Car(1, 1))

        self.prev_n = self.get_cars_per_lane()

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

    def clear_cars(self):
        for approach in self.approaches:
            for lane in approach.lanes:
                lane.clear()

    def step(self, action):
        action = np.array(action)
        # print(action)
        action_matrix = np.transpose(np.transpose(self.V) * action)
        epsilon = np.sum(action)
        
        for x in action_matrix:
            lanes = np.where(x != 0)[0]         # Get lanes to turn green

            if len(lanes) > 0:
                steps = x[lanes][0]             # Get time to turn green
            else:
                steps = 0

            for step in range(steps):
                for lane in lanes:
                    self.lanes[lane].step()

        n = self.prev_n - (np.sum(action_matrix, 0) * self.u) + (epsilon * self.i)
        n = np.where(n < 0, 0, n)
        self.prev_n = n

        if np.all(n <= 1):
            drukte = 0
        else:
            d1 = np.sum(n**2)
            d2 = np.sum(n)**2
            drukte = d1 / d2
            print('D1: ', d1, '| D2: ', d2, '| Drukte: ', drukte)

        # print('n: ', n, '| n**2: ', n**2, '| np.sum(n**2): ', np.sum(n**2), '| np.sum(n)**2: ', np.sum(n)**2)

        reward = 1 - drukte
        # reward = self.prev_drukte - drukte

        # if np.any(n > 100):
        #     reward = reward - 1
        # elif np.any(n > 50):
        #     reward = reward - 0.5
        # elif np.any(n > 25):
        #     reward = reward - 0.25
        

        self.prev_drukte = drukte

        print('Action: ', action, '| Sum action M', np.sum(action_matrix, 0) * self.u, '| Reward: ', round(reward, 2), '| Drukte: ', round(drukte, 2), 'n', n)

        if self.steps_done < 500:
            self.steps_done += 1
        else:
            self.done = True
            self.steps_done = 0
            print('Drukte: ', drukte)
            self._drukte_hist.append(n)

        return n, reward, self.done, {}

    def close(self):
        return self.metrics

    def render(self):
        render_cmd(self.approaches, self.exits)
        render_3d(self.approaches, self.exits)

    def reset(self):
        self.approaches = self.init_approaches
        self.exits = self.init_exits
        self.traffic_light_groups = self.init_traffic_light_groups
        self.metrics = []
        self.waiting_cars_at_start = 0
        self.done = False
        self.steps = 0
        self.clear_cars()
        self.generate_random_traffic(50)
        self.prev_n = self.get_cars_per_lane()
        self.prev_drukte = 0

        return self.get_cars_per_lane()

    def __str__(self):
        return f'Approaches: {self.approaches}, Exits: {self.exits}, Traffic light groups: {self.traffic_light_groups}'

    @property
    def drukte_hist(self):
        return self._drukte_hist


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
        if self.queue.qsize() > 0:
            self.queue.get()

    def clear(self):
        self.queue = Queue()

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
