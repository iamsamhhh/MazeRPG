import math
from mimetypes import init
from operator import truediv

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return "{}, {}".format(self.x, self.y)
    
    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2(self.x / other.x, self.y / other.y)
    
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __cmp__(self, other):
        if self.x == other.x and self.y == other.y:
            return True

    def normalise(self):
        mag = self.magnitude()
        return self/Vector2(mag, mag)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

class Transform:
    def __init__(self) -> None:
        self.position = Vector2(0, 0)
        self.rotation = 0.0
        self.scale = Vector2(1, 1)