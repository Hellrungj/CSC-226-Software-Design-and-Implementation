#-------------------------------------------------------------------------------
# Name:        John Hellrung
# Purpose:     To make a Shell Game
#
# Author:      hellrungj
#
# Created:     07/02/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

def gamble(A):
    '''Fuction looks at the number of money in the bet and subtracts the amount against the total amount of money the user has on his or her's person'''
    if gamble <= 0:
        print("No way, get money, you bum!")
    else:
        TotalG = gamble - StartingMoney
        return TotalG

StartingMoney = raw_input("Your starting bet.(20, 50, or 100(NO $.))")
if int(StartingMoney) >= 100 or int(StartingMoney) >= 50 or int(StartingMoney) >= 20:
    BittingMoney = raw_input("How much do you want to bet.(Bets must must be 10 dollars or more.(NO $.))")
    if BittingMoney >= 10:
        TotalM = gamble
        TotalMoney = gamble(BittingMoney)

        RC = random.choice(['shell_1','shell_2','shell_3'])
        Pick = raw_input("Pick shell_1 or shell_2 or shell_3")
        print("You picked ") + str(Pick) + "."
        if str(Pick) == str(RC):
            print("You Win.")
        else:
            print("You Lose.")
            print("The key was under ") + str(RC) + (".")
    else:
        pass
else:
    pass

