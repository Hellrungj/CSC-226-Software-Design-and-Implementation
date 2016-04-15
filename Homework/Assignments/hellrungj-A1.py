######################################################################
# Author: John Hellrung
# username: hellrungj
#
# Assignment: A1
# Purpose: As a class demonstration of nested if statements
# using multiple elif keywords
######################################################################
# Acknowledgements:
# Big Bang Theory for the game idea.
# Jan Pearce and Mario Nakazawa for use of this original code.
######################################################################
import time
import random

#Rock's outcomes
Rsaying1= ('Rock crushes Lizard, you win!')
Rsaying2= ('Rock crushes Scissors, you win!')
Rsaying3= ('Rock was yaporized by Spock, you lose.')
Rsaying4= ('Rock was covered by Paper, you lose.')
#Paper's outcomes
Psaying1= ('Paper covers Rock, you win!')
Psaying2= ('Paper disproves Spock, yo win!')
Psaying3= ('Paper was cut up by Scissors, you lose.')
Psaying4= ('Paer was eaten by Lizard, you lose.')
#Scissor's outcomes
Ssaying1= ('Scissor cuts up Paper, you win!')
Ssaying2= ('Scissor decapitates Lizard, you win!')
Ssaying3= ('Scissor was smashed by Spock, you lose.')
Ssaying4= ('Scissor was Crushes by Rock, you lose')
#lizard's outcomes
Lsaying1= ('Lizard eats paper, you win!')
Lsaying2= ('Lizard poisons Spock, you win!')
Lsaying3= ('Lizard was decapitated by Scissors, you lose!')
Lsaying4= ('Lizard was crushed by Rock, you lose!')
#Spock's outcomes
SPsaying1= ('Spock yaporizes Rock, you win!')
SPsaying2= ('Spock smashes Scisors, you win!')
SPsaying3= ('Spock was poisoned by Lizard, you lose.')
SPsaying4= ('Spock was dosproved by Paper, you lose.')
#Choices
ChoiceRock = random.choice([Rsaying1,Rsaying2,Rsaying3, Rsaying4])
ChoicePaper = random.choice([Psaying1,Psaying2,Psaying3, Psaying4])
ChoiceScissors = random.choice([Ssaying1,Ssaying2,Ssaying3, Ssaying4])
ChoiceLizard = random.choice([Lsaying1,Lsaying2,Lsaying3, Lsaying4])
ChoiceSpock = random.choice([SPsaying1,SPsaying2,SPsaying3, SPsaying4])
#Welcome and raw_input
print('Welcome.')
time.sleep(1.0)
myinput = raw_input('Please choose one of the following words: Rock, Paper, Scissors, Lizard, Spock.')

print('')
#If Statement
if myinput == 'Rock':
    print('Rock, Paper, Scissors, Lizard, Spock, Shoot.')
    print('')
    print ChoiceRock
elif myinput == 'Paper':
    print('Rock, Paper, Scissors, Lizard, Spock, Shoot.')
    print('')
    print ChoicePaper
elif myinput == 'Scissors':
    print('Rock, Paper, Scissors, Lizard, Spock, Shoot.')
    print('')
    print ChoiceScissors
elif myinput == 'Lizard':
    print('Rock, Paper, Scissors, Lizard, Spock, Shoot.')
    print('')
    print ChoiceLizard
elif myinput == 'Spock':
    print('Rock, Paper, Scissors, Lizard, Spock, Shoot.')
    print('')
    print ChoiceSpock
else:
    print('Checking...')
    time.sleep(2.0)
    print('Sorry, What did you say!')
    print('Please try again but maks sure you have your anwser type correctly. (Case Sensitive)')
#Thanks and end of code
time.sleep(2.0)
print(" Thank you for playing")
print('')
time.sleep(3.0)
print('Created by John Hellrung for CSC 226')
print('Date: 1/12/2014')
print('Acknowledgements:')
print('Big Bang Theory for the game idea.')
print('Jan Pearce and Mario Nakazawa for use of this original code.')


