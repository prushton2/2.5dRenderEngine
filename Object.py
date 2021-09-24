#This will be for objects that need to be rendered
from Vector2 import *
from DistanceCalculator import *
from Angle import *

class Camera:
    def __init__(self, cameraPos, cameraAngle, fov):
        self.pos = cameraPos
        self.angle = cameraAngle
        self.fov = fov

class Side:
    def __init__(self, point1, point2): #point1 & 2 should be a vector2
        self.point1 = point1
        self.point2 = point2

    def __repr__(self):
        return f"Side: ({self.point1}),  ({self.point2})"

    


class Object:
    def __init__(self, sides): #sides should be an array of Sides
        self.sides = sides
    
    