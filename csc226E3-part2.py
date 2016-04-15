#-------------------------------------------------------------------------------
# Name:       csc226E3-part2.py
# Purpose: A program that implements the automobile class, which has one
#   state variable, gear_state
#
# Created:     Apr/16/2014
# ------------------------------------------------------------------------------
# Exam E3 Part 2
# Instructions:
#   (9 points)
#   Implement the two functions shift_up() and shift_down(), which change the
#   state of the Automobile so that its gear_state goes up and down by one,
#   respectively. Make sure you prevent cases such as when you try to shift-up
#   beyond its max gear or shift down below its minimum.
#   NOTHING SHOULD BE OUTPUT TO THE SCREEN!
#   Make sure to insert appropriate docstrings and comments, they are worth points.
#
#   (6 points)
#   Complete the function test_Automobile_class() that creates an Automobile
#   object and tests whether the methods you implemented in part 1 work. Make sure
#   you test for cases such as when you try to shift-up beyond its max gear or
#   shift down below its minimum, and this function should output to the screen
#   what gear the Automobile object is in using the appropriate method of the
#   Automobile class.
#
#-------------------------------------------------------------------------------
#
# Your Name:  John Hellrung
#
class Automobile:
    def __init__(self):
        self.gear_state = 0 # set to neutral

# ##########################################################################
# PART 1:
#   Complete the two methods shift_up() and shift_down()
# ##########################################################################
    #########################
    # define the shift_up() function below, where each time it is called,
    # the gear is increased by one. This gear cannot go above 5, so once
    # it reaches 5, it stays there when this method is called.
    #########################
    def shift_up(self):
        if int(self.gear_state) < 5: #Checks the to see if the value store in self in great than 5
            Gear = self.gear_state + 1 #And if the value is greater then add 1 to its self
        return Gear # returns the value of gear
    #########################
    # define the shift_down() function below, where each time this method
    # is called, the gear_state decreases by one. This gear cannot go below
    # -2 (which is the fastest the automobile can go in reverse). Once the
    # gear reaches -2, it stays there if this method is called.
    #########################
    def shift_down(self):
        if int(self.gear_state) > int(-2): #Checks the to see if the value store in self in great than -2
            gear = self.gear_state - 1 #And if the value is greater then add 1 to its self
        return self # returns the value of gear

    def to_string(self):
        return "Auto is in {0} gear.".format(self.gear_state)
# ##########################################################################
# PART 2:
#   Complete the following function which TESTS the Automobile class.
#   Make sure to test for multiple gear shifts upwards and downwards. This
#   function should output to the screen what gear the Automobile object is
#   in using the appropriate method of the Automobile class.
# ##########################################################################
def test_Automobile_class():
    '''This function creates an object of type Automobile and tests whether
    the shift_up() and shift_down() methods of that class work.'''
    JH = ''
    A = 1 # I am having problems with this function because I dont know why it error messaging and I don't know what the question asking me to do.
    A.Automobile(JH) # I don't remember ever going over this in or out of class and I think that this is an unfair part of the exam.
    print Automobile.gear_state
    if Automobile.shift_down == -1: #Check to see if the out value of my functions are right
        print('True')
    else:
        print("False")

    if Automobile.shift_up == 1: #Check to see if the out value of my functions are right
        print('True')
    else:
        print("False")

test_Automobile_class()