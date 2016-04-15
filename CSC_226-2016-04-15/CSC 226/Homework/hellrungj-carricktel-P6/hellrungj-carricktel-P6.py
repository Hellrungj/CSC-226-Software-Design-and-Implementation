######################################################################
# Author: John Hellrung & Joseph Carrick
# usernames: hellrungj & carricktel
#
# Purpose: Highlight the use of doctest when try to design and debug
#   code, and for unit testing using a testit() function.
#
# Modified: Created add_rand() function
#           Inserted testit() function for the text
#           Created is_equal() function, encapsulating Boolean test
#           Added doctest for is_equal() function
######################################################################
# Acknowledgements
# based on buggy.py
# From: http://inventwithpython.com/chapter7.html
# fixed this broken code based on Dr, Jan Perice & Dr. Mario Nakawaza orgianl broken code
######################################################################

import random
import sys

def testit(did_pass):
    """ Print the result of a test. """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

# We use doctest here to check for the expected output of this function.
# note that we included both expected cases (the function is supposed to return
# true when the sum of the first two parameters is the same as the third
# parameter, and false otherwise).
def is_equal(number1, number2, answer): #Changed the parameter to answer so the that is_equal calls the right vaible.
    """ Returns true of the sum of the first two parameters is equal to the third.
    >>> is_equal(3, 4, 7)
    True
    >>> is_equal(3, 4, 8)
    False
    """
    if number1 + number2 == answer: #Changed the sum_check to answer.
        return True
    else:
        return False

def add_rand(number1, number2):
    '''ask the user for a number, and output Correct! if the response is equal
        to those two numbers added together, and "Nope!..." otherwise.'''
    answer = int(raw_input('What is ' + str(number1) + ' + ' + str(number2) + '?'))
    if is_equal( number1, number2, answer) == True: #set the if statement to if is_equal to True
        print('Correct!')
        return True
    else:
        print('Nope! The answer is ' + str(number1 + number2))
        return False

#main program begins here
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)

# The following two lines will "test" the is_equal() function using doctest
import doctest
doctest.testmod()   # check to see if the doctest in the is_equal function works

testit(add_rand(number1,number2)) # Here is the call to run the main test