# 2.5dRenderEngine
A render engine for 2.5d built in Python.<br>
This uses sides to create objects, and renders them in 2.5 dimensions<br>
### What is 2.5D?
2.5D is a 2 dimensional image rendered in 3 dimensions. Objects all have the same height, and you cannot look up or down.
### How to create objects
An object is made up of sides. The origin of the coordinate grid is the camera.<br>
The Object instance can be made up of an infinite number of sides. A side is a grouping of 2 points.<br>
Grouping multiple sides together can create an object.
Example of an Object:
```python

Polygon([
  Vector2(1, 2),
  Vector2(1, 4),
  Vector2(5, 4),
  Vector2(5, 2)
])

```
This is a basic cube. You define each point in an object, and make sure that the points are supposed to connect to the points necxt to each other in the list


### Changing Camera Settings
In main.py, the camera object is located below the list of objects. These are the parameters:
* Camera Position
* Camera Angle
* Tuple of the two angles that determine FOV

### How to move
* Click on the tkinter window
* Hit any button
* WASD are movement
* J & L or Q & E are look left & right