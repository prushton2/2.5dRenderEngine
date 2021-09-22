import turtle as tl
#Currently plan on using turtle. Pretty fast load and it allows pixel per pixel drawing.
class Render():
    def __init__(self, distances):
        self.distances = distances

    def render(self, scalar):

        s = tl.getscreen()
        t = tl.Turtle()

        s.clearscreen()
        t.left(90)
        t.speed("fastest")
        #NEED TO CHANGE HOW THESE VARS WORK

        tl.tracer(0,0)

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

        t.pencolor("black")
        


        for i in self.distances:
            t.penup()
            t.goto(i[1]*(scalar/100), 0)
            size = (1 / i[0]) * scalar
            t.pendown()
            t.fd(size/2)
            t.back(size)


        t.penup()
        t.right(90)
        t.goto(0,0)
        tl.update()
        tl.done()
