######################################################################
# A flawed change making program
#
# Author: Mario Nakazawa
# username: nakazawam
#
# Purpose: This program has a bunch of problems with that need to be
#   fixed. It should be simple enough to be able to trace using the
#   debugger and find out what is wrong.
######################################################################
# Acknowledgements:
# This is original BAD code
######################################################################
import sys

print("Welcome to the change maker!")
response = "no"
count = 0
while response != "yes" or "YES":
    if response == "no" or response == "No":
        print("Great.")

        change = int(raw_input("How much money are we making change? "))
        output = ""

        if change <= 0:
            print("Can you put in a positive number?")
        else:
            # Ok, create an output string that lists out the number of each coin
            for coin in [1, 5, 10, 25]:
                num_coins = change // coin
                change = change % coin

            output = output + str(coin) + ": " + str(num_coins)
            print (output)
    elif response == "maybe":
        print("Please decide something!")
    else:
        pass
    count = count + 1
    print("We went through the loop "+str(count)+" times.")
    response = raw_input("Are we done?")
else:
    sys.exit