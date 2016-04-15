######################################################################
# This used to be a flawed birthday program
#
# Authors: Vincent Tembo (driver) and John Hellrung (navigator)
# usernames: tembov & hellrungj
#
# Purpose(taken from original program by Dr. Jan Pearce): This program has flow of control and parameter-passing
#           problems which need to be fixed.
######################################################################
# Acknowledgements:
# Dr. Jan Pearce for the original bad code
######################################################################

def happyBirthday(l, x): # The parameter l was changed from i to prevent confusion with the local variable i
    '''This function loops through print statements several times to simulate singing happy birthday''' #This docstring was corrected to make it more useful to a future user of the program
    for i in range(x):
        print("Happy Birthday to you!")
    #The two print functions below were indented because they were running under the function definition instead of the for loop
    print("Happy Birthday, dear " + l + ".") # The i was changed to an l because i was the local variable with a value of 3 but l is the argument of the call
    print("Happy Birthday to you!")

happyBirthday('Leslie', 4) # name and number of times to loop

