#-------------------------------------------------------------------------------
# Name:        John Hellrung & Gerardo Ivan Santos
# Purpose:
#
# Author:      hellrungj & santosg
#
# Created:     21/04/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Acknowledgements:
#   Bridget ODaniel - odanielb-A12.py
#
#
#-------------------------------------------------------------------------------
#make a game.

import turtle
import Tkinter
import sys
import random
import time


##def scoreNUM():
##    """"""
##    GameStart.setpos(300,300)
##    GameStart.write('Score: ' +str(score),move=False, align='left',font=("Arial",12("bold","normal")))
def Keep_Track(Ran):
    Ran += 1
    if Ran%2 == 0:
        Whale_has_been_hit(Whale, Eskamo,hit,Ran)

def Whale_has_been_hit(Whale, Eskamo,hit,Ran):
    """"""
    if hit == True:
        print "GameOver"
    else:
        hit = hit_by_Eskamos(Whale, Eskamo)
    Keep_Track(Ran)
    print hit
    return hit

def Plankton_has_been_eaten(Plankton, Whale):
    """"""
    if hitPlankton == True:
        hit = Plankton_has_been_hit(Plankton, Whale)
        Score += 1
        scoreNUM(Score)

def hit_by_Eskamos(Whale, Eskamo):
    """"""
    xdistance = Whale.xcor() - Eskamo.xcor()
    ydistance = Whale.ycor() - Eskamo.ycor()
    if abs(xdistance) <= 20 and abs(ydistance) <= 20:
        return True
    else:
        return False

def Plankton_has_benn_hit(Plankton, Whale):
    """"""
    xdistance = Whale.xcor() - Plankton.xcor()
    ydistance = Whale.ycor() - Plankton.ycor()
    if abs(xdistance) <= 20 and abs(ydistance) <= 20:
        return True
    else:
        return False


Score = 0
global Score

GameStart = turtle.Screen()
GameStart.setup(500,500)
GameStart.bgcolor("lightblue")

Whale = turtle.Turtle()
Whale.color("yellow")
Whale.shape("square")
Whale.penup()

def left():
    Whale.setheading(0)
    Whale.backward(10)
    Events += 1
    global Events
    print Events
def right():
    Whale.setheading(0)
    Whale.forward(10)
    Events += 1
    global Events
    print Events
def Up():
    Whale.setheading(90)
    Whale.forward(10)
    Events += 1
    global Events
    print Events
def Down():
    Whale.setheading(270)
    Whale.forward(10)
    Events += 1
    global Events
    print Events
def Quit():
    GameStart.bye()
    sys.exit()
#on key decations

Eskamo = turtle.Turtle()
Eskamo.color("red")
Eskamo.shape("square")
Eskamo.penup()
Eskamo.ht()
Eskamo.setpos(random.randrange(-230,230), random.randrange(-230,230))
Eskamo.st()
#Comes from the edges (2) first and later from the sides (1)
#move dictacrt then when it parlael it will move staight
#function

def Icebergs(x,y):
    Icebergs = turtle.Turtle()
    Icebergs.color("white")
    Icebergs.shape("triangle")
    Icebergs.penup()
    Icebergs.setpos(x,y)
    #Start and stay at four differnt locations
    #function

def Plankton(a):
    (x,y) = a
    Plankton = turtle.Turtle()
    Plankton.color("green")
    Plankton.shape("arrow")
    Plankton.penup()
    Plankton.setposition(x,y)
#Randomly Appers on the screen
#function

##scoreNUM()

PlanktonSET1 = [100,0]
PlanktonSET2 = [-100,0]
PlanktonSET3 = [-100,100]
PlanktonSET4 = [100,100]

PlanktonSET = random.choice([PlanktonSET1,PlanktonSET2,PlanktonSET3,PlanktonSET4])

Plankton(PlanktonSET)

HitPlantion = False
hit = False
Ran = 0
Events = 0

Icebergs(200,200)
Icebergs(200,0)
Icebergs(-200,200)
Icebergs(-200,0)


Whale_has_been_hit(Whale, Eskamo, hit,Ran)
GameStart.onkey(Up, "Up")
GameStart.onkey(left, "Left")
GameStart.onkey(right, "Right")
GameStart.onkey(Down, "Down")
GameStart.onkey(Quit, "q")

GameStart.listen()
Tkinter.mainloop()

#===============================================================================
#  !                                                                       !
# !                                                                          !
#                           $
#                       7           7
#                      7           7
#                     7             7
#                           &
#                     7             7
#                      7          7
#                     7          7
#
#
#
#
# !                                                                        !
#  !                                                                      !
#===============================================================================