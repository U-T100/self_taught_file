#Q!
class Apple:
    def __init__(self,c,t,w,h):
        self.color = c
        self.taste = t
        self.weight = w
        self.hardness = h

#Q2
import math

class Circle:
    def __init__(self,r):
        self.radius = r

    def area(self):
        return self.radius**2*math.pi

circle = Circle(7)
print(circle.area())

#Q3
class Triangle:
    def __init__(self,bottom,height):
        self.height = height
        self.bottom = bottom

    def area(self):
        return self.height*self.bottom*0.5

triangle = Triangle(8,6)
print(triangle.area())

#Q4
class Hexagon:
    def __init__(self,length):
        self.length = length

    def calculate_perimeter(self):
        return self.length*6

hexagon = Hexagon(3)
print(hexagon.calculate_perimeter())
