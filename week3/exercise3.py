"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    checkLower = False
    checkUpper = False

    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    while checkLower == False:
      lowerBound = input("Enter a lower bound: ")
      try:
        int(lowerBound)
        checkLower = True
      except ValueError: 
          print("Enter a Number this time! ")
      except TypeError:
          print("Enter a Number this time! ")
      if isinstance(lowerBound, str) == True:
        checkLower = False
      
    while checkUpper == False:
      upperBound = input("Enter an upper bound: ")
      try:
        int(upperBound)
        checkUpper = True
      except ValueError: 
          print("Enter a Number this time! ")
      except TypeError:
          print("Enter a Number this time! ")
      if upperBound == lowerBound:
        print("The two numbers must be different!")
        checkUpper = False
      if isinstance(upperBound, str) == True:
        checkUpper = False
    
    print("OK then, a number between " + str(lowerBound) + " and " + str(upperBound) + "!")
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = 0

    if lowerBound < upperBound:
      actualNumber = random.randint(lowerBound, upperBound)
    if upperBound < lowerBound:
      actualNumber = random.randint(upperBound, lowerBound)

    guessed = False
    checkGuess = False

    while not guessed:
        guessedNumber = input("Guess a number: ")
        try:
          int(guessedNumber)
          checkGuess = True
        except ValueError:
          guessedNumber = input("A number this time!")
        except TypeError:
          guessedNumber = input("A number this time!")
        print("You guessed {},".format(guessedNumber),)
        if int(guessedNumber) == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"

   
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
