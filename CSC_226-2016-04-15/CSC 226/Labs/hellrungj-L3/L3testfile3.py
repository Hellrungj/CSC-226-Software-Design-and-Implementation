#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      hellrungj
#
# Created:     05/04/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle

John = ('123456789012', '102938475610')

def Dictionary(A):
    """Decodeds the Bracode into Binart Code"""
    BarcodeDecodedList = []
    for i in A:
        BarcodeC = str(i)
        PL = BarcodeC[0:6]
        PR = BarcodeC[6:12]
        PartLeft = {0:'0001101',1:'0011001',2:'0010011',3:'0111101',4:'0100011',5:'0110001',6:'0101111',7:'0111011',8:'0110111',9:'0001011'}
        PartRight = {0:'1110010',1:'1100110',2:'1101100',3:'1000010',4:'1011100',5:'1001110',6:'1010000',7:'1000100',8:'1001000',9:'1110100'}
        PLdecoded = ('')
        PRdecoded = ('')
        for A in PL:
            number = int(A)
            PLdecoded += str(PartLeft[number])
        for A in PR:
            number = int(A)
            PRdecoded += str(PartRight[number])
        BarcodeDecoded = str(PLdecoded) + str(PRdecoded)
        BarcodeDecodedList.append(BarcodeDecoded)
    print BarcodeDecodedList
    return BarcodeDecodedList

#Center is 01010
#Guard is 101

def printturtle(A):
    wn=turtle.Screen()
    barcode=turtle.Turtle()
    barcode.color("black")
    barcode.pensize(2)
    JohnH = []
    for index in A:
        Guard = '101'
        Center = '01010'
        LeftSide = index[0:42]
        RightSide = index[42:84]
        JohnH.append(Guard)
        JohnH.append(LeftSide)
        JohnH.append(Center)
        JohnH.append(RightSide)
        JohnH.append(Guard)
##        index1 =
    index1 = 0
    for index in JohnH:
        #index variable is the element
        if int(index1) % 2 == 0:
            for a in JohnH[index1]:
                if int(a) == 1:
                    barcode.right(90)
                    barcode.forward(70)
                    barcode.right(180)
                    barcode.forward(70)
                    barcode.right(90)
                    barcode.forward(4)
                else:
                    barcode.forward(2)
        else:
            for a in JohnH[index1]:
                if int(a) == 1:
                    barcode.right(90)
                    barcode.forward(50)
                    barcode.right(180)
                    barcode.forward(50)
                    barcode.right(90)
                    barcode.forward(2)
                else:
                    barcode.forward(2)
        index1 += 1
##        for A in index:
##            #A is character of that element
##            print A
##        print index
##        print "----------------------------------------------------------------"
##        for a in index:
##            if index1 == 5:
##                index1 = 0
##            else:
##                index1 += 1
##                if int(index1) == 1 or int(index1) == 3 or int(index) == 5:
##
##
##        barcode.pensize(6)
##        barcode.forward(4)
##        barcode.left(90)
##        barcode.forward(50)
##        barcode.backward(150)
##        barcode.forward(100)
##        barcode.right(90)
##        barcode.forward(4)
##        barcode.pensize(2)
##        if int(index1) < 5:
##            index1 += 1
##        else:
##            index1 = 0

##        print(i[0:3] + ' ' + i[0:43] + ' ' + i[43:48] + ' ' + i[48:91] + ' ' + i[91:94])
##        print(str(len(i[0:3])) + ' ' + str(len(i[0:43])) + ' ' + str(len(i[43:48])) + ' ' + str(len(i[48:91])) + ' ' + str(len(i[91:94])))
        # the size of the length of the sting will be 95 characters long

##            index = 0
##            if index == 0 or index == 1 or index == 2  or index == 46 or index == 47 or index == 48 or index == 51 or index == 52 or index == 91 or index == 92 or index == 93 or index == 94:
####                a = str(index) + ' ' + str(oneorzero)
####                JohnH.append(a)

##            if int(oneorzero) == 1:
##                p = str(index) + ' ' + str(oneorzero)
##                JohnH.append(p)

##            else:
##
##            print JohnH
##            print "-------------------------------------------------------------------------------------------------------------------------------------------- "

'''Get the turtle part to work and then add a for loop with in a for loop to make the function work with muti barcodes.
    to do this, I will need to make the turtle move 2 away from the last barcode.'''

##for i in John:
##    Dictionary(i)
printturtle(Dictionary(John))
