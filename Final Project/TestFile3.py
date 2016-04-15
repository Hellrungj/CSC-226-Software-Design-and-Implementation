#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hellrungj
#
# Created:     27/04/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle
import Tkinter
import sys
import time
#===============================================================================
def left():
    Whale.setheading(0)
    Whale.backward(10)
    Events += 1
    MoveEskamos(HJ, Whale)
    GameStater(HJ) #insert Plantion is here
    global Events
    print Events
def right():
    Whale.setheading(0)
    Whale.forward(10)
    Events += 1
    MoveEskamos(HJ, Whale)
    GameStater(HJ) #insert Plantion is here
    global Events
    print Events
def Up():
    Whale.setheading(90)
    Whale.forward(10)
    Events += 1
    MoveEskamos(HJ, Whale)
    GameStater(HJ) #insert Plantion is here
    global Events
    print Events
def Down():
    Whale.setheading(270)
    Whale.forward(10)
    Events += 1
    MoveEskamos(HJ, Whale)
    GameStater(HJ) #insert Plantion is here
    global Events
    print Events
def Instructions():
    """Show the user the instructions"""
    display.setpos(0,170)
    display.write('Instructions',move=False,align='center',font=("Arial",30,("bold","normal")))
    display.setpos(0,100)
    display.write('''The goal of the game is live as long as you can
    without being killed by the Ekskamos.''',move=False,align='center',font=("Arial",15,("bold","normal")))
    display.setpos(0,50)
    display.write('Push the any arrow keys to begin.',move=False,align='center',font=("Arial",15,("bold","normal")))
    display.setpos(0,0)
    display.write('This message will last for 5 seconds.',move=False,align='center',font=("Arial",15,("bold","normal")))
    time.sleep(5)
    display.clear()
def Quit():
    GameStart.bye()
    sys.exit()
#===============================================================================
def GameStater(HJ): #insert Plantion is here
    """Starts the game"""
##    StartScreen(display)
    time.sleep(0.2)
##    if hit_by_Eskamos(Whale, Eskamo) == True:
##        print "GameOver"
##        GameOver()
##    elif Plankton_has_been_hit(Plankton, Whale) == True:
##        global Score
##        Plankton.clear()
##        Plankton.setposition(random.randrange(-230,230), random.randrange(-230,230))
##        Score += 1
##        print "Your Score is " + str(Score)
##        return Score
    if Hit_by_iceberg(HJ, Iceberg) == True:
        for Eskamo in HJ:
            Eskamo.clear()
#===============================================================================
def MoveEskamos(HJ, Whale):
    """Makes the Eskamos move"""
    print HJ
    for Eskamo in HJ:
        Eskamo.forward(10)
#===============================================================================
def Hit_by_iceberg(HJ, Iceberg):
    """The Eskamo hits a iceberg"""
    for Eskamo in HJ:
        xdistance = Eskamo.xcor() - Iceberg.xcor()
        ydistance = Eskamo.ycor() - Iceberg.ycor()
        if abs(xdistance) <= 20 and abs(ydistance) <= 20:
            return True
        else:
            return False
#===============================================================================
GameStart = turtle.Screen()
GameStart.setup(500,500)
GameStart.bgcolor("lightblue")

Events = 0
Score = 0

def Icebergs(X,Y):
    Iceberg = turtle.Turtle()
    global Iceberg
    Iceberg.penup()
    Iceberg.shape("arrow")
    Iceberg.color("White")
    Iceberg.left(90)
    Iceberg.setpos(X,Y)

Icebergs(50,50)
Icebergs(40,40)

Icebergs(50,0)
Icebergs(40,10)

Icebergs(0,50)
Icebergs(10,40)

Icebergs(0,0)
Icebergs(10,10)

Whale = turtle.Turtle()
Whale.color("yellow")
Whale.shape("square")
Whale.penup()

#===============================================================================
def Eskamos(X,Y):
    HJ = []
    Eskamo1 = turtle.Turtle()
    Eskamo1.color("red")
    Eskamo1.shape("arrow")
    Eskamo1.penup()

    Eskamo2 = turtle.Turtle()
    Eskamo2.color("red")
    Eskamo2.shape("arrow")
    Eskamo2.penup()

    Eskamo3 = turtle.Turtle()
    Eskamo3.color("red")
    Eskamo3.shape("arrow")
    Eskamo3.penup()

    Eskamo4 = turtle.Turtle()
    Eskamo4.color("red")
    Eskamo4.shape("arrow")
    Eskamo4.penup()

    Eskamo5 = turtle.Turtle()
    Eskamo5.color("red")
    Eskamo5.shape("arrow")
    Eskamo5.penup()

    Eskamo6 = turtle.Turtle()
    Eskamo6.color("red")
    Eskamo6.shape("arrow")
    Eskamo6.penup()

    Eskamo7 = turtle.Turtle()
    Eskamo7.color("red")
    Eskamo7.shape("arrow")
    Eskamo7.penup()

    Eskamo8 = turtle.Turtle()
    Eskamo8.color("red")
    Eskamo8.shape("arrow")
    Eskamo8.penup()

    Eskamo1.setpos(-200,190)
    Eskamo1.right(45)

    Eskamo2.setpos(-190,200)
    Eskamo2.right(45)

    Eskamo3.setpos(200,-190)
    Eskamo3.right(225)

    Eskamo4.setpos(190,-200)
    Eskamo4.right(225)

    Eskamo5.setpos(-200,-190)
    Eskamo5.left(45)

    Eskamo6.setpos(-190,-200)
    Eskamo6.left(45)

    Eskamo7.setpos(200,190)
    Eskamo7.left(225)

    Eskamo8.setpos(190,200)
    Eskamo8.left(225)
    return HJ
print HJ
#===============================================================================
GameStart.onkey(Instructions, "?")
GameStart.onkey(Up, "Up")
GameStart.onkey(left, "Left")
GameStart.onkey(right, "Right")
GameStart.onkey(Down, "Down")
GameStart.onkey(Quit, "q")

GameStart.listen()
Tkinter.mainloop()