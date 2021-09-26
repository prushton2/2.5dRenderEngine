from Vector2 import *
from DistanceCalculator import *
from Object import *
from Render import *
from Angle import *

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
camera = Camera(Vector2(0, 0), Angle(0), (Angle(315), Angle(45)))
scalar = Scalar(100, 3.5)
print(DistanceCalculator.getAngleToCamera(camera, Vector2(1,1)))