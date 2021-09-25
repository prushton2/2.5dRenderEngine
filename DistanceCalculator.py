from Vector2 import *
import math
# from Object import *

class DistanceCalculator:

    
    @staticmethod
    def getDistanceToCamera(camera, point):

        sideA = math.abs(camera.pos.x - point.x)
        sideB = math.abs(camera.pos.y - point.y)
        sideC = (sideA**2 + sideB**2)**.5

        

    @staticmethod
    def getAllDistances(camera, points): 
        pass
