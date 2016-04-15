#-------------------------------------------------------------------------------
# Name:     p8.broken_code.py
# Purpose:
#   This program is designed for reflection on modularity, scope, and side-effects.
#   This file contains a few functions that are broken to some extent,
#   and a main section that has quite a number of unit tests for each of these
#   functions. This program highlights some of the common errors that can happen
#   when implementing functions without attention to minimizing side effects
#   by using parameters and return values as intended.
#
# Author:      nakazawam and pearcej
#
# Created:     06/03/2014
# Copyright:   (c) nakazawam and pearcej 2014
#-------------------------------------------------------------------------------
#   Aknowledgement: Except for testit(), this is original code.
#-------------------------------------------------------------------------------

import sys      # needed for the testit function
import random

def testit(did_pass):
    """ Print the result of a test. """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def get_max_number( number_list ):
    ''' given a list of numbers in the parameter number_list input, it finds
    the largest one and returns it.'''

    max_number = number_list[0]
    for i in number_list:
        if i > max_number:
            max_number = i
    return max_number

def find_max_number( number_list ):
    ''' given a list of numbers in the parameter number_list input, it finds
    the largest one and outputs it to the screen.'''

    max_number = number_list[0]
    for i in number_list:
        if i > max_number:
            max_number = i
    print( max_number )

def rotate_flag( input_flag ):
    ''' Rotate the flag colours; if input is "red", "white", "green" --> "white", "green", "red"
                                 if input is "white", "green", "red" --> "green", "red", "white"
                                 if input is "green", "red", "white" --> "red", "white", "green" '''
    global my_flag
    (first_c, second_c, third_c) = input_flag
    my_flag = (second_c, third_c, first_c)
    return my_flag

def make_older( input_person ):
    ''' Unpacks the first name, last name, and age of the person stored in the
        parameter input_person, increments the age, updates the new older person's
        information in the "person" variable defined in the main part of
        the program, and returns the new age. '''
    (fname, lname, age) = input_person  # unpack the tuple to get the age
    age = age + 1                       # make the age older
    person = (fname, lname, age)        # save the older person's information in person
    return age

#-------------------------------------------------------------------
#   The main part of the program, which has the unit tests for the
#   functions defined above.
#-------------------------------------------------------------------
# UNIT TEST BATTERY

# test out the get_max_number function
print("get_max_number() tests:")
testit( get_max_number([34, 23, 1]) == 34)
testit( get_max_number([12, 23, 67]) == 67)

# Set this variable to hold my flag's colours
my_flag = ("red", "white","green")

# test out the rotate_flag() function that rotates the colours

# this function call with the same variable should return the same values no matter
# how many times it is called
print("\nrotate_flag() tests:")
testit( rotate_flag(my_flag) == ("white", "green", "red"))
testit( rotate_flag(my_flag) == ("white", "green", "red"))
testit( rotate_flag(("green", "red","white")) == ("red","white", "green"))
testit( rotate_flag(my_flag) == ("white", "green", "red"))

# test out the make_older function
print("\nmake_older() tests:")

# Set this variable to hold Danielle's information
person = ("Danielle","Smith", 34)
testit( make_older( person ) == 35 )           # person was updated in make_older, so Danielle is a year older (35)
testit( make_older( person ) == 36 )           # person was updated in make_older, so Danielle is a year older (36)

# person should have Jack's information now, and Jack is a year older (12 -> 13)
testit( make_older( ("Jack", "Stevens", 12) ) == 13 )
testit( make_older( person ) == 14 )            # Jack should be a year older
