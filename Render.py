import turtle as tl
from Angle import *

#Currently plan on using turtle. Pretty fast load and it allows pixel per pixel drawing.
class Render():
    def __init__(self, distances):
        self.distances = distances

    def render(self, camera, scalar):

        s = tl.getscreen()
        t = tl.Turtle()

        s.clearscreen()
        t.left(90)
        t.speed("fastest")

        tl.tracer(0,0)

        t.pencolor("black")
        

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
