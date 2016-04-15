#-------------------------------------------------------------------------------
# Purpose:
#
# Author:      hellrungj
#
# Created:     16/01/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Acknowledgements:
#Dr. Jan Pearce
#http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html
#licensed under a Creative Commons
#Attribution-Noncommercial-Share Alike 3.0 United States License.
#-------------------------------------------------------------------------------
import turtle
import time
import random

choice = random.choice([90,180,270,360])

myinput = raw_input('Do yo want see a turtle?:')

if myinput == 'Yes' or 'yes':
    wn = turtle.Screen()
    myturtle = turtle.Turtle()

    myturtle.shape('turtle')
    myturtle.color('red')

    head=30
    myturtle.setheading(head)
    myturtle.pensize(5)
    myturtle.speed(0)
#looping into a loop was hard
    Hellrung = ["1""2""3""4"]
    for t in Hellrung:
        John = ["1","2","3","4"]
        for c in John:
            if c == '2' or c == '4':
                myturtle.color("blue")
            else:
                myturtle.color("red")

            for i in range(5):
                myturtle.forward(200)
                myturtle.left(144)

            for r in range(350):
                myturtle.left(1)
                myturtle.forward(1)

            for e in range(350):
                myturtle.right(1)
                myturtle.forward(1)

            myturtle.right(90)
            myturtle.forward(100)
# How do you set up a color witch red to blue
        head = choice
        myturtle.penup()
        myturtle.forward(200)
        myturtle.pendown()

    wn.exitonclick()
else:
    print('good bye')

