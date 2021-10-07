#Class to store 2 points. 


class Vector2:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    def toFloat(self):
        self.x = float(self.x)
        self.y = float(self.y)

    def __repr__(self):
        return f"Vector2: {self.x}, {self.y}"

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2(self.x / other.x, self.y / other.y)

