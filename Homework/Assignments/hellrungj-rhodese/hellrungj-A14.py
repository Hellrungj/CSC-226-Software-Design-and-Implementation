#-------------------------------------------------------------------------------
# Name:        John Hellrung & Eric
# Username:    hellrungj
# Purpose:     We would like you to create a program that would take a cryptogram from a file called "cryptogram.txt"
#              and do some frequency analysis on it. Using the original distribution of the letters from another file
#              called "orig_dist.txt", your program will decrypt the text and output the decoded text to an output file.
#
# Created:     19/03/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
filename = "orig_dist.txt"

def OpenFileConvertion(filename):
    '''Takes the parameter filename with the filename we open up the file "orig_dist.txt"
    and converts the contents into a letter frequency list. Then, the function returns
    a list of the frequency list.'''
    in_list = ''
    My_File = file(filename, "r")
    My_File = My_File.readline()
    in_list = in_list + str(My_File)
    for i in in_list:
        i

    return in_list


print OpenFileConvertion(filename)













