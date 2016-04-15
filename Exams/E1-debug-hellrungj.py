#-------------------------------------------------------------------------------
# Name:       E1-debug-guessing-1or2.py
# Purpose: A program that needs to be debugged. It asks the user until the user
#       inputs either a 1 or 2 and then outputs "Right!" if the user put in a
#       2 and "Wrong!" otherwise.
#
# Author:   Mario Nakazawa
# Username: nakazawam
# Editor: John Hellrung
# Editor Username: hellrungj
#
# Created:     Feb/13/2014
# ------------------------------------------------------------------------------
# Exam E1 Part B
# Instructions:
#   You are to debug this program and modify it so that it works as expected,
#   which you can do in various ways, such as manually tracing the code or using
#   the tools like the debugger that come with PyScripter. You are to ONLY debug
#   the program; DO NOT change the structure of the program.
#
#   1) You must add comments to this code at each of the errors you find explaining
#      exactly what steps you took to get find them.
#   2) Fill out your name in the space below
#   3) Save this file as E1-Debug-<yourname>.py
#   4) Upload this file to the Exam 1 submission spot on Moodle when you are done.
#-------------------------------------------------------------------------------
#
# Your Name:  John Hellrung
#Username: hellrungj

def prompt_user( question, valid_response1, valid_response2 ):
    ''' Ask the user the question with the valid responses added to the end of the
        prompt in parentheses. Return back the user's response.'''
    response =""
    while (response != valid_response1 and response != valid_response2 ):
        # the next line asks the user to input either a 1 or 2 and saves the input to response
        response = int(raw_input(str(question) + "(" + str(valid_response1) + " or " + str(valid_response2) + ")"))# I add a int() to made the output of this rawinput a indenger and i also had to make the varibles in to string by adding str().
    return response

# Call the prompt_user function with the question and the two numbers to
# ask the user to input either the number 1 or 2
user_input=prompt_user("Guess a number", 1, 2)
if user_input == 1: # The statemnet has to have == to be equal any thing because an if statment compairs two or more things.
    print("Wrong!")
else: #you want a else because the user guess a numder and he/she is only right or wrong.
    print("Right!")
