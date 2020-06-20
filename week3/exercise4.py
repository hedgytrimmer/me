# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time
import random


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    tries = 0
    guess = 0
    while True:
        guess = high - math.floor((high-low)/2)
        print("guess: " + str(guess))
        print("high: " + str(high))
        print("low: " + str(low))
        if guess > actual_number:
            high = guess - 1
        elif guess < actual_number:
            low = guess + 1
        elif guess == actual_number:
            break
        tries += 1

    return {"guess": guess, "tries": tries}
""" TESTING
def binary_search2(low, high, actual_number):
    tries = 0
    guess = 0
    while guess != actual_number:
        guess = high - math.floor((high-low)/2)
        print("guess: " + str(guess))
        print("high: " + str(high))
        print("low: " + str(low))
        tries += 1
        if guess > actual_number:
            high = guess - 1
        elif guess < actual_number:
            low = guess + 1



    return {"guess": guess, "tries": tries}"""

if __name__ == "__main__":
    print(binary_search(1, 3, 1))
    print(binary_search(1, 100, 5))
    #print(binary_search(1, 100, 95))
    #print(binary_search(1, 51, 5))
    #print(binary_search(1, 50, 5))
