import math


d = input("What is the diameter of your circle?  ")
area = 0
circumference = 0


def is_digit(d): 
    try:
        float(d)
        return True
    except ValueError:
        return False


def validate_input(d):
    while (True):
        if is_digit(d) is False:
            d = input("Please enter a numerical value: ")
        elif (float(d) < 0):
            d = input("Please enter a value greater than 0: ")
        else:
            return float(d)
            break


d = validate_input(d)


area = math.pi * ((d / 2)*(d/2))
circumference = math.pi * d


roundedArea = round(area, 2)
roundedCircumference = round(circumference, 2)


print('The area of your circle is ', roundedArea)
print('The circumference of your cirlce is', roundedCircumference)
print('Thank you for using this program')
