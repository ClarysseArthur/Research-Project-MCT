from queue import Queue
import queue
from Car import Car
from Trafficlight import TrafficLight

import numpy as np

import time

class Intersection():
    ###
    # Intersection class
    # ---
    # This class is used to simulate an intersection
    # ---
    # @param number_directions:                 Number of directions the intersection has - same as len(lanes)
    # @param lanes:                             List of lanes that are connected to the intersection - lanes[0] is the lane that is connected to the intersection from the top
    # @param nrof_trafficlights_per_direction:  Number of trafficlights per direction - nrof_trafficlights_per_direction[0] is the number of trafficlights for the top direction
    # @param traffic_lights:                    List of traffic lights that are connected to the intersection - Order is defined in nrof_trafficlights_per_direction
    #
    ###
    def __init__(self, number_directions, lanes, nrof_trafficlights_per_direction, traffic_lights):
        self.number_directions = number_directions

        # lanes = [2, 3, 2, 3]
        self.north_lane = [None] * lanes[0]
        self.east_lane = [None] * lanes[1]
        self.south_lane = [None] * lanes[2]
        self.west_lane = [None] * lanes[3]

        # nrof_trafficlights_per_direction = [1, 2, 2, 1]
        for i in nrof_trafficlights_per_direction:
            





        self.sides = ['N', 'E', 'S', 'W']
        self.possible = [['ES', 'W'], ['NW', 'W', 'S'], ['NE', 'W'], ['ES', 'E', 'N']]
        self.nr_lanes = [2, 3, 2, 3]
        self.green_posssible = ['N-ESW', 'E-NW', 'E-S', 'S-NEW', 'W-NS', 'W-E'] # = light id

        self.north_lane = [Queue(), Queue()] # 2 lanes
        self.east_lane = [Queue(), Queue(), Queue()] # 3 lanes
        self.south_lane = [Queue(), Queue()] # 2 lanes
        self.west_lane = [Queue(), Queue(), Queue()] # 3 lanes

        # Lights
        self.north_light = TrafficLight(0, 10, 10, 0, 0, 1, 0, 2, 0)
        self.east_light = TrafficLight(1, 10, 10, 0, 0, 1, 0, 2, 0)

    def generate_cars(self):
        if np.random.rand() > 0.75:
            if np.random.rand() < 0.5: 
                #!------North------!#
                lane = np.random.randint(0, 2)
                self.north_lane[lane].put(Car('N', self.possible[0][lane]))
            else:
                #!------South------!#
                lane = np.random.randint(0, 2)
                self.south_lane[lane].put(Car('S', self.possible[2][lane]))

        else:
            if np.random.rand() < 0.5:
                #!------East------!#
                lane = np.random.randint(0, 3)
                self.east_lane[lane].put(Car('E', self.possible[1][lane]))
            else:
                #!------west------!#
                lane = np.random.randint(0, 3)
                self.west_lane[lane].put(Car('W', self.possible[3][lane]))

    def clear_green_light(self, light_id, time_s):
        current_time = int(time.time() * 1000)
        end_time = current_time + (time_s * 1000)
        i = 0

        while end_time > current_time:
            i += 1
            self.clear_queue(light_id)
            current_time = int(time.time() * 1000)
            print('#' * i, end='\r')
        print('')

    def clear_queue(self, light_id):
        #['N-ESW', 'E-NW', 'E-S', 'S-NEW', 'W-ES', 'W-N']
        match light_id:
            case 0:
                car1 = self.north_lane[0].get()
                car2 = self.north_lane[1].get()
                time.sleep(np.average([car1.time, car2.time]))

            case 1:
                car1 = self.east_lane[0].get()
                car2 = self.east_lane[1].get()
                time.sleep(np.average([car1.time, car2.time]))

            case 2:
                car = self.east_lane[2].get()
                time.sleep(car.time)
                
            case 3:
                car1 = self.south_lane[0].get()
                car2 = self.south_lane[1].get()
                time.sleep(np.average([car1.time, car2.time]))

            case 4:
                car1 = self.west_lane[0].get()
                car2 = self.west_lane[1].get()
                time.sleep(np.average([car1.time, car2.time]))

            case 5:
                car = self.west_lane[2].get()
                time.sleep(car.time)

    def print_queues(self):
        # Print size of queus 
        print('North: ', self.north_lane[0].qsize(), self.north_lane[1].qsize())
        print('East: ', self.east_lane[0].qsize(), self.east_lane[1].qsize(), self.east_lane[2].qsize())
        print('South: ', self.south_lane[0].qsize(), self.south_lane[1].qsize())
        print('West: ', self.west_lane[0].qsize(), self.west_lane[1].qsize(), self.west_lane[2].qsize())

intersection = Intersection()
intersection.generate_cars()
intersection.print_queues()
intersection.clear_green_light(0, 15)
intersection.print_queues()