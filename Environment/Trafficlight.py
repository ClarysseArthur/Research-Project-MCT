class Trafficlight():
    def __init__(self, id, time_green, time_red, top_bulb_color = 0, top_bulb_direction = 0, middle_bulb_color = 1, middle_bulb_direction = 0, bottom_bulb_color = 2, bottom_bulb_direction = 0):
        self.id = id
        self.time_green = time_green
        self.time_red = time_red

        self.top_bulb = TrafficlightBulb(top_bulb_color, top_bulb_direction)
        self.middle_bulb = TrafficlightBulb(middle_bulb_color, middle_bulb_direction)
        self.bottom_bulb = TrafficlightBulb(bottom_bulb_color, bottom_bulb_direction)


class TrafficlightBulb():
    def __init__(self, color, direction = 0):
        # 0 = red, 1 = yellow, 2 = green
        self.color = color

        # 0 = All, 1 = Straight, 2 = Right, 3 = Left
        self.direction = direction