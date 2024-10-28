"""
Ultimate Number Guess
----------------------
Created by: John Fiore
Created on: 10/28/2024
----------------------
ATTENTION PROGRAMMERS:

This code probably looks like it sucks.
Thankfully, there is a reason for it.
More info can be found in the GitHub
repo's README.

Thanks,
John Fiore
"""

import random as r
import sys

difficulty = 0 # 0 by default

def init():
    print("Welcome to <ULTIMATE NUMBER GUESS>.")
    difch = int(input("Choose a Difficulty Level (1 = Easy, 2 = Medium, 3 = Hard, 4 = Insane): "))
    if difch >= 5:
        print("Can't go higher than 4!")
        sys.exit()
    
    game(difch)

def game(difLvl):
    print("Playing on Difficulty Level: " + str(difLvl))

    while True:
        try:
            if difLvl == 1: # Easy Mode
                number = r.randint(1, 10)
                max_attempts = None
                print("I am thinking of a number between 1-10...")
            elif difLvl == 2:
                number = r.randint(1, 50)
                max_attempts = 10
                print("I am thinking of a number between 1-50...")
            elif difLvl == 3:
                number = r.randint(1, 100)
                max_attempts = 5
                print("I am thinking of a number between 1-100...")
            elif difLvl == 4:
                number = r.randint(1, 100)
                max_attempts = 2
                print("I am thinking of a number between 1-1000...")
            else:
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    attempts = 0

    while True:
        try:
            guess = int(input("What is your guess?: "))
            attempts += 1

            if guess < number:
                print("Too Low! Try again.")
            elif guess > number:
                print("Too High! Try again.")
            else:
                print("Congrats! You guess correctly in " + str(attempts) + " attempts.")
                break

            if max_attempts and attempts >= max_attempts:
                print("Out of attempts! The number was " + str(number) + "..")
                break

        except ValueError:
            print("Please enter a valid integer.")
    
    pag = input("Wanna play again? (y/n): ")
    if pag == "y":
        init()
    else:
        print("Thanks for playing!!")
        
init()
