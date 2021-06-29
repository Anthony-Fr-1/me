"""Set 3, Exercise 3.

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

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nWelcome to the guessing game!")
    print("A number between 0 and _ ?")
    correctanswer = False
    while correctanswer == False:
        try:
            upperBound = int(input("enter upper bound\n"))
            correctanswer = True
        except:
            print("input must be integer\n")
    print("OK then, a number between 0 and {} ?".format(upperBound))
    print("A number between _ and {} ?".format(upperBound))
    correctanswer = False
    while correctanswer == False:
        try:
            lowerBound = int(input("enter lower bound\n"))
            correctanswer = True
        except:
            print("input must be integer")
    print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))
    C = int(upperBound)

    if lowerBound > upperBound:
        temp = lowerBound
        lowerBound = upperBound
        upperBound = temp

    actualNumber = random.randint(0, upperBound)

    guessed = False

    while not guessed:
        correctanswer = False
        while correctanswer == False:
            try:
                guessedNumber = int(input("enter guess\n"))
                correctanswer = True
            except:
                print("input must be integer\n")
        print(
            "You guessed {},".format(guessedNumber),
        )
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"


# checking to see if number is within the range
# try:
# if upperBound in random.randint(0, upperBound):
# except:
# print("The number is outside range.")
# checking if guessed number is an integer
# try:
# guessedNumber == int:
# except:
# print("try again: number must be an integer")


if __name__ == "__main__":
    exampleGuessingGame()
