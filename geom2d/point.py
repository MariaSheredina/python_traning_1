
from math import sqrt


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx*dx + dy*dy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.y < other.y

    def __repr__(self):
       #return "Point(" % + str(self.x) + ", " + str(self.y) + ")"
       return "Point(%s, %s)" % (self.x, self.y)
