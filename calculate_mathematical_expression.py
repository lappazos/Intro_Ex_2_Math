def calculate_mathematical_expression(num1,num2,requested_operator):
    '''The function performs a mathematical operation according to 2 numbers
    and an operator (+, -, *, /) defined in the function params'''
    if requested_operator == '+':
        return num1 + num2
    if requested_operator == '*':
        return num1 * num2
    if requested_operator == '-':
        return num1 - num2
    if requested_operator == '/':
        # if the number divided by is 0 we cant perform a correct devision
        if num2 == 0:
            return None
        return num1 / num2
    return None


def calculate_from_string(text):
    '''The function receive text message ,applies on it the
    calculate_mathematical_expression function and returns specific value '''
    # now we will split the text into the 3 relevant parameters we need
    part1_text, part2_text, part3_text = str.split(text, " ")
    return calculate_mathematical_expression(float(part1_text),
                                             float(part3_text),part2_text)