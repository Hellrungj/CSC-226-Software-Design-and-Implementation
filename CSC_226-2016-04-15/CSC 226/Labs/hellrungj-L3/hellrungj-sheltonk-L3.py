#-------- -----------------------------------------------------------------------
# Name:        John Hellrung & Kenan Shelton
# UserName:    hellrungj & sheltonk
# Purpose: To make a barcode and learning how coded more efficly.
#
#
#
# Created:     28/03/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Import Zone:
import turtle

#-------------------------------------------------------------------------------
#Function Zone:

def barcode_split (file_name):
    """ This function is for opening the file and put each line into a list as
    element"""
    barcodelines = [] #Creates a turple for storing the barcode of each line in the file
    lines= open(file_name, "r") #opens the file based on file's filename
    while True: #a while loop that check to see if there is next line
        theline = lines.readline () # if there is a line then it read that line and store it as value in varable named theline
        if len(theline) == 0: #if the varable named theline is a length is equal to 0 then break out of the while loop
            break
        theline = theline.replace ('\n','') #This line replace all "\n" with a space in the string stored in the varable named theline
        DBars = theline[1:12] #This line slice the line read to make it 11 characters long.
        Modulo_Check_Character = theline[12:13] # This line slice just the end of the line read
        barcodelines.append(DBars) # Then this line appends the varable named Dbars to the turple named barcodelines
        barcodelines.append(Modulo_Check_Character) # Then this line appends the varable named Modulo_Check_Character to the turple named barcodelines
    return barcodelines

def trueORfalse(turple_of_barcode):
    """Test to see if the barcodes read from the file are true or false"""
    TRUEORFALSE = []
    A = 0
    B = 0
    index = 0
    while int(index) < len(turple_of_barcode):
        if index % 2 == 0:
            Barcode = str(turple_of_barcode[index])
        else:
            CheckNumber = str(turple_of_barcode[index])
            Even = 0 #A varable for even#s
            Odd = 0 #A varable for odd#s
            index2 = 0 #A varable to index
            while int(index2) < len(Barcode): # a while so that the code does not error message
                if index2 % 2 == 0: # an if statement that finds the second, fourth, sixth, and eigth number in the string
                    Odd += int(Barcode[index2]) # stores the sum of the odd elements
                else:
                    Even += int(Barcode[index2]) # stores the sun of the even elements
                index2 += 1 # add one to the index
            Odd2 = Odd * 3 #Odd2 is a varable for mutipling the odd numbers by 3
            Total1 = Odd2 + Even #Adds the total sum for even numbers and odds numbers
            Total2 = Total1 % 10 # find the remainer for the first total
            Total3 = 10 - int(Total2) # subtracts 10 by the second total
            if int(Total3) == int(CheckNumber): # an if statement that take the total and compairs it to the value of the Check
                print str(CheckNumber)+ ' ' + str(Total3) + 'True' # if the compair is true, then print true, if not print false.
                T = "True"
                TRUEORFALSE.append(T)
            else:
                print str(CheckNumber) + ' ' + str(Total3) + 'False'
                F = "False"
                TRUEORFALSE.append(F)
        index += 1
    return TRUEORFALSE

def barcodetogether(A):
    """Take all the split parts of the barcodes and puts them togther"""
    Listofbarcodes = []
    index = 0
    while int(index) < len(A): #loops untill the length of the is eqaul
        if index % 2 == 0: #only run the following code it the index has a remember of zero
            List = ('')
            P1 = A[index]
            indexA = index + 1
            P2 = A[indexA]
            List += str(P1) + str(P2)
            Listofbarcodes.append(List) #make the add varables into a turple
        index += 1
    return Listofbarcodes

