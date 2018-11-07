def largest_and_smallest(num1, num2, num3):
    '''The function provides for every 3 numbers max_val & min_value'''
    # if num1 is bigger or equal to the other 2 he will be defined as Max
    if num1 >= num2 and num1 >= num3:
        max_val = num1
        # if num1 is max we have no need to check if its Min
        if num2 <= num3:
            min_val = num2
        else:
            min_val = num3
    # now we will check only between nums 2&3, cause we checked before and
    # it isnt num1
    elif num2 >= num3:
        max_val = num2
        if num3 <= num1:
            min_val = num3
        # if num2 is Max and num3 isn't Min, it must be num1
        else:
            min_val = num1
    else:
        max_val = num3
        if num2<= num1:
            min_val = num2
        else:
            min_val = num1
    return max_val, min_val