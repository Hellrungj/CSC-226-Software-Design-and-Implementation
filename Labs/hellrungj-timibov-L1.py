#-------------------------------------------------------------------------------
# Name:        John Hellrung and Vincent Timibo
# Purpose:     To make a game of Nim for CSC 226
#
# Author:      hellrungj & timibov
#
# Created:     31/01/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Acknowledgements:
#Alrick Green & Jan Pearce & Mario Nakazawa
#turtle.interactive.py
#By:
#Jan Pearce & Mario Nakazawa
#santosg-spradlnj-L1.py
#By:
#Gerardo Ivan Santos & JT
#Tester:
#Travon, Chris, Bradon.
#-------------------------------------------------------------------------------
import time
import random
import sys
import math  #Importing the imports I need

def Computer():
    if int()% 5 == 1:
        return(1)
    elif int()%5 == 2:
        return(2)
    elif int()%5 == 3:
        return(3)
    elif int()%5 == 4:
        return(4)
    else:
        return random.choice([1,2,3,4])

HI = str(raw_input("Name please! "))
V = 0
NumberOfBalls=40
while NumberOfBalls != (int(NumberOfBalls) <= 40 and int(NumberOfBalls) >= 15):
    NumberOfBalls = raw_input("Pick the number of Balls(15-40) ")
    if int(NumberOfBalls) <= 40 and int(NumberOfBalls) >= 15:#If statement for testing user input is true
        print HI + (", you selected ") + str(NumberOfBalls) + (" balls.")#If Statement for Number of Balls
        print ("You have the first turn.")#Player1 Turn
        RemaningBalls = NumberOfBalls
        while RemaningBalls != 0:#While statement is for a loop so that the program will loop untill it reach less than or equal to zero

            Player1 = raw_input("Take 1-4 Balls ")
            if int(Player1) <= 4 and int(Player1) >= 1:#If statement for testing user input is true
                RemaningBalls = int(RemaningBalls) - int(Player1)#Subtracts the total remaining balls by the player1 input
                print ("You takes ") + str(Player1) + (" balls")#Tells the user how many they have taking
                print('')
                time.sleep(1.0)
                if int(RemaningBalls) <= 0:#If statement for find if the player1 wins
                    if V >= 3:
                        print ("You lose because you were trying to cheat more than 3 times.")
                        time.sleep(3)
                        sys.exit()
                    else:
                        print HI + (" is the winner!")
                        time.sleep(3)
                        sys.exit()
                else:
                    print ("There are ") + str(RemaningBalls) + (" balls left")#Tells the user how many are left
#Computer Turn
                if int(RemaningBalls) == 1 or int(RemaningBalls) == 2 or int(RemaningBalls) == 3 or int(RemaningBalls) == 4 or int(RemaningBalls) == 6:
                    if int(RemaningBalls) == 1:
                        ComputerBalls = 1
                    elif int(RemaningBalls) == 2:
                        ComputerBalls = 2
                    elif int(RemaningBalls) == 3:
                        ComputerBalls = 3
                    elif int(RemaningBalls) == 4:
                        ComputerBalls = 4
                    elif int(RemaningBalls) == 6:
                        ComputerBalls = 1
                else:
                    ComputerBalls = int(Computer())#Setting up a varaibe for my funtion
                RemaningBalls = int(RemaningBalls) - int(ComputerBalls)#Subtracts the total remaining balls by the computers choice input
                print ("Computer takes ") + str(ComputerBalls) + (" balls")#Tells the user many the computer is taking
                if int(RemaningBalls) == 0:#If statement for find if the computer wins
                    if V >= 3:
                        print ("You lose cheater!")
                        time.sleep(3)
                        sys.exit()
                    else:
                        print ("Sorry. ") + HI + (" you lose, the computer is the winner!")
                        time.sleep(3)
                        sys.exit()
                else:
                    print ("There are ") + str(RemaningBalls) + (" balls left.")#Tells the user how many left
                    print('')
                    time.sleep(1)
                    pass
            else:
                print HI + (", stop cheating!")
                V = V + 1
                time.sleep(1)
                sys.exit
        else:
            time.sleep(2)
    else:
        print ("Sorry, I asked you to choice from 15-40, and you didn't. So, please try again.")
        time.sleep(1)
else:
    pass