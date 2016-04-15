######################################################################
# Author: John Hellrung
# username: hellrungj
# Assignment: A0
# Purpose: To test out the installation of python and pyscripter
# and to play around with a few features of the python language.
#Class CSC 266
#Made: Jan. 9, 2014
#
######################################################################
# Acknowledgements:
# Original code written by Dr. Jan Pearce
######################################################################

import time          # import a library with time.sleep()
import random        # import a library with random.choice()

saying1='Is this, Ivan. If not, still stop tring to sign-in.'
saying2='Sup, sorry but your not John.'
saying3='Hello, this 2244JH Dell model E5430 and go die.'
saying4='Jump in a lake of fire.'
saying5='2244JH is ready to sever but first you have to sign-in.'

somechoice = random.choice([saying1,saying2,saying3, saying4, saying5])

# This is how to ask for input from the keyboard:
myname = raw_input('Name')

print('') # This prints a blank line.

#This is a python conditional statement
if myname == 'JohnHellrung' or myname == 'hellrungj':
    print('Hello, Sir ' + myname + '!' )
    print(':)')
    time.sleep(1.0)
    print('How can 2244JH sever you, today.')

elif myname == 'John': # else if
    print('Hello, ' + myname + '!')
    time.sleep(0.5)
    print('')
    print('Checking...')
    time.sleep(1.2)
    print('John, Who?')
    print('Whats is your last name')
    time.sleep(3)
    print('Remember Lightbriger')

else:
    print('Hello, ' + myname + '!')
    time.sleep(0.5)
    print('')
    print('Checking...')
    time.sleep(1.2)
    print(somechoice)
    time.sleep(1.0)
    print('Failure to sign-in. Please, try again.')
    time.sleep(2.0)
    print('remember to not leave any blanks')

# Be sure to change the filename of this file to your username-a0.py
