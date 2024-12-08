'''
Problem - Create a program to play a number guessing game.

get a random 1-100

create a while loop that keeps on asking the user for a number 1-100
inside the loop
if not a number say so then continue

if correct, break
if more than 100 or less than 1, tell so
if greater, tell smaller
if smaller, tell greater
'''
import random
# Getting the correct number
num = random.randint(1, 100)

# The while loop that allows the user to guess and prints when the input is incorrect or correct.
while True:
    print()
    # The user's guess
    guess = input("Please guess a number 1-100: ")
    # Printing error if the input is not a number else make it an integer
    try:
        guess = int(guess)
    except:
        print("Please guess a valid number next time.")
        continue
    
    # Tell if the number is corect or incorrect and print messages based on that.
    if guess == num:
        print("Congratulations! You guessed the right number.")
        break
    elif guess > 100 or guess < 1:
        print("Please guess a number 1-100 next time.")
    elif guess > num:
        print("Your guess is too high. Try a smaller number.")
    else:
        print("Your guess is too low. Try a larger number.")
