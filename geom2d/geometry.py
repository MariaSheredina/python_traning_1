
#from geom2d import *
from geom2d.point import Point

l1 = [Point(2, 1), Point(0, 0), Point(1, 2)]

# def x(p):
    # return p.x

# def y(p):
    # return p.y

# l2 = sorted(l1, key=y)
l2 = sorted(l1, key=lambda p: p.x)
# print("ок")
print(l1)
print(l2)


# l1 = [Point(0, 0), Point(1, 2), Point(2, 1)]
# l2 = [Point(0, 0), Point(1, 2), Point(2, 1)]
# l2 = list(l1)
# l2[0] = Point (0, 0)

# print(l1 == l2)
# print(a.distance(b))
# print(a == b)
# print(a == Point(0, 0))
