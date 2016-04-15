#-------------------------------------------------------------------------------
#Name: John Hellrung
#Username:   hellrungj
# Purpose:  A project for learning eventdriven programing in python.
#
# Created:     13/03/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#acknowlegdements:
#How to Think Like a Computer
#Scientist: Learning with Python 3
#Documentation
#Release 3rd Edition
#Peter Wentworth, Jeffrey Elkner,
#Allen B. Downey and Chris Meyers
#August 12,
#Dr. Jan Pearce
#Dr. Mario Nakawaza
#-------------------------------------------------------------------------------
import turtle
import Tkinter
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("John's Epic Game")
wn.bgcolor("darkblue")

Title = turtle.Turtle
Title.write("Click the yellow square and red triangle, the both will a circle if click the right of times.",move=False,align='center',font=("Arial",15,("bold","normal")))

tess = turtle.Turtle()
tess.color("white")
tess.pensize(3)
tess.shape("circle")

John = turtle.Turtle()
John.color("green")
John.pensize(4)
John.shape("triangle")

Alex = turtle.Turtle()
Alex.color("red")
Alex.pensize(5)
John.shape("triangle")

F = turtle.Turtle()
F.color("yellow")
F.pensize(7)
F.shape("square")

def MouseMove(x, y):
    '''Draws a line from orgian and where the user clicked'''
    tess.goto(x, y)

def KeyMoveForward():
    '''Make John draw a turtle forward'''
    John.forward(30)

def KeyMoveLeft():
    '''Make John draw a turtle to the lift'''
    John.left(90)
    John.forward(30)

def KeyMoveRight():
    '''Make John draw a turtle to the right'''
    John.right(90)
    John.forward(30)

def KeyMoveBack():
    '''Erases the line and moves the turtle'''
    John.color("darkblue")
    John.backward(30)
    John.color("green")

def KeyBYE():
    '''Close down the turtle window'''
    wn.bye()

def handler_for_F(x, y):
    '''Makes Circles'''
    wn.title("Tess clicked at {0}, {1}".format(x, y))
    for i in range(8):
        F.left(42)
        F.forward(30)
    F.forward(30)
    wn.title("John's Epic Game")

def handler_for_Alex(x, y):
    '''Makes Circles'''
    wn.title("Alex clicked at {0}, {1}".format(x, y))
    for r in range(4):
        Alex.right(84)
        Alex.forward(50)
    Alex.forward(30)
    wn.title("John's Epic Game")

wn.onkey(KeyMoveBack,"Down")
wn.onkey(KeyMoveForward, "Up")
wn.onkey(KeyMoveLeft, "Left")
wn.onkey(KeyMoveRight, "Right")
wn.onkey(KeyBYE, "q")
wn.onclick(MouseMove)
F.onclick(handler_for_F)
Alex.onclick(handler_for_Alex)


wn.listen()

Tkinter.mainloop()