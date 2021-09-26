from Vector2 import *
import math
# from Object import *

class DistanceCalculator:

    
    @staticmethod
    def getDistance(pointA, pointB):

        sideA = abs(pointA.x - pointB.x)
        sideB = abs(pointA.y - pointB.y)
        sideC = (sideA**2 + sideB**2)**.5

        return sideC

    @staticmethod
    def getAngleToCamera(camera, point):
        a = 1
        b = DistanceCalculator.getDistance(camera.pos, point)
        c = DistanceCalculator.getDistance(point, Vector2(0, 1))

        angleC = math.degrees( math.acos( (a**2 + b**2 - c**2) / (2*a*b) ) )

        return angleC if point.x > camera.pos.x else (180 - angleC) + 180


    @staticmethod
    def getAllDistances(camera, points): 
        pass
