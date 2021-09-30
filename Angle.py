
class Angle():
    def __init__(self, angle):
        self.angle = angle
    
    def __repr__(self):
        return str(self.angle)

    def __add__(self, other):
        return Angle((self.angle + other.angle) % 360)
    
    def __sub__(self, other):
        return Angle((self.angle - other.angle) % 360)
    
    def __mul__(self, other):
        return Angle((self.angle * other.angle) % 360)
    
    def __truediv__(self, other):
        return Angle((self.angle / other.angle) % 360)

    def __gt__(self, other):    #greater than and less work differently: They return true if the angle is between 180 degrees +- the angle. 
                                #ex: 90 > 80, 90 > 360, 359 < 90, but not 359 < 181, or 270 > 0. This makes determining if something is in fov so much easier
        angle = self.angle
        opposite = self - Angle(180)
        opposite = opposite.angle
        
        if(angle - opposite <= 0): 
            return other.angle > opposite or other.angle < angle
        else:
            return other.angle > opposite and other.angle < angle

    
    def __lt__(self, other):
        angle = self.angle
        opposite = self - Angle(180)
        opposite = opposite.angle
        
        if(opposite - angle <= 0):
            return other.angle < opposite or other.angle > angle
        else:
            return other.angle < opposite and other.angle > angle


    def toPosition(self):
        if (self.angle > 180):
            return self.angle - 360
        return self.angle