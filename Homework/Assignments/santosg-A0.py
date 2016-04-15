######################################################################
# Author: Ivan Santos
# username: santosg
# Assignment: A0
# Purpose: To test out the installation of python and pyscripter
# and to play around with a few features of the python language.
#
#
#
######################################################################
# Acknowledgements: ****** CHANGE ALL OF THESE!! *****
#   This program utilizes inspiration from Ivan's brain
#   from Ivan's Websites, http://gismc.us/ and
#   from http://www.gismc.net/

# You need to acknowledge having modifed this code and all other code you modify
# or use for assitance.
#   To do so, you will indicate something like:
#   Mopidied from code written by Dr. Jan Pearce
#   Original code downloaded from:
#   http://faculty.berea.edu/pearcej/csc226/tasks/yourusername-A0.py
######################################################################

import time          # import a library with time.sleep()
import random        # import a library with random.choice()

# This is how to ask for input from the keyboard:
myname = raw_input('Please enter your name: ')

print('') # This prints a blank line.

#This is a python conditional statement
if myname == 'Ivan' or myname == 'Gerardo':
    print('Dear ' + myname + ' you are AWESOME!' )

elif myname == 'Dean': # else if
    print('Dean. Who?')
    print('Hey,... Dean Wilder,...')
    time.sleep(2)
    print('You are Legen... Wait for It ... Dary')
    time.sleep(2)
    print('You are Legendary')


else:
    print('Hello, ' + myname + '!')

# The following are from http://www.brainyquote.com/quotes/topics/topic_computers.html
saying1='Computing is not about computers any more. It is about living...  N. Negroponte'
saying2='Computers are famous for being able to do complicated things starting from simple programs... S. Lloyd'
saying3='The good news about computers is that they do what you tell them to do. The bad news is that they do what you tell them to do... T. Nelson'
saying4='Its the dreams that never came true, Cause your too damn scared to try... Actress/Singer Selena Gomez'
# The following is from Hot The Lights by Selena Gomez
saying5='Its the dreams that never came true, Cause your too damn scared to try... Actress/Singer Selena Gomez'

somechoice = random.choice([saying1,saying2,saying3, saying4, saying5])

time.sleep(0.75)
print('')
print('Listen to this!')
print(somechoice)

# Be sure to change the filename of this file to your username-a0.py
