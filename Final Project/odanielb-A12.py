#-------------------------------------------------------------------------------
# Name: Bridget O'Daniel
# Username: odanielb
#
# Assignment: A12: Interactive Graphics
# Purpose: To play a game of snake, which is always fun and entertaining although quite frustrating at times. Use arrow keys to change direction and
# try to eat 10 food squares. Don't hit walls or your tails! Click screen to start and press it again to quit.
#
# Acknowledgements: The exit method here: http://docs.python.org/2/library/sys.html#sys.exit
#
#Errors: displays an error when you quit by pressing the screen. Only does so because the program moves by timer, rather than waiting for key presses,
# meaning that once the user presses quit, it will sometimes have already done something that is impossible once the window closes. I could find
# no way to correct this problem, but all other ways of quitting (by running into something or winning) quit cleanly. Also, speed could not increase
# steadily because processing time slowed down the snake with each added tail, meaning the later tails are closer to the beginning tail in speed.
# Also I thought the drawing was a nice touch.
#
# Two clicking events: Start() and then a click can call GameOver(); see Click_Checker()
#-------------------------------------------------------------------------------

import turtle
import random
import Tkinter
import sys
import time

##### FUNCTIONS ################################################################

# # # # Key press functions # # # #
def Up():
    """Changes snake direction to up"""
    snake.setheading(90)

def Down():
    """Changes snake direction to down"""
    snake.setheading(270)

def Left():
    """Changes snake direction to left"""
    snake.setheading(180)

def Right():
    """Changes snake direction to right"""
    snake.setheading(0)

def Quit():
    """Quits the program by closing window and then exiting using sys."""
    wn.bye()
    sys.exit()

# # # # Game running functions # # # #

def GamePlay(snake, food, foodCount, tList):
    """Runs the entire game by using all the functions that need to be checked every time the snake moves. Calls itself on a timer if user has not lost or won."""
    is_game_over = Is_Hit(snake, tList)                                         #Checks if user has hit walls/itself, stores in is_game_over
    (foodCount, tList) = Food_Tracker(snake, food, foodCount, tList)            #Checks if food is eaten, makes necessary changes if so, including new food and new tails
    snake.speed(Current_Speed(foodCount))
    tList = Move_Snake(snake, tList, foodCount)                                 #Moves snake and tails forward
    if is_game_over == True:                                                    #If the user did hit something...
        GameOver()                                                                  #Calls GameOver function
    elif foodCount >= 10:
        GameWon()
    else:                                                                       #Otherwise...
        wn.ontimer(GamePlay(snake, food, foodCount, tList), 1)                     #On the timer, calls itself again with updated parameters

def Start():
    """Activated when user presses space bar. Uses global variable start to start game."""
    global start
    global num_of_clicks
    num_of_clicks += 1
    start = True

def Click_Checker(x,y):
    """Checks how many times the screen has been clicked; no clicks means start, one means quit."""
    global num_of_clicks
    if num_of_clicks > 0:
        GameOver()
    else:
        Start()

def GameWon():
    """Game won! Displays game won and quits."""
    Display_Game_Won()
    time.sleep(2)
    Quit()

def GameOver():
    """Game over! Displays game over and quits."""
    Display_Game_Over()
    time.sleep(2)
    Quit()

# # # # Display functions # # # #

def Instructions():
    """Displays instructions"""
    display.color("white")
    display.setpos(0,170)
    display.write("Play snake!",move=False,align='center',font=("Arial",30,("bold","normal")))
    display.setpos(0,140)
    display.write("Collect food and don't hit walls or your tail.",move=False,align='center',font=("Arial",12,("bold","normal")))
    display.setpos(0,100)
    display.write("Get 10 food items to win!",move=False,align='center',font=("Arial",12,("bold","normal")))
    display.setpos(0,-100)
    display.write('Click the screen to begin!',move=False,align='center',font=("Arial",12,("bold","normal")))
    display.setpos(0,-140)
    display.write('Use arrow keys to change direction, click the screen again to quit.',move=False,align='center',font=("Arial",10,("bold","normal")))

def Display_Score(foodCount):
    """Displays amount of food eaten"""
    display.setpos(-230,-230)
    display.write('Food eaten: '+str(foodCount),move=False,align='left',font=("Arial",12,("bold","normal")))

