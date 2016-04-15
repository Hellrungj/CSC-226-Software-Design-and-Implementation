######################################################################
# Author: John Hellrung
# username: hellrungj
#
# Assignment: A1
# Purpose: As a class demonstration of nested if statements
# using multiple elif keywords
######################################################################
# Acknowledgements:
# Code
#
#
######################################################################
import time          # import a library with time.sleep()
import random        # import a library with random.choice()

# This is how to ask for input from the keyboard:
myinput = raw_input('Please enter a three letter word: ')

print('Your word is: ' + myinput + '!')

print('') # This prints a blank line.

if myinput == 'cat' or myinput == 'dog':
    print('I guess you like pets!')
    if myinput == 'dog': #This if statment will only run if myinput is either cat or dog.
        print('If a dog barks his head off in the forest and no human hears him, is he still a bad dog?')
    else: #we only get here if the input was cat
        print('What do cats like to eat for breakfast?')
        time.sleep(2)
        print('Mice Krispies!')
elif myinput == 'the': #This is gotten to if the input was neither cat nor dog.
    print('What the???')
elif myinput == 'and':
    print('and, what???')
elif myinput == 'for':
    print('What for???')
elif myinput == 'but':
    print("but what?! Don't be contrary!")
else:
    print('Thanks for the ' + myinput + '!')

# The following are from http://www.brainyquote.com/quotes/topics/topic_computers.html
saying1='Computing is not about computers any more. It is about living...  N. Negroponte'
saying2='Computers are famous for being able to do complicated things starting from simple programs... S. Lloyd'
saying3='The good news about computers is that they do what you tell them to do. The bad news is that they do what you tell them to do... T. Nelson'
saying4='The digital revolution is far more significant than the invention of writing or even of printing... D. Engelbart'
# The following is from http://en.wikipedia.org/wiki/Doctor_Who
saying5='The world would be a poorer place without Doctor Who... Director Steven Spielberg'

somechoice = random.choice([saying1,saying2,saying3, saying4, saying5])

time.sleep(0.5)
print('')
print('Have you heard this one?')
print(somechoice)

# Be sure to change the filename of this file to your username-a1.py