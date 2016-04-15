######################################################################
#Authors Demetris Coleman and  John Hellrung
# modified from http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html
# Objectives:
#- Introduces the use of the turtles library
######################################################################
# Acknowledgements:
#Driver: colemande
#
# modified by Dr. Jan Pearce
#remodified by Demetris Coleman
# modified from http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window--needed for a clean close

triangle1 = turtle.Turtle()  # create a turtle named myturtle

triangle1.shape('turtle')    # shapes possible are 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
triangle1.color('black')
triangle1.hideturtle()

head=0                     # initial heading for turtle
triangle1.setheading(head)
triangle1.pensize(5)

triangle1.forward(200)           # tell myturtle to move forward by 150 units
triangle1.left(120)               # turn by 90 degrees
triangle1.forward(200)         # complete the second side of a rectangle
triangle1.left(120)
triangle1.forward(200)

head2=90
triangle2 = turtle.Turtle()
triangle2.hideturtle
triangle2.setheading(head2)
triangle2.color("black")
triangle2.pensize(5)
triangle2.penup()
triangle2.forward(120)
triangle2.pendown()
triangle2.right(90)
triangle2.forward(200)
triangle2.right(120)
triangle2.forward(200)
triangle2.right(120)
triangle2.forward(200)

triangle1.hideturtle()
triangle1.penup()
triangle1.goto(0,-65)

triangle1.write("6 point star by John Hellrung and Demetris Coleman",)


wn.exitonclick()            # Added by Dr. Pearce to wait for a user click on the canvas