def Display_Game_Over():
    """Displays GAME OVER"""
    display.clear()
    display.setpos(0,0)
    display.write('GAME OVER',move=False,align='center',font=("Arial",50,("bold","normal")))

def Display_Game_Won():
    """Displays YOU WIN!"""
    display.clear()
    display.setpos(0,0)
    display.write('YOU WIN!',move=False,align='center',font=("Arial",50,("bold","normal")))

# # # # Food functions # # # #

def Is_Eaten(snake, food):
    """Checks if the snake and food turtles have overlapped--meaning that the snake ate the food. Returns True or False."""
    xdistance = snake.xcor() - food.xcor()                                      #Finds distance between the X values of the snake and the food
    ydistance = snake.ycor() - food.ycor()                                      #Finds the distance between the Y values of the snake and the food
    if abs(xdistance) <= 20 and abs(ydistance) <= 20:                           #If those distances are less than 20 pixels in either direction...
        return True                                                                 #It has been eaten, return True
    else:
        return False                                                                #Otherwise, it has not been eaten, return False


def Food_Tracker(snake, food, foodCount, tList):
    """If Is_Eaten returns True, adds it to total food eaten, calls Add_Tail, and resets the food turtle to a new location. Returns total food eaten."""
    if Is_Eaten(snake, food) == True:                                           #If food is eaten...
        foodCount += 1                                                              #Add it to the amount eaten
        display.clear()                                                             #Clears display
        Display_Score(foodCount)                                                    #Displays new total
        tList = Add_Tail(tList)                                                     #Add a tail!
        food.ht()
        food.setpos(random.randrange(-230,230), random.randrange(-230,230))         #Puts food in a new random location
        food.st()
    return (foodCount, tList)                                                   #Returns the amount of food eaten and the list of tails

# # # # Tail functions # # # #

def Add_Tail(tList):
    """Adds a tail turtle to tList (list of tails)."""
    tail = turtle.Turtle()
    tail.up()
    tail.color("plum")
    tail.shape("circle")
    tX = 0                  #Stores x of new tail
    tY = 0                  #Stores y of new tail

    #Set of if statements tells where to place the new tail relative to the position of the last tail (so that they are lined up)
    if tList[len(tList)-1].heading() == 90:     #If the tail before the new one was facing up...
        tX = tList[len(tList)-1].xcor()             #Give the new tail the same x coordinate
        tY = tList[len(tList)-1].ycor() - 20        #But put it 20 spaces below it
    if tList[len(tList)-1].heading() == 270:    #(And so on)
        tX = tList[len(tList)-1].xcor()
        tY = tList[len(tList)-1].ycor() + 20
    if tList[len(tList)-1].heading() == 180:
        tX = tList[len(tList)-1].xcor() + 20
        tY = tList[len(tList)-1].ycor()
    if tList[len(tList)-1].heading() == 0:
        tX = tList[len(tList)-1].xcor() - 20
        tY = tList[len(tList)-1].ycor()

    tail.setpos(tX,tY)  #Set this as the position of the tail
    tList.append(tail)  #Add it to the list
    return tList        #Return the list

def Move_Snake(snake, tList, foodCount):
    """Moves the given snake and tails (from given list) forward, then returns the changed list."""
    snakeX = snake.xcor()                                       #Saves snake x coordinate before it moves
    snakeY = snake.ycor()                                       #Saves snake y coordinate before it moves
    snake.forward(20)                                           #Moves
    tList = Update_Tails(snakeX, snakeY, tList, foodCount)      #Moves tails, returns updated tails
    return tList                                                #Returns tails

