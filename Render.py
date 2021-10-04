import turtle as tl
from Angle import *
from DistanceCalculator import *

class Scalar():
    def __init__(self, heightScalar, widthScalar):
        self.heightScalar = heightScalar
        self.widthScalar = widthScalar

#Currently plan on using turtle. Pretty fast load and it allows pixel per pixel drawing.
class Render():
    def __init__(self, renderDebugInfo):
        self.renderDebugInfo = renderDebugInfo
        self.t = tl.Turtle()
        self.s = tl.getscreen()
    def render(self, camera, scalar, lines):


        
        self.s.clearscreen()


        self.t.hideturtle()
        self.t.speed("fastest")
        tl.tracer(0,0)

        self.t.left(90)

        
        self.t.pencolor("black")
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

            self.t.fillcolor("black")
            self.t.penup()
            self.t.goto(point1.x, point1.y)
            self.t.pendown()
            self.t.begin_fill()
            self.t.goto(point2.x, point2.y)
            self.t.goto(point2.x, -1*point2.y)
            self.t.goto(point1.x, -1*point1.y)
            self.t.goto(point1.x, point1.y)
            self.t.end_fill()

        size = self.s.screensize()

        self.t.pencolor("white")
        self.t.penup()
        self.t.goto(-1*size[0], size[1])
        self.t.fillcolor("white")
        self.t.begin_fill()
        self.t.pendown()
        self.t.goto((camera.fov[0].angle - 360)*scalar.widthScalar, size[1])
        self.t.goto((camera.fov[0].angle - 360)*scalar.widthScalar, -1*size[1])
        self.t.goto(-1*size[0], -1*size[1])
        self.t.end_fill()
       
        self.t.penup()
        self.t.goto(size[0], size[1])
        self.t.fillcolor("white")
        self.t.begin_fill()
        self.t.pendown()
        self.t.goto((camera.fov[1].angle)*scalar.widthScalar, size[1])
        self.t.goto((camera.fov[1].angle)*scalar.widthScalar, -1*size[1])
        self.t.goto(size[0], -1*size[1])
        self.t.end_fill()

        self.t.penup()
        if(self.renderDebugInfo):
            self.t.pencolor("black")
            self.t.goto(-1*size[0]+30, size[1]-10)
            self.t.pendown()
            self.t.write(f"X Pos: {camera.pos.x}")
            self.t.penup()
            self.t.goto(-1*size[0]+30, size[1]-20)
            self.t.pendown()
            self.t.write(f"Y Pos: {camera.pos.y}")
            self.t.penup()
            self.t.goto(-1*size[0]+30, size[1]-30)
            self.t.pendown()
            self.t.write(f" Angle: {camera.angle.angle}")
            self.t.penup()


        self.t.penup()
        tl.update()
        tl.done()
