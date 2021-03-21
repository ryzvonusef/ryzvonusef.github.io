import math

class Shapes:
    def __init__(self,sLength,sWidth):
        self.length=sLength
        self.width=sWidth
        
class Triangle(Shapes):
    def shapeArea(self):
        area = (self.length * self.width)*0.5
        print(area)
        
class Rectangle(Shapes):
    def shapeArea(self):
        area = self.length * self.width
        print(area)
        
class Circle(Shapes):
    def shapeArea(self):
        area = self.length * 2 * math.pi
        print(area)

a1=Triangle(3,4)

a1.shapeArea()

a2=Rectangle(3,4)    

a2.shapeArea()

a3=Circle(4,0)

a3.shapeArea()
        
        
        
