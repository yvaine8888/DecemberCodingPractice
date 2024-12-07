'''
Problem - Create a program that gets the area based on the shape.

function
get the shape

use if, else if, and else statements to calculate the area

then you return the area (I'm doing it as a string)
Make sure to return an error message if input is wrong like incorrect shape or not a number
'''

def get_area():
    # Asking for the shape to calculate the area
    shape = input("I can calculate the area of a shape for you. Which shape do you want me to calculate the area of? ")
    shape = shape.lower()
    #Calculating the area based on shape
    if shape == "circle":
        radius = input("Please enter the radius: ")
    else if shape == "rectangle":
        length = input("Please enter the length: ")
        width = input("Please enter the width: ")
    else if shape == "square":
        side_length = input("Please enter the side-length: ")
    else if shape == "triangle":
        base = input("Please enter the base: ")
        height = input("Please enter the height: ")
    else:
        return "I'm sorry, but it is an invalid shape. Please check spelling."
