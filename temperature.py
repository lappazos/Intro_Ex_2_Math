def is_it_summer_yet(temp_wanted, temp_day_1, temp_day_2, temp_day_3):
    '''The function receives a desired temperature and 3 current
    temperatures n 3 different days, and determine whether or not the total
    temperature fits travelling'''
    day_1 = False
    day_2 = False
    day_3 = False
    if temp_day_1 > temp_wanted:
        day_1 = True
    if temp_day_2 > temp_wanted:
        day_2 = True
    if temp_day_3 > temp_wanted:
        day_3 = True
    # here we count the amount of days we do have the desired temp, and if
    # this number is 2 and above well approve the travel
    if (day_1 + day_2 + day_3) > 1:
        return True
    else: return False