def Dictionary(A):
    """Decodeds the Bracode into Binart Code"""
    BarcodeDecodedList = [] #make a turple for later
    for i in A: #a for loop that allow the function to run throuht all value
        BarcodeC = str(i)
        PL = BarcodeC[0:6] #slicing half of the string from the function named ""
        PR = BarcodeC[6:12]
        PartLeft = {0:'0001101',1:'0011001',2:'0010011',3:'0111101',4:'0100011',5:'0110001',6:'0101111',7:'0111011',8:'0110111',9:'0001011'} # made a dictionary for the lift of the barcode
        PartRight = {0:'1110010',1:'1100110',2:'1101100',3:'1000010',4:'1011100',5:'1001110',6:'1010000',7:'1000100',8:'1001000',9:'1110100'} # made a dictionary for the right of the barcode
        PLdecoded = ('')
        PRdecoded = ('')
        for A in PL: #make a string of convered barcode information for left of the barcode
            number = int(A)
            PLdecoded += str(PartLeft[number])
        for A in PR: #make a string of convered barcode information for right of the barcode
            number = int(A)
            PRdecoded += str(PartRight[number])
        BarcodeDecoded = str(PLdecoded) + str(PRdecoded)
        BarcodeDecodedList.append(BarcodeDecoded)
    return BarcodeDecodedList

def checkiffalse(B, C):
    """Prints all barcodes and Nonbarcodes but for Nonbarcodes the screen prints an error message saying 'Error: This barcode is not acceptable (Check function trueORfalse)'"""
    barcode=turtle.Turtle() # set up for the turtle named barcode
    wn=turtle.Screen()
    barcode.hideturtle
    barcode.speed(0)
    index = 0
    X = -675 # fin the X and Y for the codnets in the turtle sceern
    Y = 320
    for part in B: # "part" a variable and set it for each elements of the turlpe from function
        print part
        if part == 'True': # if true do the following
            Binary = C[index]
            print len(C[index])
            printturtle(Binary,barcode,X,Y)
            barcode.pensize(6)
            barcode.penup()
            barcode.forward(10)
            barcode.pendown()
            barcode.left(90)
            barcode.forward(50)
            barcode.backward(150)
            barcode.forward(100)
            barcode.right(90)
            barcode.penup()
            barcode.forward(10)
            barcode.pendown()
            barcode.pensize(2)
        else: # if false do the following
            barcode.write("Error:This barcode is not acceptable")
            barcode.pensize(6)
            barcode.penup()
            barcode.forward(200)
            barcode.pendown()
            barcode.left(90)
            barcode.forward(50)
            barcode.backward(150)
            barcode.forward(100)
            barcode.right(90)
            barcode.penup()
            barcode.forward(10)
            barcode.pendown()
            barcode.pensize(2)
        if index == 3 or index == 7: #the four barcode move to th ebarcode to the line
            Y = int(Y) - 200
            X = -675
        else: #else move the barcode to right
            X += 210
        index += 1

def printturtle(A, barcode, X, Y):
    """Prints a barcode """
    barcode.color("black") #set for the turtle named barcode
    barcode.pensize(2)
    barcode.penup()
    barcode.setposition(X, Y)
    barcode.pendown()
    barcode.hideturtle
    Barcode = []
    Guard = '101'
    Center = '01010'
    LeftSide = A[0:42]
    RightSide = A[42:84]
    Barcode.append(Guard)
    Barcode.append(LeftSide)
    Barcode.append(Center)
    Barcode.append(RightSide)
    Barcode.append(Guard)
    Barcode.append('')
    index1 = 0
    print JohnH
    while index1 < len(Barcode): #a while loop and says if the length of JohnH
        if int(index1) % 2 == 0: # make the code only print guard and center bars
            for a in JohnH[index1]: #makes the barcodes for guard and manfure code and center bars
                if int(a) == 1:
                    barcode.right(90)
                    barcode.forward(70)
                    barcode.right(180)
                    barcode.forward(70)
                    barcode.right(90)
                    barcode.penup()
                    barcode.forward(2)
                    barcode.pendown()
                else:
                    barcode.penup()
                    barcode.forward(2)
                    barcode.pendown()
        else:
            for a in JohnH[index1]: #makes the barcodes for product and manfure code
                if int(a) == 1:
                    barcode.right(90)
                    barcode.forward(50)
                    barcode.right(180)
                    barcode.forward(50)
                    barcode.right(90)
                    barcode.penup()
                    barcode.forward(2)
                    barcode.pendown()
                else:
                    barcode.penup()
                    barcode.forward(2)
                    barcode.pendown()
        index1 += 1
#-------------------------------------------------------------------------------
#Calling Zone:

file_name = raw_input("file name") #Asks the user which file they should use.
#look for file name "upc-input1.txt"
checkiffalse(trueORfalse(barcode_split(file_name)),Dictionary(barcodetogether(barcode_split(file_name))))