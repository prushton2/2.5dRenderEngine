from Vector2 import *
from DistanceCalculator import *
from Object import *
from Render import *

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

FOV = (-1, 1)

def main():
    pass
    linesToRender = []
    for i in Objects:
        linesToRender += (i.getSidesInFOV(FOV))
    
    pointsToRender = []
    for i in linesToRender:
        pointsToRender += i.getAllPoints(100)

    renderPoints = DistanceCalculator.getAllDistances(pointsToRender)


    renderer = Render(renderPoints)
    renderer.render(400)



if (__name__ == "__main__"):
    main()