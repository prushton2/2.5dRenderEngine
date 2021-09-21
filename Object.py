#This will be for objects that need to be rendered
from Vector2 import *

class Side:
    def __init__(self, point1, point2): #point1 & 2 should be a vector2
        self.point1 = point1
        self.point2 = point2

    def __repr__(self):
        return f"Side: ({self.point1}),  ({self.point2})"

    def getAllPoints(self, resolution):
        x1, y1 = resolution*self.point1.x, resolution*self.point1.y
        x2, y2 = resolution*self.point2.x, resolution*self.point2.y
        points = []
        issteep = abs(y2-y1) > abs(x2-x1)
        if issteep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        rev = False
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            rev = True
        deltax = x2 - x1
        deltay = abs(y2-y1)
        error = int(deltax / 2)
        y = y1
        ystep = None
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(x1, x2 + 1):
            if issteep:
                points.append(Vector2(y/resolution, x/resolution))
            else:
                points.append(Vector2(x/resolution, y/resolution))
            error -= deltay
            if error < 0:
                y += ystep
                error += deltax
        # Reverse the list if the coordinates were reversed
        if rev:
            points.reverse()
        return points


class Object:
    def __init__(self, sides): #sides should be an array of Sides
        self.sides = sides
    
    def getSidesInFOV(self, FOV): #sloped are the slopes of the edge of the FOV. FOV will naturally be 90, slopes should be -1 and 1
        sidesToRender = []
        slope1 = FOV[0]
        slope1 = FOV[1]
        for i in self.sides:
            if(i.point1.y > slope1 * i.point1.x and i.point1.y > slope1 * i.point1.x):
                sidesToRender.append(i)
            elif(i.point2.y > slope1 * i.point2.x and i.point2.y > slope1 * i.point2.x):
                sidesToRender.append(i)
        return sidesToRender

