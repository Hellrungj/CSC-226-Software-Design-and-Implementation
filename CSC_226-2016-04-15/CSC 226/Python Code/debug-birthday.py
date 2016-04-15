######################################################################
# A flawed birthday program
#
# Author: Jan Pearce
# username: pearcej
#
# Purpose: This program has flow of control and parameter-passing
#           problems which need to be fixed.
######################################################################
# Acknowledgements:
    # This is original BAD code
######################################################################

def happyBirthday(i, x): # please fix: parameter names should be meaningful!!
    '''Happy birthday function''' #example of useless docstring- please fix!
    for i in range(x):
        print("Happy Birthday to you!")
print("Happy Birthday, dear " + i + ".")
print("Happy Birthday to you!")

happyBirthday('Leslie', 4) # name and number of times to loop

