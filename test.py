from Vector2 import *
from DistanceCalculator import *
from Object import *
from Render import *


camera = Camera(Vector2(0, 0), 0, (-45, 45))
print(DistanceCalculator.getDistanceToCamera(Vector2(-1, 1), camera.pos))