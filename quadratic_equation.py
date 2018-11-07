import math
# we need to import math library in order to use it in our functions


def quadratic_equation(a, b, c):
    '''The function provides the possible solutions for a function of type
    'ax^2 + bx + c' '''
    in_sqrt = (math.pow(b, 2) - 4 * a * c)
    # in_sqrt is a square root of a number, and if that number will be < 0,
    # the function has no solutions
    if in_sqrt < 0:
        x1 = None
        x2 = None
    if a != 0 and in_sqrt > 0:
        x1 = (-b + math.sqrt(in_sqrt)) / (2 * a)
        x2 = (-b - math.sqrt(in_sqrt)) / (2 * a)
    # if in_sqrt == 0, the function has only 1 solution
    elif a != 0 and in_sqrt == 0:
        x1 = -(b / 2 * a)
        x2 = None
    # if a == 0, the function will look like this 'bx - c = 0' and has only
    # 1 possible value
    elif a == 0:
        if b == 0: x1 = None
        else:
            x1 = (-c) / b
        x2 = None
    return x1, x2


def quadratic_equation_user_input():
    '''The function asks the user for 3 numbers, and accordingly match these
     numbers to the function above. Then the function prints out the
     possible solutions'''
    # split by space the input into 3 parameters
    num_a, num_b, num_c = str.split(input("Insert coefficients a, b, and c: "))
    solution_1, solution_2 = quadratic_equation(float(num_a), float(num_b),
                                                float(num_c))
    # now we will provide the 3 possible outcomes and print each accordingly
    #  to the user
    if solution_1 is None:
        print("The equation has no solutions")
    elif solution_2 is None:
        print("The equation has 1 solution: " + str(solution_1))
    else:
        print("The equation has 2 solutions: " + str(solution_1) + " and " +
              str(solution_2))