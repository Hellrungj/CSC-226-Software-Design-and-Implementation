#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hellrungj
#
# Created:     31/03/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import string

file_name = raw_input("file name")
# look for file name "upc-input1.txt, upc-input2.txt"

def barcode_split (file_name):
    """ This function is for opening the file and put each line into a list as
    element"""
    barcodelines = []
    lines= open(file_name, "r")
    while True:
        tepstring = lines.readline ()
        tepstring = tepstring.replace ('\n','')
        barcodelines.append(tepstring)
        if len(tepstring) == 0:
            break
    for i in barcode_split(file_name):
        '''Take the code that has been slied and run a Modulo Check Character'''
        tepstring=i[1:11] #we need to take the string and run them through your Modulo Check Character.
        print tepstring
##    while True:
##        tepstring = lines.readline ()
##        tepstring = theline.replace ('\n','')
##        barcodelines.append(tepstring)
##        if len(tepstring) == 0:
##            break
    return barcodelines


print barcode_split (file_name) #Ask TA about the \n at the end.

