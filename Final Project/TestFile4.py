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

s = turtle.Screen()
s.bgcolor("lightblue")

def Eskamos():
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
    HJ.append(Eskamo1)
    HJ.append(Eskamo2)
    HJ.append(Eskamo3)
    HJ.append (Eskamo4)
    HJ.append (Eskamo5)
    HJ.append (Eskamo6)
    HJ.append (Eskamo7)
    HJ.append(Eskamo8)
    return HJ
print Eskamos()

def Icebergs():
    JH = []
    Iceberg1 = turtle.Turtle()
    Iceberg1.penup()
    Iceberg1.shape("arrow")
    Iceberg1.color("White")
    Iceberg1.left(90)

    Iceberg2 = turtle.Turtle()
    Iceberg2.penup()
    Iceberg2.shape("arrow")
    Iceberg2.color("White")
    Iceberg2.left(90)

    Iceberg3 = turtle.Turtle()
    Iceberg3.penup()
    Iceberg3.shape("arrow")
    Iceberg3.color("White")
    Iceberg3.left(90)

    Iceberg4 = turtle.Turtle()
    Iceberg4.penup()
    Iceberg4.shape("arrow")
    Iceberg4.color("White")
    Iceberg4.left(90)

    Iceberg5 = turtle.Turtle()
    Iceberg5.penup()
    Iceberg5.shape("arrow")
    Iceberg5.color("White")
    Iceberg5.left(90)

    Iceberg6 = turtle.Turtle()
    Iceberg6.penup()
    Iceberg6.shape("arrow")
    Iceberg6.color("White")
    Iceberg6.left(90)

    Iceberg7 = turtle.Turtle()
    Iceberg7.penup()
    Iceberg7.shape("arrow")
    Iceberg7.color("White")
    Iceberg7.left(90)

    Iceberg8 = turtle.Turtle()
    Iceberg8.penup()
    Iceberg8.shape("arrow")
    Iceberg8.color("White")
    Iceberg8.left(90)

    Iceberg9 = turtle.Turtle()
    Iceberg9.penup()
    Iceberg9.shape("arrow")
    Iceberg9.color("White")
    Iceberg9.left(90)

    Iceberg10 = turtle.Turtle()
    Iceberg10.penup()
    Iceberg10.shape("arrow")
    Iceberg10.color("White")
    Iceberg10.left(90)

    Iceberg11 = turtle.Turtle()
    Iceberg11.penup()
    Iceberg11.shape("arrow")
    Iceberg11.color("White")
    Iceberg11.left(90)

    Iceberg12 = turtle.Turtle()
    Iceberg12.penup()
    Iceberg12.shape("arrow")
    Iceberg12.color("White")
    Iceberg12.left(90)


    Iceberg1.setpos(-70,50)
    Iceberg2.setpos(-60,40)
    Iceberg3.setpos(-60,60)

    Iceberg4.setpos(70,-50)
    Iceberg5.setpos(60,-40)
    Iceberg6.setpos(60,-60)

    Iceberg7.setpos(-70,-50)
    Iceberg8.setpos(-60,-40)
    Iceberg9.setpos(-60,-60)

    Iceberg10.setpos(70,50)
    Iceberg11.setpos(60,40)
    Iceberg12.setpos(60,60)

    JH.append(Iceberg1)
    JH.append(Iceberg2)
    JH.append(Iceberg3)

    JH.append(Iceberg4)
    JH.append(Iceberg5)
    JH.append(Iceberg6)

    JH.append(Iceberg7)
    JH.append(Iceberg8)
    JH.append(Iceberg9)

    JH.append(Iceberg10)
    JH.append(Iceberg11)
    JH.append(Iceberg12)
    return JH
print Icebergs()