import math
# we need to import math library in order to use it in our functions


def shape_area():
    '''The function let the user choose a specific shape out of 3, and then
    helps him to calculate the shape area -
    for a circle radius length is needed
    for a rectangle 2 sides lengths are needed
    for a trapezoid 2 bases and height lengths are needed'''
    shape = input("Choose shape (1=circle, 2=rectangle, 3= trapezoid)")
    if shape == '1':
        radius = input()
        return math.pi * float(radius) **2
    if shape == '2':
        side1 = input()
        side2 = input()
        return float(side1)*float(side2)
    if shape == '3':
        base1=input()
        base2=input()
        height=input()
        return (float(base1) + float(base2)) * float(height) / 2
    else:
        return None