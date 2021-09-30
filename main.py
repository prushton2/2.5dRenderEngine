from Vector2 import *
from DistanceCalculator import *
from Object import *
from Render import *
from Angle import *

from tkinter import *


Objects = [
    Object([
        Side(Vector2(1, 2), Vector2(1,4)),
        Side(Vector2(5, 4), Vector2(1,4)),
        Side(Vector2(5, 4), Vector2(5,2)),
        Side(Vector2(1, 2), Vector2(5,2))
    ]),

    Object([
        Side(Vector2(-3, 4), Vector2(-3,6)),
        Side(Vector2(-1, 6), Vector2(-3,6)),
        Side(Vector2(-1, 6), Vector2(-1,4)),
        Side(Vector2(-3, 4), Vector2(-1,4))
    ])
]
camera = Camera(Vector2(0, 0), Angle(0), (Angle(300), Angle(60))) #The distance between the FOV angles must be less than 180 degrees
scalar = Scalar(100, 3.5)
renderer = Render(True)

def renderScreen():

    linesToRender = []
    for i in Objects:
        linesToRender += i.getSidesInFov(camera)
       
    renderer.render(camera, scalar, linesToRender)

def moveCamera(event):

    if(event.char == "j" or event.char == "q"):
        camera.angle -= Angle(15)
    elif(event.char == "l" or event.char == "e"):
        camera.angle += Angle(15)

    if(camera.angle > Angle(269)):
        xangle = Angle(90) + camera.angle
    else:
        xangle = Angle(270) - camera.angle

    if(camera.angle > Angle(359)):
        yangle = camera.angle
    else:
        yangle = Angle(360) - camera.angle
    
    xIncrease = ((xangle.angle / 180) * 2) - 1
    yIncrease = ((yangle.angle / 180) * 2) - 1

    if(event.char == "w"):
        camera.pos += Vector2(xIncrease, -yIncrease)
    elif(event.char == "a"):
        camera.pos += Vector2(yIncrease, xIncrease)
    elif(event.char == "s"):
        camera.pos += Vector2(-xIncrease, yIncrease)
    elif(event.char == "d"):
        camera.pos += Vector2(-yIncrease, -xIncrease)

    renderScreen()


def main():
    root = Tk()
    root.geometry('300x200')
    root.bind('<KeyPress>', moveCamera)
    root.mainloop()


if (__name__ == "__main__"):
    main()