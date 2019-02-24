import math
#1
class Apple:
    def __init__(self,w,s,c,f):
        self.weight = w
        self.size = s
        self.color = c
        self.freshness = f
#2
class Circle:
    def __init__(self,r):
        self.radius = r

    def area(self):
        return pow(self.radius,2)*math.pi
#3
class Triangle:
    def __init__(self,w,l):
        self.width = w
        self.len = l
    
    def area(self):
        return self.width*self.len/2
#4
class Hexagon:
    def __init__(self,s1,s2,s3,s4,s5,s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

apple1 = Apple(200,10,"red","fresh")
print(apple1.weight)
print(apple1.size)
print(apple1.color)
print(apple1.freshness)

circle1 = Circle(2)
print(circle1.area())

triangle1 = Triangle(4,5)
print(triangle1.area())

hexagon1 = Hexagon(1,2,3,4,3,2)
print(hexagon1.calculate_perimeter())

"""
200
10
red
fresh
12.566370614359172
10.0
15
"""