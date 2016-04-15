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

JOhn = ('45612312312','3','435123312312','4')
(BC1,C1,BC2,C2) = JOhn

def barcodetogether(A):
    Listofbarcodes = []
    index = 0
    while int(index) < len(A):
        if index % 2 == 0:
            List = ('')
            P1 = A[index]
            indexA = index + 1
            P2 = A[indexA]
            List += str(P1) + str(P2)
            Listofbarcodes.append(List)
        index += 1
    return Listofbarcodes

print barcodetogether(JOhn)