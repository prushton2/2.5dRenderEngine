from Vector2 import *
class DistanceCalculator:

    #I am creating a right triangle to determine the distance from origin to the given point.
    #Whats cool is this: I dont really create a triangle. I am finding side distances, and I never make a triangle. Normally, I wouldnt
    #be able to know what angle im getting if I dont know what the triangle looks like. I need to use SOHCAHTOA to get my angle.
    #If I use the X differences as the opposite side of theta, that side has to be opposite of theta. This means I know how
    #the triangle is made and can ensure the angle is the angle from the center of the camera.
    @staticmethod
    def getDistanceToCamera(point, camera): #Both values should be Vector2
        import math
        sideA = abs(point.x - camera.x)
        sideB = abs(point.y - camera.y)

        sideC = ((sideA**2) + (sideB**2)) ** 0.5

        if(sideC == 0):
            sideC = 0.1

        angle = math.degrees(math.asin(sideA/sideC))

        angle = -1*angle if point.x < camera.x else angle #Make it negative if the point is on the left

        return sideC, angle
    @staticmethod
    def getAllDistances(points, camera): #returns a 2d array containing all distances and angles when given points
        distances = []
        for i in points:
            dist, angle = DistanceCalculator.getDistanceToCamera(i, camera)
            distances.append([dist, angle])
        return distances
