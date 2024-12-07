'''
Problem - Create a program that gets the area based on the shape.

function
get the shape

use if, elif, and else statements to calculate the area

then you return the area (I'm doing it as a string)
Make sure to return an error message if input is wrong like incorrect shape or not a number
'''

def get_area():
    # Asking for the shape to calculate the area
    shape = input("I can calculate the area of a shape for you. Which shape do you want me to calculate the area of? ")
    shape = shape.lower()
    
    #Calculating the area based on shape and return error messages.
    area = 0
    if shape == "circle":
        radius = input("Please enter the radius: ")
        if is_not_num(radius):
            return "I'm sorry, but this is not valid."
        radius = float(radius)
        area = radius*radius*3.14
    elif shape == "rectangle":
        length = input("Please enter the length: ")
        if is_not_num(length):
            return "I'm sorry, but this is not valid."
        width = input("Please enter the width: ")
        if is_not_num(width):
            return "I'm sorry, but this is not valid."
        length = float(length)
        width = float(width)
        area = length * width
    elif shape == "square":
        side_length = input("Please enter the side-length: ")
        if is_not_num(side_length):
            return "I'm sorry, but this is not valid."
        area = side_length * side_length
    elif shape == "triangle":
        base = input("Please enter the base: ")
        if is_not_num(base):
            return "I'm sorry, but this is not valid."
        height = input("Please enter the height: ")
        if is_not_num(height):
            return "I'm sorry, but this is not valid."
        base = float(base)
        height = float(height)
        area = base * height / 2
    else:
        return "I'm sorry, but it is an invalid shape. Please check spelling."

    # Returning the area as a string.
    return f"The area of a {shape} is {area}."

def is_not_num(str):
    try:
        str = float(str)
        return False
    except:
        return True
