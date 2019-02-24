
#1
class Square():
    square_list = []
    def __init__(self,s):
        self.sides = s
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.sides*4
    
    def change_size(self,l):
        if l>0:
            self.sides = self.sides + l
        else:
            if self.sides + l > 0:
                self.sides = self.sides - l
            else:
                self.sides = 1
            
    def __str__(self):
        return "{} by {} by {}".format(self.sides,self.sides,self.sides)

square1 = Square(5)
square2 = Square(6)
square3 = Square(3)

print(Square.square_list)

#2
print(square1)

#3
def decision(a,b):
    if a is b:
        return True
    else:
        return False

print(decision(square1,square1))
print(decision(square1,square2))

"""
[<__main__.Square object at 0x0000019531A930F0>, <__main__.Square object at 0x0000019531A93128>, <__main__.Square object at 0x0000019531A93160>]
5 by 5 by 5
True
False
"""
