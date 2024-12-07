'''
Problem - Create a function that determines if all characters in a string are unique.

function

use a for loop through the string to check if it occurs more than once.
that means another for loop.
if it does return false
Note: I consider spaces to be a character so it will return false if there are multiple spaces.
I also consider captilization to be different letters and empty strings to be unique.
'''

def is_unique(s):
    # Going through each element to see if there is more than one of it
    for ele in s:
        count = 0
        #Checking it
        for char in s:
            if ele == char:
                count = count + 1
        # Returning false if more than one count
        if count > 1:
            return False
    # Returning true if okay
    return True
