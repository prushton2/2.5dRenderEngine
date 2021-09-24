from Vector2 import *
# from Object import *

class DistanceCalculator:

    #I am creating a right triangle to determine the distance from origin to the given point.
    #Whats cool is this: I dont really create a triangle. I am finding side distances, and I never make a triangle. Normally, I wouldnt
    #be able to know what angle im getting if I dont know what the triangle looks like. I need to use SOHCAHTOA to get my angle.
    #If I use the X differences as the opposite side of theta, that side has to be opposite of theta. This means I know how
    #the triangle is made and can ensure the angle is the angle from the center of the camera.
    @staticmethod
    def getDistanceToCamera(point, camera): #Both values should be Vector2 
        #Function tricks the renderer to render objects behind the camera. It only outputs an angle betweek -90, 90.
        import math
        sideA = abs(point.x - camera.x)
        sideB = abs(point.y - camera.y)


        sideC = ((sideA**2) + (sideB**2)) ** 0.5

        print(sideA, sideB, sideC)

        if(sideC == 0):
            sideC = 0.1

        angle = math.degrees(math.asin(sideA/sideC))

        print(angle)
        
        relativex = camera.x - point.x
        relativey = camera.y - point.y
        print(point.x, camera.x)

        if(point.x < camera.x or (point.x == camera.x and point.y < camera.y)): #This code is problematic
            angle += 180
            print("added 180")
        if((relativey < 0 and relativex > 0) or (relativey > 0 and relativex < 0)):
            angle += 90
            print("added 90")

        return sideC, angle
    @staticmethod
    def getAllDistances(points, camera): #returns a 2d array containing all distances and angles when given points
        distances = []
        for i in points:
            dist, angle = DistanceCalculator.getDistanceToCamera(i, camera.pos)
            distances.append([dist, angle])
        return distances
