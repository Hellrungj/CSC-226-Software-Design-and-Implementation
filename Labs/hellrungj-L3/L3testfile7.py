#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hellrungj
#
# Created:     06/04/2014
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




A = Dictionary(John)
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
    JohnH.append('')
    index1 = 0
print JohnH
while index1 < len(JohnH):
    if int(index1) % 2 == 0:
        for a in JohnH[index1]:
            if int(a) == 1:
                print str(a) + ' ' + '1' + '-----------------------------------'
                barcode.right(90)
                barcode.forward(70)
                barcode.right(180)
                barcode.forward(70)
                barcode.right(90)
                barcode.penup()
                barcode.forward(2)
                barcode.pendown()
            else:
                print str(a) + ' ' + '2' + '-----------------------------------'
                barcode.penup()
                barcode.forward(2)
                barcode.pendown()
    else:
        for a in JohnH[index1]:
            if int(a) == 1:
                print str(a) + ' ' + '3'
                barcode.right(90)
                barcode.forward(50)
                barcode.right(180)
                barcode.forward(50)
                barcode.right(90)
                barcode.penup()
                barcode.forward(2)
                barcode.pendown()
            else:
                print str(a) + ' ' + '4'
                barcode.penup()
                barcode.forward(2)
                barcode.pendown()
    index1 += 1
    if int(index1) % 6 == 0:
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