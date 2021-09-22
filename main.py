from Vector2 import *
from DistanceCalculator import *
from Object import *
from Render import *
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
cameraPos = Vector2(0, 0)
FOV = (-1, 1)

def main():

    root = Tk()
    root.geometry('300x200')
    text = Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
    text.pack()
    root.bind('<KeyPress>', renderScreen)
    root.mainloop()

def renderScreen(event):
    global cameraPos
    print(event.char)

    if(event.char == "w"):
        cameraPos += Vector2(0, 1)
    elif(event.char == "a"):
        cameraPos += Vector2(-1, 0)
    elif(event.char == "s"):
        cameraPos += Vector2(0, -1)
    elif(event.char == "d"):
        cameraPos += Vector2(1, 0)

    linesToRender = []
    for i in Objects:
        linesToRender += (i.getSidesInFOV(FOV))
    
    pointsToRender = []
    for i in linesToRender:
        pointsToRender += i.getAllPoints(500)

    renderPoints = DistanceCalculator.getAllDistances(pointsToRender, cameraPos)


    renderer = Render(renderPoints)
    renderer.render(400)



if (__name__ == "__main__"):
    main()