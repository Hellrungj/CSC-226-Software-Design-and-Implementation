    ######################################################################
# Author: Dr. Jan Pearce
# username: pearcej
#
# Purpose: demonstration of event-driven programming using the turtle library
######################################################################
# Acknowledgements:
#    Mario Nakazawa added the quit_box to close more cleanly
######################################################################
import time
import turtle
import random

turtle.colormode(255)
wn = turtle.Screen()  # Get a reference to the window
#wn.exitonclick()  # wait for a user click on the canvas


# Create turtle for header
header = turtle.Turtle()
header.penup()
header.setpos(-10,150)
header.write("Click one of the big choices",move=False,align='center',font=("Arial",30,("bold","normal")))
header.hideturtle()

# Create turtle for choice of 1
one = turtle.Turtle()
one.color("purple")
one.shapesize(3)
one.penup()
one.setpos(-100,20)
one.shape("circle")

# Create turtle for choice of 2
two = turtle.Turtle()
two.color("#0000FF")
two.shapesize(3)
two.penup()
two.setpos(100,20)
two.shape("circle")
two.stamp()
two.color("#000099")
two.setpos(110,25)
two.stamp()

# use a "quitter" turtle to draw some text to stop the loop.
quit_box = turtle.Turtle()
quit_box.penup()
quit_box.hideturtle()
quit_box.setpos(-60,-200)
quit_box.write("Click to stop ->",move=False,align='center',font=("Courier New",15,("bold","normal")))

quit_box.showturtle()
quit_box.setpos(60,-190)
quit_box.shapesize(1,1,15)
quit_box.shape("square")
quit_box.color("#AFA4AF")

# Create turtle for text
text = turtle.Turtle()
text.penup()
text.setpos(0,-150)
text.hideturtle()

def handler_one(x, y):
    '''called when circle one is clicked'''
    wn.title("1 clicked")
    text.clear()
    text.write("1 clicked",move=False,align='center',font=("Arial",30,("bold","normal")))
    # add more code here for when the user clicks 1

def handler_two(x, y):
    '''called when circle two is clicked'''
    wn.title("2 clicked")
    text.clear()
    text.write("2 clicked",move=False,align='center',font=("Arial",30,("bold","normal")))
    # add more code here for when the user clicks 2

def display_nim(numb):
    '''called to display numb many circles of random colors'''
    turtle.colormode(255)
    position=-150
    for i in range(numb):
        num = turtle.Turtle()
        num.shape("circle")
        num.color(random.randrange(256),random.randrange(256),random.randrange(256))
        num.penup()
        num.setposition(position+20*i, 130)
        num.stamp()

def quit_nim(x,y):
    '''called in order to return the true value'''
    quit_box.hideturtle()
    text.clear()
    text.write("Quitting",move=False,align='center',font=("Arial",30,("bold","normal")))

wn.onkey(quit_nim,"q")
wn.listen()
#main loop
while quit_box.isvisible():
    numb=15 # we will allow the user to enter this.
    quit_box.onclick(quit_nim)
    one.onclick(handler_one)
    two.onclick(handler_two)
    display_nim(numb)

wn.bye()
