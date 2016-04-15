#-------- -----------------------------------------------------------------------
# Name:        John Hellrung & Kenan Shelton
# UserName:    hellrungj & sheltonk
# Purpose:
#
#
#
# Created:     28/03/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string

file_name = raw_input("file name")
# look for file name "upc-input1.txt, upc-input2.txt"

with open(file_name,"r") as file_name_reader:
    file_name_string=file_name_reader.read()
def file_split(file_name_string):
    #file_name_string[0:12]
    Index = 0
    End_index = 12
    for i in file_name_string:
        A = file_name_string[Index:End_index]
        Index += 12
        End_index += 12
    return A

print file_split(file_name_string)

