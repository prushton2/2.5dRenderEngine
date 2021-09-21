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

Object([
  Side(Vector2(1, 2), Vector2(1,4)),
  Side(Vector2(5, 4), Vector2(1,4)),
  Side(Vector2(5, 4), Vector2(5,2)),
  Side(Vector2(1, 2), Vector2(5,2))
])

```
This is  a basic cube. You need to define both coordinates of each side. The coordinates are redundant, <br> I plan on making a more abstract polygon instancer

### Field of View
Currently, FOV is defined by 2 things, and is tricky to change. There is the FOV tuple in main.py, which contains 2 slopes. This is the input FOV. If a point is above both slopes, it will be rendered. The output FOV is defined by 2 angles and is located in Render.py. The wider this is, the wider the output screen. This is finnicky, I still need to properly write the FOV in.