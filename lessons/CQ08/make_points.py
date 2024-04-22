"""Test Point functions."""

from point import Point

point_1: Point = Point(2.0, 2.0)
print(point_1.x, point_1.y)


point_1.scale_by(2)
print(point_1.x, point_1.y)

point_2: Point = point_1.scale(3)
print(point_2.x, point_2.y)
