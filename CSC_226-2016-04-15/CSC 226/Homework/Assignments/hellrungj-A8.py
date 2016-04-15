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
import sys
import time

def test(BittingMoney, TotalM):
    '''Fuction looks at the number of money in the bet and subtracts the amount against the total amount of money the user has on his or her's person'''
    if int(BittingMoney) > int(TotalM):
        print("Sorry, but you have to have ") + str(BittingMoney)+(" in cashs to bet ") + str(BittingMoney) + (".")
        time.sleep(2)
        sys.exit()
    else:
        pass

def gamble(BittingMoney, TotalM, Pick, RC):
    '''Test to see if you win or lose'''
    if str(Pick) == str(RC):
        print("You Win.")
        TotalM = TotalM + BittingMoney
        return TotalM
    else:
        print("You Lose.")
        print("The key was under ") + str(RC) + (".")
        TotalM = TotalM - BittingMoney
        return TotalM

StartingMoney = int(raw_input("Your starting amount.(20, 50, or 100(NO $.))"))
#User picks the starting the amount of cash to start the game.
print("Your starting money is ") + str(StartingMoney) + (".")
TotalM = StartingMoney
if int(StartingMoney) == 100 or int(StartingMoney) == 50 or int(StartingMoney) == 20:
    #if statement for the user starting amount of cash.
    while TotalM >= 1:
        #while statement that loops untill TotalM equals 0.
        BittingMoney = int(raw_input("How much do you want to bet.(Bets must must be 10 dollars or more.(NO $.))"))
        test(BittingMoney, TotalM)
        if BittingMoney >= 1:
            #if statement that more than or equal to 1.
            print("Your bit is ") + str(BittingMoney) + (".")
            RC = random.choice(['shell_1','shell_2','shell_3'])
            #Computer random choics for placing the key.
            Pick = raw_input("Pick shell_1 or shell_2 or shell_3")
            #User pick for the game.
            print("You picked ") + str(Pick) + "."
            TotalM = gamble(BittingMoney,TotalM, Pick, RC)
            print("Your cash is now, ") + str(TotalM) + (".")
        else:
            pass
    else:
        print("Sorry, you have no more money.")
        print("Game over.")
        print("Please, play again.")
else:
    pass