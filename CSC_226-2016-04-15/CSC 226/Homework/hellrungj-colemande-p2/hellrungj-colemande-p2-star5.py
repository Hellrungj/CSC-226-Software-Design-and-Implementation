#-------------------------------------------------------------------------------
# Name:        John Hellrung and Demetris Coleman
# Purpose:
#
# Driver:      hellrungj
# Naviagator:    colemande
#
# Created:     15/01/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Acknowledgements:
#Dr. Jan Pearce
#Dr. Mario Nakazawa
#Demetris Coleman
#-------------------------------------------------------------------------------
import turtle
wn = turtle.Screen()

myturtle = turtle.Turtle()

head=90
myturtle.setheading(head)
myturtle.pensize(4)
myturtle.color('red')

for i in range(5):
    myturtle.left(144)
    myturtle.forward(100)

myturtle.penup()
myturtle.hideturtle()
myturtle.color('black')
myturtle.write('Create by John Hellrung and Demetris Coleman',("Arial",8))
#"Arial",8,

wn.exitonclick()