def Update_Tails(snakeX, snakeY, tList, foodCount):
    """Moves each tail forward to the position the tail in front of it last had. Provided coordinates are used to move the first tail. Returns changed tail list."""
    new_posList = []                            #Stores updated set of positions for each tail
    tX = 0                                      #Stores current tail's new x coordinate
    tY = 0                                      #Stores current tail's new y coordinate
    if len(tList) > 1:                          #If there is more than just the head...

        for t in range(len(tList)-1):               #For every tail in tList (ie, not including the head)...
            if t == 0:                                  #If it's the first tail,
                tX = snakeX                                 #Make its coordinates the same as the snake head's old ones
                tY = snakeY
            else:                                       #Otherwise,
                tX = tList[t].xcor()                        #Make its coordinates the same as the tail in front of its old ones
                tY = tList[t].ycor()
            new_posList.append((tX, tY))            #Adds the new set of coordinates to a list (Appends into new_posList[t+1])

        for t in range(len(tList)-1):               #For every tail in tList...
            tList[t+1].setpos(new_posList[t])           #Set its position to the corresponding updated position in new_posList
            tList[t+1].speed(Current_Speed(foodCount))  #Set its speed to the current speed based on foodCount

    return tList                                #Returns list of tails

def Current_Speed(foodCount):
    foodvsSpeed = {0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9, 9:10, 10:0} #Each # of food paired with appropriate speed, so that they can be matched below.
    speed = foodvsSpeed[foodCount]
    return speed


# # # # Running into things functions # # # #

def Is_Hit(snake, tList):
    """Checks if the snake has hit anything that would result in game over. Returns True or False."""
    hit = Has_Hit_Edges(snake)                      #Calls to see if snake has hit edges
    if hit == False:                                #If not...
        hit = Has_Hit_Tail(snake, tList)                #Has it hit its tails?
    return hit                                      #Returns whether it has hit anything or not


def Has_Hit_Edges(snake):
    """Checks if snake has hit the edges of the window/gone offscreen. Returns True or False."""
    if snake.xcor() >= 250 or snake.xcor() <=-250:      #If snake's x coordinates show it's offscreen
        return True                                         #Return True
    elif snake.ycor() >= 250 or snake.ycor() <=-250:    #If snake's y coordinates show it's offscreen
        return True                                         #Return True
    else:
        return False                                    #Otherwise, return False

def Has_Hit_Tail(snake, tList):
    """Checks if snake has hit any of its tails. Returns True or False."""
    xdistance = 0
    ydistance = 0
    for t in tList:                                             #For every turtle/tail in tList
        if t == snake:                                              #If that turtle is the same as snake, do nothing.
            continue
        else:                                                       #If it's a tail...
            xdistance = snake.xcor() - t.xcor()                         #Distance between tail and snake
            ydistance = snake.ycor() - t.ycor()
            if abs(xdistance) <= 15 and abs(ydistance) <= 15:           #If the distance is too close (touching)
                return True                                                 #Return True
    return False                                                #Else return False



##### SET UP BOARD AND GAME ####################################################

turtle.setup(500,500)                                                           #Change screensize for easy reference
wn = turtle.Screen()                                                            #Sets up screen
wn.bgcolor("black")                                                             #Background color

foodCount = 0                                                                   #Keeps track of how much food snake has eaten
tList = []                                                                      #List of "snake parts", the head and tails, as they get added

start = False                                                                   #For instructions to display at first
num_of_clicks = 0                                                               #How many times screen has been clicked
display = turtle.Turtle()                                                       #Turtle used to display text to user
display.ht()
display.up()

snake = turtle.Turtle()                                                         #Snake head turtle
snake.shapesize(2,1,1)                                                          #Makes it a bit wider than a normal arrow shape
snake.color("hot pink")                                                         #Snake head is hot pink, also leaves a fun hot pink trail
snake.speed(1)

tList.append(snake)                                                             #Adds snake head to list of snake parts, tList

food = turtle.Turtle()                                                          #Creates food turtle
food.ht()                                                                       #Hides food
food.up()
food.shape("square")                                                            #Food is for squares
food.color("light green")
food.setpos(random.randrange(-230,230), random.randrange(-230,230))             #Puts food in a random location on the screen
food.st()                                                                       #Show food

#Links keys to their designated functions
wn.onkey(Up, "Up")
wn.onkey(Down, "Down")
wn.onkey(Left, "Left")
wn.onkey(Right, "Right")
wn.onkey(GameOver, "q")

#Links clicks to their designated functions
wn.onclick(Click_Checker)


################################################################################
wn.listen()

while start == False:                                                           #Program will only have instructions until user presses space bar
    Instructions()

display.clear()                                                                 #Clears instructions
GamePlay(snake, food, foodCount, tList)                                         #Calls function that runs the game

Tkinter.mainloop()                                                              #Hooray, main loop

