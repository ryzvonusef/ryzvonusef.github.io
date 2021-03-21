from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        print("i'm inside square function")
        arsqr= self.length**2
        print(arsqr)

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        print("I'm inside circle function")
        arcircle=3.14*self.radius**2
        print(arcircle)

a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
a.area()
b.area()
