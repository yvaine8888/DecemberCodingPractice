'''
Problem - Create a program to check if the given string is a palindrome

Need to get rid of captilization, punctuation and empty spaces.

function

make it lower
replace spaces and punctuation with empty from a string with it all

check if the string is equal to it reversed
if so return true else return false
'''

def is_palindrome(s):
    # Making it all lowercase
    s = s.lower() 

    # All the things to replace
    replacing = "''!()-[]{} ;:\"\,<>./?@#$%^&*_~''"

    # Replacing it
    for ele in replacing:
        s = s.replace(ele, "")

    # Checking and returning if it is a palindrome
    if s == s[::-1]:
        return "The string is a palindrome."
    else:
        return "The string is not a palindrome."