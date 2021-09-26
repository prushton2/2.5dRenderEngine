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

        print(angle1, angle1, camera.fov)

        if(angle1 > camera.fov[0] and camera.fov[1] > angle1):
            return True
        elif(angle2 > camera.fov[0] and camera.fov[1] > angle2):
            return True
        return False



class Object:
    def __init__(self, sides): #sides should be an array of Sides
        self.sides = sides
    
    def getSidesInFov(self, camera):
        lines = []
        for i in self.sides:
            if(i.isInFov(camera)):
                lines.append(i)
        return lines
    