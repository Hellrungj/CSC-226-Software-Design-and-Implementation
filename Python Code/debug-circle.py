######################################################################
# A flawed programwhich uses a funciton to determine the area of a circle

# Author: Jan Pearce
# username: pearcej
#
# Background:
# The area of a circle is the number of square units inside that circle.
# a formula for this area is a = PI * r**2 where PI is an irrational number
# opproximated by PI=3.141592

# Purpose
# To learn to debug programs with flow-of control and parameter passing problems
# There are several problems.
######################################################################
# Acknowledgements:
    # This is original BAD code
######################################################################

r=0 # what is this--why is it here?

def circleArea(i): # please fix: parameter names should be meaningful!!
    '''area docstring for circle''' #example of useless docstring- please fix!
    PI = 3.141592
    i = r
    area = PI * r**2 # this formula is correct
    return area

# This is where the main program starts
raw_input('please enter desired radius: ')
myarea=circleArea(r)
print(myarea)
