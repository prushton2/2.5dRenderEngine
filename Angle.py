
class Angle():
    def __init__(self, angle):
        self.angle = angle
    
    def __repr__(self):
        return str(self.angle)

    def __add__(self, other):
        return (self.angle + other.angle) % 360
    
    def __sub__(self, other):
        return (self.angle - other.angle) % 360
    
    def __mul__(self, other):
        return (self.angle * other.angle) % 360
    
    def __truediv__(self, other):
        return (self.angle / other.angle) % 360

    def toPosition(self):
        if (self.angle > 180):
            return self.angle - 360
        return self.angle