######################################################################
# Authors: Alrick Green & John Lowder
# username: Greenal & lowderj
# Rolls:Alrick Green-Navigator and Part Driver John Lowder-Driver and Part Navigator
# Assignment: L1
# Purpose: Practice breaking a larger problem down into smaller "pieces"using functions
# and Gain practice using loops and modulus (%)
######################################################################
# Acknowledgements: John Hellrung help to assist me with debugging our program so it could work effiecintly.
#
#
#
######################################################################
import sys
import math
import random

def computer_pick(NumberOfBalls):
    """Logic that decides what choices the computer will make"""
    if (NumberOfBalls%5) == 0:
        computer_guess=random.choice([1,2,3,4])
        return(computer_guess)
    elif (NumberOfBalls%5) == 1:
        return(1)
    elif(NumberOfBalls%5) == 2:
        return(2)
    elif(NumberOfBalls%5) == 3:
        return(3)
    elif(NumberOfBalls%5) == 4:
        return(4)

greetings = raw_input("Do you want to play a game?")
if greetings == 'yes' or greetings == 'Yes':
    print("Great! let's play")
    NumberOfBalls= int(raw_input('Please pick a number greater than 14 and less than 41'))
    if NumberOfBalls >= 15 and NumberOfBalls <= 40:
        while NumberOfBalls != 0:
            PickBalls = raw_input('How many balls do you want to take away?')
            print('You picked ') + str(PickBalls) + (" balls.")
            NumberOfBalls=int(NumberOfBalls) - int(PickBalls)
            print("the remaining balls are equal to ") + str(NumberOfBalls)
            if NumberOfBalls == 0:
                print("Human winner")
            else:
                sys.exit
            ComputerP=int(computer_pick(NumberOfBalls))
            print("computer picked ") + str(ComputerP) + (" balls")
            NumberOfBalls=int(NumberOfBalls)-int(ComputerP)
            print("the remaining balls are equal to ") + str(NumberOfBalls)
            if NumberOfBalls == 0:
                print("Computer winner")
            else:
                sys.exit
    else:
        print("Goodbye, Maybe next time")
else:
    sys.exit