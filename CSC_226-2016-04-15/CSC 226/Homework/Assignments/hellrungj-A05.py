#################################################################################
# Author:John Hellrung
#
# Purpose: to make a street with turtles.
#
#################################################################################
# Acknowledgements:
# Jan Pearce
# Mario Nakazawa
#
#################################################################################
import turtle
#the if statement will not work and i don't understand.
my_input=raw_input('Do yo want see a turtle?:')
if my_input == "yes" or "Yes":
    turtle.colormode(356)   # change color modes
    wn = turtle.Screen()    # make screen close cleanly
    wn.bgcolor("#FF4500")   # Hexadecimal colors RGB


    def J(x, y, roofcolor, housecolor, s):
        h=turtle.Turtle()
        h.hideturtle()
        h.up()
        h.setpos(x,y)

        #make main house rectangle
        h.color(housecolor)
        h.begin_fill()
        for j in range(2):
            h.right(90)
            h.forward(s)
            h.right(90)
            h.forward(s)
        h.fill(False)
        h.end_fill()
        h.left(90)

        h.forward(0)
        h.setheading(0)

        #make roof
        h.color(roofcolor)
        h.begin_fill()
        for side in range(3):
            h.left(120)
            h.forward(s)
        h.fill(False)
        h.end_fill()
        h.up()

        return h

    # draws a grey street
    JohnStreet=turtle.Turtle()
    JohnStreet.pencolor('#656680')
    JohnStreet.penup()
    JohnStreet.setpos(0,-40)
    JohnStreet.pendown()
    JohnStreet.pensize(30)
    JohnStreet.forward(800)
    JohnStreet.backward(1200)
    JohnStreet.up()

    John=turtle.Turtle()
    John.pencolor('blue')
    John.penup()
    John.setpos(0,-40)
    John.right(90)
    John.forward(80)
    John.right(90)
    John.pendown()
    John.pensize(30)
    John.forward(400)
    John.backward(1600)
    John.up()

    hellrung=turtle.Turtle()
    hellrung.pencolor('#656680')
    hellrung.penup()
    hellrung.setpos(0,-40)
    hellrung.right(90)
    hellrung.forward(140)
    hellrung.right(90)
    hellrung.pendown()
    hellrung.pensize(30)
    hellrung.forward(400)
    hellrung.backward(1600)
    hellrung.up()

    #populates the street with houses
    for i in range(6):
        h=J(i*150-5-240, i-20, 'darkred', 'white', 80) #begins drawing off screen
        h=J(i*150-240, i-70, 'lightgreen', 'yellow',80)
    #Make a Tree
    #don't understand why this will not work
    k=turtle.Turtle
    k.pencolor("green")
    k.forward(20)
    k.right(90)
    k.forward(100)
    for f in range(200):
        k.left(2)
        k.forward(1)
    k.forward(12)
    for a in range(200):
        k.right(2)
        k.forward(1)
    k.forward(12)
    for s in range(200):
        k.left(2)
        k.forward(1)
    # write text
    JohnStreet.color("white")
    JohnStreet.setpos(30,-120)
    JohnStreet.write("John's Street",move=False,align='center',font=("New Times Roman",30,("bold","normal")))


    wn.exitonclick()  # wait for a user click on the canvas
else:
    print("good bye.")