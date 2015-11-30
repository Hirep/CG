from math import sin, cos, pi
__author__ = 'Dima'


class Circle:
    points_x = []
    points_y = []

    def __init__(self, center_x, center_y, radius, segments):
        self.center_X = center_x
        self.center_Y = center_y
        self.radius = radius
        if (segments is None) or (segments < 16):
            self.segments = 16
        step = 0
        while step <= 2 * pi:
            self.points_x.append(self.center_X + self.radius * cos(step))
            self.points_y.append(self.center_Y + self.radius * sin(step))
            step += (2 * pi) / segments


cir1 = Circle(1, 1, 1, 48)
z = zip(cir1.points_x, cir1.points_y)
print(list(z), sep='\n')
