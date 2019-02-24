#3
class Shape:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def what_am_i(self):
        return "I am a shape"

#1
class Rectangle(Shape):
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width*2 + self.len*2

class Square(Shape):
    def __init__(self,s):
        self.sides = s

    def calculate_perimeter(self):
        return self.sides*4
    #2
    def change_size(self,l):
        if l>0:
            self.sides = self.sides + l
        else:
            if self.sides + l > 0:
                self.sides = self.sides - l
            else:
                self.sides = 1



rect = Rectangle(2,4)
square = Square(5)

print(rect.calculate_perimeter())
print(square.calculate_perimeter())

#2
square.change_size(-6)
print(square.calculate_perimeter())


#3
print(rect.what_am_i())

#4
class Horse:
    def __init__(self,name,rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self,name):
        self.name = name

mick = Rider("Mick")
stan = Horse("Stan",mick)
print(stan.rider.name)

"""
12
20
4
I am a shape
Mick
"""