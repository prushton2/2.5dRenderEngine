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

    def isInFov(self, camera):
        angle1 = DistanceCalculator.getAngleToCamera(camera, self.point1)
        angle2 = DistanceCalculator.getAngleToCamera(camera, self.point2)

        lowLimit = camera.angle - Angle(90)

        return angle1 > lowLimit or angle2 > lowLimit #If either angle is within 90 degrees of the camera's center



class Object:
    def __init__(self, sides): #sides should be an array of Sides
        self.sides = sides
    
    def getSidesInFov(self, camera):
        lines = []
        for i in self.sides:
            if(i.isInFov(camera)):
                lines.append(i)
        return lines
    

class Polygon(Object):
    def __init__(self, points): #Points should be a list of Vector2s of the points of the shape
        self.points = points
        self.sides = []
        for i,j in enumerate(points):
            self.sides.append(Side(points[i], points[i-1]))
    def update(self):
        for i,j in enumerate(self.points):
            self.sides.append(Side(self.points[i], self.points[i-1]))

