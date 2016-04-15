######################################################################
# A flawed change making program
#
# Author: Mario Nakazawa
# username: nakazawam
#
# EDITORs: John Hellrung (Driver) & Vincent Tembo (Navigator)
# Usernsme: hellrungj & tembov
#
# Purpose: This program has a bunch of problems with that need to be
#   fixed. It should be simple enough to be able to trace using the
#   debugger and find out what is wrong.
#   It is supposed to make change. After it asks the user for the
#   amount of money in cents, it outputs the number of quarters, dimes,
#   nickels and pennies needed to make the change.
#
# A SAMPLE RUN OF THIS PROGRAM with 34 CENTS OUTPUTS:
#   You need 1 coins worth 25 cents.
#   You need 0 coins worth 10 cents.
#   You need 1 coins worth 5 cents.
#   You need 4 coins worth 1 cents.
#
# MODIFIED: February 5, 2014
#  - simplified the code by taking out extra things that are not related
#    to the errors.
#  - added comments to explain what this program is doing
#
# MODIFIED: February 8, 2014
# By: John Hellrung (Driver) & Vincent Tembo (Navigtor)
# - Fixed the code and add some impovements
# - now the code runs smoothly and works to commucation better the the user
######################################################################
# Acknowledgements:
# This is original BAD code
######################################################################
import sys
import time

response = 'no'
while response != "yes" or "YES":	# Loop check to stop asking when the user says no

    if response == "no" or response == "No": 	# The user wants to do this again.
        change = int(raw_input("Great! How much money do we have to making change? "))
        print("You Selected ") + str(change) + (" in change.") # tell the user how much change will be inputed.
        time.sleep(1) # wanted the program to feel smoother, when the program was running.

        if( change <= 0 ):
			# Check to make sure that we are putting in a valid number. We cannot make
			# change on a negative number.

            print('Can you put in a positive number?')
        else:
            # Ok, output the number of each coin needed to make change
			# starting with the quarters, dimes, nickels and then pennies
            for coin in [25, 10, 5, 1]:
                if change >= 1: # checks to see if change is less than or equal 1.
                        num_coins = change // coin	# find the number of each type of coin
                        print( 'You need '+ str(num_coins) + ' coins worth ' + str(coin) + ' cents.' ) # We move the print so the code would show the rigth amount of coins, you would need.
                        change = change % coin		# finds out how much is left after taking out
                else: # if change is not great than or equal 1. Then it ends the program.
                    pass
        print("") #print a open line
        response = raw_input("Are we done?") # ask the user for a response.

    elif response == "yes" or response == "Yes":
        print ("Pleased to help you")
        break
    else:
        print ("That won't work. Restart the program")
        response = raw_input("Are we done?")	# Ask the user if he/she wants to quit

