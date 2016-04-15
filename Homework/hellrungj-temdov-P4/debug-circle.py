######################################################################
# This was initially a flawed program which uses a funciton to determine the area of a circle

# Authors: Vincent Tembo (driver) & John Hellrung (Navigator)
# usernames: tembov & hellrungj
#
# Background (Taken from the original code by Dr. Jan Pearce):
# The area of a circle is the number of square units inside that circle.
# a formula for this area is a = PI * r**2 where PI is an irrational number
# opproximated by PI=3.141592

# Purpose
# To learn to debug programs with flow-of control and parameter passing problems
# There are several problems.
######################################################################
# Acknowledgements:
# Original bad code by Dr. Jan Pearce
######################################################################
# We removed r = 0 because it was not adding anything to the code

def circleArea(i): # please fix: parameter names should be meaningful!!
    '''area docstring for circle''' #example of useless docstring- please fix!
    PI = 3.141592
    i = r
    area = PI * r**2 # this formula is correct
    return area

# This is where the main program starts
r = int(raw_input('please enter desired radius: ')) # First we set r to raw_input then we changed raw_input to an integer
myarea=circleArea(r)
print("The area is: ") + str(myarea) # The string "The area is: " was added to make the output more meaningful
