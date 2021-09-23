#This will be for objects that need to be rendered
from Vector2 import *
from DistanceCalculator import *

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
    
    def getSidesInFOV(self, camera): #sloped are the slopes of the edge of the FOV. FOV will naturally be 90, slopes should be -1 and 1
        sidesToRender = []
        slope1 = camera.fov[0]
        slope1 = camera.fov[1]
        for i in self.sides:
            if(self.isPointInFov(camera, i.point1) or self.isPointInFov(camera, i.point2)):
                sidesToRender.append(i)

        return sidesToRender
    
    def isPointInFov(self, camera, point):
        distance, angle = DistanceCalculator.getDistanceToCamera(point, camera.pos)
        lowFov = camera.angle + camera.fov[0] if camera.angle + camera.fov[0] > -1 else camera.angle + camera.fov[0] + 360
        highFov = camera.angle + camera.fov[1] if camera.angle + camera.fov[1] < 359 else camera.angle + camera.fov[1] - 360
        
        #Problem - Tests if the angle is greater than low FOV OR less than high FOV. Both conditions need to take other part of FOV into account, they always return true
        
        print(f"XXXXX Camera angle: {camera.angle} Object Angle: {angle} FOV: {camera.fov} Fov Angles ({lowFov}, {highFov}) passed test: ", end = "")

        if(lowFov < angle and angle < highFov):
            print(f"First Test")
            return True
        
        if(angle > lowFov and lowFov >= highFov):
            print(f"Second Test")
            return True

        if(angle < highFov and highFov <= lowFov):
            print(f"Third Test")
            return True

        print(f"Failed all tests")
        return False

camera = Camera(Vector2(0, 0), 0, (-45, 45))

sqaure = Object([
    Side(Vector2(1, 2), Vector2(1,4)),
    Side(Vector2(5, 4), Vector2(1,4)),
    Side(Vector2(5, 4), Vector2(5,2)),
    Side(Vector2(1, 2), Vector2(5,2))
])

# print("Points between 315 and 45 should pass")
# failedTests = []
# passedTests = []
# for i in range(360):
#     camera.angle = i
#     predictedOutput = i > 315 or i < 45 
#     output = sqaure.isPointInFov(camera, Vector2(1, 1))
#     print(f"Testing {i} degrees:    Output is {output}, should be {predictedOutput}")
#     if(output == predictedOutput):
#         passedTests.append((i, output, predictedOutput))
#     if(output != predictedOutput):
#         failedTests.append((i, output, predictedOutput))
# print(passedTests)
# print("------------------")
# print(failedTests)

print(sqaure.isPointInFov(camera, Vector2(-1, -1)))
