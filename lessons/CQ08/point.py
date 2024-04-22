"""Point defintion."""

from __future__ import annotations

class Point:
    """Makes a point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Init function."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scales point by factor."""
        self.x = factor * self.x
        self.y = factor * self.y
    
    def scale(self, factor: int) -> Point:
        """Creates new point scaled by factor."""
        point_x = factor * self.x
        point_y = factor * self.y
        return Point(point_x, point_y)