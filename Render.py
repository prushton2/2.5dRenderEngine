import turtle as tl
from Angle import *

#Currently plan on using turtle. Pretty fast load and it allows pixel per pixel drawing.
class Render():
    def __init__(self, distances):
        self.distances = distances

    def render(self, scalar, camera):

        s = tl.getscreen()
        t = tl.Turtle()

        s.clearscreen()
        t.left(90)
        t.speed("fastest")
        #NEED TO CHANGE HOW THESE VARS WORK

        tl.tracer(0,0)

        t.pencolor("black")
        


        for i in self.distances:
            x = camera.angle + Angle(i[1])
            t.penup()
            t.goto(x*(scalar/100), 0)
            size = (1 / i[0]) * scalar
            t.pendown()
            t.fd(size/2)
            t.back(size)


        t.pencolor("red")
        
        t.penup()
        t.goto(-45*(scalar/100), 0)
        t.pendown()
        t.fd(1000)
        t.back(2000)
        t.penup()

        t.goto(45*(scalar/100), 0)
        t.pendown()
        t.fd(1000)
        t.back(2000)
        t.penup()


        t.penup()
        t.right(90)
        t.goto(0,0)
        tl.update()
        tl.done()
