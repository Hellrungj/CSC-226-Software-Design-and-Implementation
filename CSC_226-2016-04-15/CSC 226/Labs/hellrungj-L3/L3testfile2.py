#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      hellrungj
#
# Created:     05/04/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle

JOhn = ('45612312312','3','435123312312','4')
(BC1,C1,BC2,C2) = JOhn

CB = str(BC1) + str(C1)
print CB
PL = CB[0:6]
PR = CB[6:12]
PartLeft = {0:'0001101',1:'0011001',2:'0010011',3:'0111101',4:'0100011',5:'0110001',6:'0101111',7:'0111011',8:'0110111',9:'0001011'}
PartRight = {0:'1110010',1:'1100110',2:'1101100',3:'1000010',4:'1011100',5:'1001110',6:'1010000',7:'1000100',8:'1001000',9:'1110100'}
PLdecoded = ('')
PRdecoded = ('')

for A in PL:
    number = int(A)
    PLdecoded += PartLeft[number]
print PLdecoded
for A in PR:
    number = int(A)
    PRdecoded += PartRight[number]
BarcodeDecoded = str(PLdecoded) + str(PRdecoded)
print PRdecoded


wn=turtle.Screen()
barcode=turtle.Turtle()
barcode.color("black")

for oneorzero in BarcodeDecoded:
    if int(oneorzero) == 1:
        barcode.right(90)
        barcode.forward(10)
        barcode.right(180)
        barcode.forward(10)
        barcode.right(90)
    else:
        barcode.forward(1)




