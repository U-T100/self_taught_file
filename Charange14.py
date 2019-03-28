#Q1
class Square:
    square_list = []

    def __init__(self, len):
        self.len = len
        self.square_list.append(self.len)

s1 = Square(14)
s2 = Square(46)

print(Square.square_list)

#Q2
class Square:
    square_list = []

    def __init__(self, len):
        self.len = len
        self.square_list.append(self.len)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.len, self.len, self.len, self.len)

square = Square(10)
print(square)

#Q3
def para(obj1,obj2):
    return obj1 is obj2

print(para("s", "s"))
