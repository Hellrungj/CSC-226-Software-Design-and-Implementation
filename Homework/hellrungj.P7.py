#-------------------------------------------------------------------------------
# Name:        John Hellrung, Carlos A. Berejnoi Bejarano, & James D. Thompson
# Purpose:      To make a code the writes out a story with user input.
#
# Usernames:      hellrungj, bejaranoc, & thompsonj
#
# Created:     17/02/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time

def Story_Ep1(N1,V1,N2,N3,A1,N4,N5,N6):
    '''Tells the story of the main character in Ep. 1'''
    print("Ep.1: Follow the Clue.")
    print("")
    time.sleep(3)
    print("In the town of {1}, {2} and {3} find themselves looking into the clue of {4} witch leads them both to investgating a house named {0}.").format(N2,N5,N1,N3,N4)
    time.sleep(3)
    print ("{0} starts looking into the first room to the left and {1} goes into the second room to their right.").format(N1,N3)
    time.sleep(3)
    print("As, {0} and {1} seached the house, they both wondered to where would {2} have disappeared, last night.").format(N1,N3,N4)
    time.sleep(3)
    print ("Then, suddenly {1} saw a {0} looking creature.").format(A1,N1)
    time.sleep(3)
    print("{0} started to {1} but then see that the was creature was real {0} ran through the house, until {0} slip on {2}.").format(N1,V1,N6)
    time.sleep(3)
    print("BAM, {0} hit to the floor, the creature stoped and then fell to it's knees in tears, laughing.").format(N1)
    time.sleep(3)
    print ("After the initial confusion, {0} realized it was {1}.").format(N1,N3)
    time.sleep(3)
    print("As {0} looked around {0} and {1} both realized that, now they both were up stairs.").format(N1,N3)
    time.sleep(3)
    print('"You nearly gave me a heart attack, said {0}."').format(N1)
    time.sleep(3)
    print ('"I apologies I did not mean it. I was only looking for a way to surpise you."')
    time.sleep(3)
    print("Then, came a gust of wind from outside, opening the door infont of them.")
    time.sleep(3)
    print("{0} and {1} both enter the next room.").format(N1,N3)
    time.sleep(3)
    print('On the table was the next note saying "Watch for who you call friends."')
    time.sleep(3)
    print("{0} starts steping out of the room").format(N3)
    time.sleep(3)
    print ('"Hey {0}, look at the time." I see you later {0}').format(N1)
    time.sleep(3)
    print ("{0} when came to the conculion that {1}, was the reason why, {2} disappear.").format(N1,N3,N4)
    time.sleep(3)
    print("When {0} rans out of house.").format(N3)
    time.sleep(3)
    print("")
    print ("ZiPPPPPPPPPPPPPP")
    print("")
    time.sleep(3)
    print("{0} ran after {1} as fast as {0}'s legs could carry {0} but then {0}'s legs gave out.").format(N1,N3)
    print("")
    time.sleep(3)
    print("A few seconds, later.")
    print("")
    time.sleep(3)
    print("{0} walks to the sidewalk and sits down. Out of breath {0} yells in to the cold dark nite.").format(N1)
    time.sleep(3)
    print('"{0}, YOU CAN NOT HIDE. I WILL FIND YOU. {0}! {0}, WHERE ARE YOU!"').format(N3)
    print("")
    time.sleep(3)
    print("{0} sat back down on the sidewalk think to themself.").format(N1)
    time.sleep(3)
    print("As, {0} sat there tring to piece together the events of the last 24 hours, {0} looked down at the note again {0} had found in the house, ealier.").format(N1)
    time.sleep(3)
    print('Then, {0} looks up and says "FOUND IT."').format(N1)
    print("")
    time.sleep(3)
    print("See, next time.").format(N1)

def Back_Story(N1,N3,N4,N2,N6):
    '''Tells the back around story for Ep. 1'''
    print("Back Story.")
    print("")
    print("{0} was at a off campus party.").format(N1)
    time.sleep(3)
    print("You see,{0} had past out and awoke to find that {1} was missing.").format(N1,N4)
    time.sleep(3)
    print("So, after looking around the house that {0} had pasted out in, {0} looked down at he watch and realized what time it is.")
    print('"I am going to be late to class."').format(N1)
    time.sleep(3)
    print("{0} ran to class and finds that {1} is not there.").format(N1,N4)
    time.sleep(3)
    print('After class {0} ask {1} if {1} had seen {2} after the party last night.').format(N1,N3,N4)
    time.sleep(3)
    print('{0} said with "No but I found a note on the front door of her house.').format(N3)
    time.sleep(3)
    print("After {1} had read the note, both {0} and {1} started reseaching for the anwser to clue in the note that {2} had lefted for them.").format(N1,N3,N4)
    print("There reseach lead them to a house name {0} in {1}.").format(N2,N6)
    print("")
    print("")
    time.sleep(5)

YESNO = raw_input("Do you want the back story?(yes or no)")#Asks te user if he or she want to know the back story.
N1 = raw_input("Noun(Main Character Name)")#noun for main character
V1 = raw_input("Verb(Action)")#verb for an action
N2 = raw_input("Noun(House)")#noun for a house
N3 = raw_input("Noun(Friend of the main character)")#noun for another character
A1 = raw_input("Adjective")#adjective for a description
N4 = raw_input("Noun(Name of Character)")#noun for a third character
N5 = raw_input("Noun(Town)")#noun for a town
N6 = raw_input("Noun(Item)")#noun for an item.
if YESNO == "YES" or YESNO == "yes":#An if statement for if the user want to know the back story
    print str(Back_Story(N1,N3,N4,N2,N6))
else:
    pass
print str(Story_Ep1(N1,V1,N2,N3,A1,N4,N5,N6))
print('')
print("Thanks you, for reading.")
time.sleep(25)