#-------------------------------------------------------------------------------
# Name:        John Hellrung
# Purpose: To make a house from turtles.
#
# Username:      hellrungj
#
# Created:     21/01/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle
import time
import random

wn=turtle.Screen()
John=turtle.Turtle()

John.shape('turtle')
John.color('black')

head=90
John.setheading(head)
John.pensize(8)
John.speed(0)
wn.bgcolor("lightblue")

#base of the house
#don't understand why this will not fill in my home with color
John.fillcolor("white")
for i in range(5):
    John.forward(200)
    John.left(90)

#top of house
John.right(45)
John.forward(140)
John.left(90)
John.forward(140)

#reset to the orign
John.left(45)
John.penup()
John.forward(200)
John.pendown()
John.color("darkgreen")
John.right(90)

#make a tree
John.forward(100)
John.right(90)
John.forward(100)
for f in range(200):
    John.left(2)
    John.forward(1)
John.forward(12)
for a in range(200):
    John.right(2)
    John.forward(1)
John.forward(12)
for s in range(200):
    John.left(2)
    John.forward(1)

#Reset to the orgin
John.penup()
John.right(125)
John.forward(100)
John.forward(100)
John.right(90)
John.forward(200)
John.left(85)
John.pendown()
John.forward(500)
John.backward(1000)

#Make a small tree
John.forward(200)
John.left(90)
John.forward(75)
for f in range(200):
    John.left(2)
    John.forward(1)
John.forward(12)
for a in range(200):
    John.right(2)
    John.forward(1)
John.forward(12)
for s in range(200):
    John.left(2)
    John.forward(1)

#reset to the orgin
John.penup()
John.right(125)
John.forward(300)
John.right(90)
John.forward(175)

#Make a Tall tree
John.left(85)
John.forward(350)
John.left(90)
John.pendown()
John.forward(160)
for f in range(200):
    John.right(2)
    John.forward(1)
John.forward(12)
for a in range(200):
    John.left(2)
    John.forward(1)
John.forward(12)
for s in range(200):
    John.right(2)
    John.forward(1)

#return to the orign
John.penup()
John.right(45)
John.backward(300)
John.left(90)
John.backward(200)
John.left(85)
John.pendown()

#Make a door
John.color("black")
John.forward(20)
John.right(90)
John.forward(40)
John.right(90)
John.forward(20)
John.right(90)
John.forward(40)

#Make a label
John.penup()
John.forward(100)
John.right(270)
John.forward(59)
John.pendown()
John.color("red")
John.hideturtle()
John.write("John Hellrung's House")
wn.exitonclick()