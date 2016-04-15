#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hellrungj
#
# Created:     05/04/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
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

def MAth(Barcode, CheckNumber):
    """This function does all the math for the numbers in the barcode string expect for check number and then compair that value by the check to see if the barcode in truely a barcode"""
    Even = 0 #A varable for even#s
    Odd = 0 #A varable for odd#s
    index = 0 #A varable to index
    while int(index) < len(Barcode): # a while so that the code does not error message
        if index % 2 == 0: # an if statement that finds the second, fourth, sixth, and eigth number in the string
            Odd += int(Barcode[index]) # stores the sum of the even numbers
        else:
            Even += int(Barcode[index]) # stores the sun of the odd numbers
        index += 1 # add one to the index
    Odd2 = Odd * 3 #B2 is a varable for mutipling the odd numbers by 3
    Total1 = Odd2 + Even #Adds the total sum for even numbers and odds numbers
    Total2 = Total1 % 10 # find the remainer for the first total
    Total3 = 10 - int(Total2) # subtracts 10 by the second total
    if int(Total3) == int(CheckNumber): # an if statement that take the total and compairs it to the value of the Check
        print str(CheckNumber)+ ' ' + str(Total3) + 'True' # if the compair is true, then print true, if not print false.
        TRUEORFALSE = True
    else:
        print str(CheckNumber) + ' ' + str(Total3) + 'False'
        TRUEORFALSE = False
    return TRUEORFALSE

#-------------------------------------------------------------------------------

file_name = raw_input("file name")
# look for file name "upc-input1.txt, upc-input2.txt"

A = barcode_split(file_name)
print A
(Barcode1,Check1,Barcode2,Check2,Barcode3,Check3,Barcode4,Check4,Barcode5,Check5,Barcode6,Check6,Barcode7,Check7,Barcode8,Check8,Barcode9,Check9,Barcode10,Check10,Barcode11,Check11,Barcode12,Check12) = A

MAth(Barcode1, Check1)