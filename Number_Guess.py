# a very simple number guessing game
from random import randint
lower, upper, guess = int(input("Input lower value ")), int(input("Input upper value ")), True
number = randint(lower, upper)
while guess:
    guessnumber = int(input("input your guess "))
    if number == guessnumber:
        print("Correct!")
        guess = False
    elif guessnumber < number:
        print("You guessed too low")
    elif guessnumber > number:
        print("You guessed too high")
