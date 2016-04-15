#-------------------------------------------------------------------------------
# Name:        John Hellrung
# Purpose:      Make a Live Path Number Game
#
# Author:      hellrungj
#
# Created:     01/28/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Acknowledgements:
#Thanks to Frederic Hamidi for his anwser on http://stackoverflow.com/questions/7282054/split-three-digit-integer-to-three-item-list-of-each-digit-in-python
#Dr. Jan Perice
#Dr. Mario Nakazawa
#-------------------------------------------------------------------------------
import time
#Add some fun to the coding
YESorNO = raw_input("Hello, User. Do you want to know your Live Number?")
print("Welcome, User what is your name?")
#makes the game more interactive.
if YESorNO == "yes" or YESorNO == "Yes":
    UserName =raw_input("Name Please.")
    #user put in  his or her's birth date.
    birthM = raw_input("Please input your birth month? (#s please)")
    birthD = raw_input("Please input your birth day? (#s please)")
    birthY = raw_input("Please input your birth year? (#s please)")
    #Months
    if birthM < 12 or birthM > 0:
        if birthM == 10:
            M = 1
        elif birthM==12:
            M = 3
        elif birthM==13:
            M = 4
        else:
            M = birthM
    else:
        M = 0
        print str("error")
    #Days
    if birthD > 31 or birthD < 0:
        if birthD == 10:
            D = 1
        elif birthD==20:
            D = 2
        elif birthD==(12,21,30):
            D = 3
        elif birthD==13:
            D = 4
        elif birthD==(14,23):
            D = 5
        elif birthD==(15,24):
            D = 6
        elif birthD==(16,25):
            D = 7
        elif birthD==(17,26):
            D = 8
        elif birthD==(18,27):
            D = 9
        elif birthD == (19,28):
            D = 10
        elif birthD == 29:
            D = 11
        else:
            D = birthD
    else:
        D = 0
        print str("error")
    #Years
    Y = map(int, str(birthY))
    Year = sum(Y)
    #LiveNumber
    time.sleep(1.0)
    print UserName + str("'s") + str(" life Number")
    print str(M) + "/" + str(D) + "/" + str(birthY),("Birth Date")
    A = int(M) + int(D) + int(Year)
    B = map(int, str(A))
    C = sum(B)
    if C == (11, 22):
        print C, str("Life Number")
    else:
        D = map(int, str(C))
        LifeNumber = sum(D)
        time.sleep(1.0)
        print str("Life Number is "), LifeNumber
        time.sleep(1.0)
        print("Thank you and have a great day,") + UserName + "."
        time.sleep(5.0)
else:
    print("Well then, have a great day, human.")
    time.sleep(3.0)