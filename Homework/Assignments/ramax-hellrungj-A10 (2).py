#-------------------------------------------------------------------------------
# Names:         John Hellrung & Xhafer Rama
# Roles:         Driver: John
#                Navigator: Xhafer
# Purpose:      Finding the HTML mistakes and fixing them; modernizing
#               the HTML using Python coding
#
# Author:      hellrungj & ramax
#
# Created:     21/02/2014
# ------------------------------------------------------------------------------
# Acknowledgements:
#   1)http://cs.berea.edu/courses/csc226/tasks/a10.xhtml.html
#   2)http://infohound.net/tidy/
#   3) Ccomputer Science Lab
#-------------------------------------------------------------------------------
#It was a very challenging assignment. We changed our code three times until we
# got it to work. Our previous codes were smaller and more condense which allowed room
# for errors however making a longer code helped us go through each of the problems
# we have to fix for our html.


Example = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html;charset=UTF-8" http-equiv="Content-Type">
<title>Basic Web Page</title>
</head>
<body>
<h3>A Basic Web Page</h3>

<p>A basic web page looks something like this. It might have
images like:<br>

<img style="width: 66px; height: 44px;" alt="WC3 image" src="wc3.gif">
<br>
And it might have a line like:
</p>

<hr>
<p>Be sure to "view source" of this page.</p>
</body>
</html>'''


output = ''
A = 0

#This was a function we used but we dont need it anymore
#def html(Example, A, output): #We define our function as html and give three parameters
    #S = output
    #while Example[A] != '>':
        #S += Example[A]
        #A = A + 1 # Note that the A will keep count of the words
    #else:
        #S += " />" # It will add the "/>" wherever it encounters a problem
        #A = A + 1
        #return S


while len(Example) > A: # Within this while loop, we have four main if functions to solve the 4 problems the HTML has
    if Example[A] == '<':
        output += Example[A]
        A = A + 1 #This will keep count for words

        if Example[A] == 'b': #While it is looping, when it comes to a "b" and finds it is going to put " />" at the end
            output += Example[A]
            A = A + 1
            while Example[A] != '>':
                output += Example[A]
                A = A + 1
            else:
                output += " />"
                A = A + 1

        if Example[A] == 'h': #While it is looping, when it comes to a "h" and finds it is going to put " />" at the end
            output += Example[A]
            A = A + 1
            while Example[A] != '>':
                output += Example[A]
                A = A + 1
            else:
                output += " />"
                A = A + 1

        if Example[A] == 'i': #While it is looping, when it comes to the word image, in this case when it reads, i-m-g,it is going to put " />" at the end
            output += Example[A]
            A = A + 1
            if Example[A] == 'm':
                output += Example[A]
                A = A + 1
                if Example[A] == 'g':
                    output += Example[A]
                    A = A + 1
                    while Example[A] != '>':
                        output += Example[A]
                        A = A + 1
                    else:
                        output += " />"
                        A = A + 1


        if Example[A] == 'm': # In this case it is supposed to look for the word "meta" and so when it comes to meta, it will fix the mistake by placing "/>"
            output += Example[A]
            A = A + 1
            if Example[A] == 'e':
                output += Example[A]
                A = A + 1
                if Example[A] == 't':
                    output += Example[A]
                    A = A + 1
                    while Example[A] != '>':
                        output += Example[A]
                        A = A + 1
                    else:
                        output += " />"
                        A = A + 1

    else:
        output += Example[A]
        A = A + 1

print(output) # Prints the corrected html