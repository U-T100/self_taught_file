#Q1
class Rectangle:
    def __init__(self, len):
        self.len = len

    def calculate_perimeter(self):
        return self.len*4

class Square:
    def __init__(self, len):
        self.len = len

    def calculate_perimeter(self):
        return self.len*4

rectangle = Rectangle(3)
square = Square(9)
print(rectangle.calculate_perimeter())
print(square.calculate_perimeter())

#Q2
class Square:
    def __init__(self, len):
        self.len = len

    def change_size(self, n):
         self.len += n

square = Square(5)
print(square.len)

square.change_size(7)
print(square.len)

square.change_size(-2)
print(square.len)

#Q3
class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, len):
        self.len = len

    def calculate_perimeter(self):
        return self.len*4

class Square(Shape):
    def __init__(self, len):
        self.len = len

    def calculate_perimeter(self):
        return self.len*4

a_rectangle = Rectangle(5)
print(a_rectangle.what_am_i())

a_square = Square(10)
print(a_square.what_am_i())

#Q4
class Horse:
    def __init__(self, name, living, keeper):
        self.name = name
        self.living = living
        self.keeper = keeper

class Rider:
    def __init__(self, name):
        self.name = name

keeper_name = Rider("Jack Hammer")
white_horse = Horse("Nammily", "Japan", keeper_name)
print(white_horse.keeper.name)
