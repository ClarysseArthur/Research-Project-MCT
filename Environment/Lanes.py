from Trafficlight import TrafficLight

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
        self.trafficlights = []

        # lanes = [2, 3, 2, 3]
        self.north_lane = [None] * lanes[0]
        self.east_lane = [None] * lanes[1]
        self.south_lane = [None] * lanes[2]
        self.west_lane = [None] * lanes[3]

        # nrof_trafficlights_per_direction = [1, 2, 2, 1]
        for i in nrof_trafficlights_per_direction:
            for x in i:
                self.traffic_lights.append(TrafficLight())

class Approach:
    def __init__(self, side, lane_directions, traffic_lights, angle):
        self.side = side
        self.angle = angle
        self.lanes = []

        for i in len(lane_directions):
            self.lanes.append(Lane(lane_directions[i]), TrafficLight(traffic_lights[i]))

class Exit():
    def __init__(self, side):
        self.side = side

class Lane:
    def __init__(self, direction, traffic_light):
        pass