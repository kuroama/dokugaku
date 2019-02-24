
a = 3
#1

def squared(x):
    """
    Squared x.
    :param x: int.
    :return: int squared x.
    """
    return pow(x,2)

print(squared(a))

#2
def print_str(str):
    """
    Print string.
    :param str: string.
    """
    print(str)

print_str("Hello")

#3
def print_num(a,b,c,d=3,e=7):
    """
    Print number.
    :param a:int.
    :param b:int.
    :param c:int.
    :param d:int.
    :param e:int.
    """
    print(str(a)+":"+str(b)+":"+str(c)+":"+str(d)+":"+str(e))

print_num(1,2,3,4)

#4
def divide2(x):
    """
    x divided by 2.
    :param x:2.
    :return:int x divided by 2 is?
    """
    return int(x/2)

def multi4(x):
    """
    x multiplied by 4.
    :param x:int.
    :return x:int multiplied by 4 is?
    """
    return x*4

b=divide2(9)
print(multi4(b))

#5
def str_to_float(str):
    """
    String converts float.
    :param str:string.
    :return:float number after converts from string
    """
    try:
        return float(str)
    except ValueError:
        print("Invalid input") 

print(str_to_float("7"))
str_to_float("#")

"""
9
Hello
1:2:3:4:7
16
7.0
Invalid input
"""

