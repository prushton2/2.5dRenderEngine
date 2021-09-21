from Vector2 import *
from DistanceCalculator import *
from Object import *
from Render import *

Objects = [
    Object(Vector2(3, 3), [
        Side(Vector2(1, 2), Vector2(1,4)),
        Side(Vector2(5, 4), Vector2(1,4)),
        Side(Vector2(5, 4), Vector2(5,2)),
        Side(Vector2(1, 2), Vector2(5,2))
    ]),

    Object(Vector2(0, 5), [
        Side(Vector2(-1, 4), Vector2(-1,6)),
        Side(Vector2(1, 6), Vector2(-1,6)),
        Side(Vector2(1, 6), Vector2(-1,6)),
        Side(Vector2(-1, 4), Vector2(-1,6))
    ])
]

FOV = (-1, 1)

def main():
    pass
    linesToRender = []
    for i in Objects:
        linesToRender += (i.getSidesInFOV(FOV))
    # print(linesToRender)
    
    pointsToRender = []
    for i in linesToRender:
        pointsToRender += i.getAllPoints(10)
    # print("----------------------")
    # print(pointsToRender)

    renderPoints = DistanceCalculator.getAllDistances(pointsToRender)

    # print("-----------------------")
    # print(renderPoints)

    renderer = Render(renderPoints)
    renderer.render()



if (__name__ == "__main__"):
    main()