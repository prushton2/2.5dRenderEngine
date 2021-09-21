import turtle as tl
#Currently plan on using turtle. Pretty fast load and it allows pixel per pixel drawing.
class Render():
    def __init__(self, distances):
        self.distances = distances

    def render(self):

        s = tl.getscreen()
        t = tl.Turtle()

        t.left(90)
        t.speed("fastest")

        tl.tracer(0,0)

        for i in range(100):
            x = i
            t.goto(i, 0)
            t.fd(x)
            t.back(2*x)

        tl.update()
        tl.done()