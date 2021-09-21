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
        #NEED TO CHANGE HOW THESE VARS WORK

        tl.tracer(0,0)

        for i in self.distances:
            t.goto(i[1], 0)
            size = (1 / i[0]) * 200
            t.fd(size/2)
            t.back(size)

        tl.update()
        tl.done()
