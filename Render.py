import turtle as tl
from Angle import *
from DistanceCalculator import *

class Scalar():
    def __init__(self, heightScalar, widthScalar):
        self.heightScalar = heightScalar
        self.widthScalar = widthScalar

#Currently plan on using turtle. Pretty fast load and it allows pixel per pixel drawing.
class Render():
    def __init__(self):
        pass
    def render(self, camera, scalar, lines):

        s = tl.getscreen()
        s.clearscreen()
        t = tl.Turtle()

        t.hideturtle()

        t.left(90)
        t.speed("fastest")
        tl.tracer(0,0)

        t.pencolor("black")
        
        
        for i in lines:
            angle1 = DistanceCalculator.getAngleToCamera(camera, i.point1)
            angle2 = DistanceCalculator.getAngleToCamera(camera, i.point2)
            # print(angle1, angle2)
            angle1 -= camera.angle
            angle2 -= camera.angle
            # print(angle1, angle2)
            
            angle1 = angle1.angle-360 if angle1.angle > 180 else angle1.angle
            angle2 = angle2.angle-360 if angle2.angle > 180 else angle2.angle
            
            # print(angle1, angle2)

            angle1 = angle1 * scalar.widthScalar
            angle2 = angle2 * scalar.widthScalar
            # print(angle1, angle2)


            point1 = Vector2(angle1, DistanceCalculator.getDistance(camera.pos, i.point1)/2)
            point2 = Vector2(angle2, DistanceCalculator.getDistance(camera.pos, i.point2)/2)
            # print(point1, point2)
            point1.y = 1/point1.y * scalar.heightScalar
            point2.y = 1/point2.y * scalar.heightScalar
            # print(point1, point2)

            
            t.penup()
            t.goto(point1.x, point1.y)
            t.pendown()
            t.begin_fill()
            t.goto(point2.x, point2.y)
            t.goto(point2.x, -1*point2.y)
            t.goto(point1.x, -1*point1.y)
            t.goto(point1.x, point1.y)
            t.end_fill()


       
        t.penup()
        tl.update()
        tl.done()
