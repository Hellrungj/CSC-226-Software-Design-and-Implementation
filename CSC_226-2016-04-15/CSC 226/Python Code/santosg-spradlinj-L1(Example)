#-------------------------------------------------------------------------------
# Name:        santosg-spradlinj-l1.py
# Purpose:     Lab 1
#
# Author:      JT and Ivan
#
# Created:     27/01/2014
# Copyright:   (c) santosg 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
import sys
import time

def calc (ballnum): #function for calculating what the computer chooses (this is set up so the computer always wins)
    if int(ballnum) % 5 is 1:
        cpchoice = 1
        return cpchoice
    if int(ballnum) % 5 is 2:
        cpchoice = 2
        return cpchoice
    if int(ballnum) % 5 is 3:
        cpchoice = 3
        return cpchoice
    if int(ballnum) % 5 is 4:
        cpchoice = 4
        return cpchoice

"""This function loops a starting balls choice until a valid choice is made"""
def start (ballnum):
    balls = int(raw_input('How many balls would you like 15, 20, or 25?'))
    if balls == 15:
        ballnum = 15
        return ballnum
    if balls == 20:
        ballnum = 20
        return ballnum
    if balls == 25:
        ballnum = 25
        return ballnum
    else:
        start(ballnum)

"""This function loops a player choice of balls until a valid choice is made"""
def pturn (playerchoice):
    pballs = int(raw_input('Draw how many 1, 2, 3, or 4?'))
    if pballs == 1:
        playerchoice = 1
        return playerchoice
    if pballs == 2:
        playerchoice = 2
        return playerchoice
    if pballs == 3:
        playerchoice = 3
        return playerchoice
    if pballs == 4:
        playerchoice = 4
        return playerchoice
    else:
        pturn(playerchoice)

ballnum = (0)
ballnum = start(ballnum) #Calls the player to pick how many balls to start with.

for i in range(6): #This keeps the player choosing balls until there are none left.
        playerchoice = (0)
        playerchoice = pturn(playerchoice) #Calls the player to select how many balls to draw.
        ballnum = int(ballnum) - int(playerchoice)
        cpnum = calc(ballnum)
        ballnum = int(ballnum) - int(cpnum)
        print ('Computer takes ' + str(cpnum) + ' balls.')
        print ('There are ' + str(ballnum) + ' balls left.')
        if int(ballnum) == 0: #when there are no balls left, the game ends.
            print ('Game over, you lose! LOSER!')
            time.sleep(15)
            sys.exit()