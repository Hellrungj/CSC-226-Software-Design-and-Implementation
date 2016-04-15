#-------------------------------------------------------------------------------
# Name:        John Hellrung & Xhafer Rama
# Purpose:      Inclass Test
#
# Author:      hellrungj & ramax
#
# Created:     21/02/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Example = '''<br> JOHN HELLRUNG & XHAFER RAMA and <img src="filename"  ...>afsdgajfh'''
output = ""

A = 0
while len(Example) > A:
    while str(Example[A]) == '<':
        output = output + Example[A]
        A = int(A) + 1
        if str(Example[A]) == 'b' or str(Example[A]) == 'm' or str(Example[A]) == 'i' or str(Example[A]) == 'h':
            output = output + Example[A]
            A = int(A) + 1
            if str(Example[A]) == str('r') or str(Example[A]) == str('e') or str(Example[A]) == ('m'):
                output = output + Example[A]
                A = int(A) + 1
                if str(Example[A]) == str('g') or str(Example[A]) == str('a'):
                    output = output + Example[A]
                    A = int(A) + 1
                    if str(Example[A]) == str('s'):
                        output = output + Example[A]
                        A = int(A) + 1
                        if str(Example[A]) == str('r'):
                            output = output + Example[A]
                            A = int(A) + 1
                            if str(Example[A]) == str('c'):
                                output = output + Example[A]
                                A = int(A) + 1
                                if str(Example[A]) == str('='):
                                    output = output + Example[A]
                                    A = int(A) + 1
                                    if str(Example[A]) == str('"'):
                                        output = output + Example[A]
                                        A = int(A) + 1
                                        if str(Example[A]) == str('f'):
                                            output = output + Example[A]
                                            A = int(A) + 1
                                            if str(Example[A]) == str('i'):
                                                output = output + Example[A]
                                                A = int(A) + 1
                                                if str(Example[A]) == str('l'):
                                                    output = output + Example[A]
                                                    A = int(A) + 1
                                                    if str(Example[A]) == str('e'):
                                                        output = output + Example[A]
                                                        A = int(A) + 1
                                                        if str(Example[A]) == str('n'):
                                                            output = output + Example[A]
                                                            A = int(A) + 1
                                                            if str(Example[A]) == str('a'):
                                                                output = output + Example[A]
                                                                A = int(A) + 1
                                                                if str(Example[A]) == str('m'):
                                                                    output = output + Example[A]
                                                                    A = int(A) + 1
                                                                    if str(Example[A]) == str('e'):
                                                                        output = output + Example[A]
                                                                        A = int(A) + 1
                                                                        if str(Example[A]) == str('"'):
                                                                            output = output + Example[A]
                                                                            A = int(A) + 1
                                                                        elif str(Example[A]) == str('>'):
                                                                                output = output + " />"
                                                                                A = int(A) + 1
                                                                        else:
                                                                            output = output + Example[A]
                                                                            A = int(A) + 1
                                                                    else:
                                                                        output = output + Example[A]
                                                                        A = int(A) + 1
                                                                else:
                                                                    output = output + Example[A]
                                                                    A = int(A) + 1
                                                            else:
                                                                output = output + Example[A]
                                                                A = int(A) + 1
                                                        else:
                                                            output = output + Example[A]
                                                            A = int(A) + 1
                                                    else:
                                                        output = output + Example[A]
                                                        A = int(A) + 1
                                                else:
                                                    output = output + Example[A]
                                                    A = int(A) + 1
                                            else:
                                                output = output + Example[A]
                                                A = int(A) + 1
                                        else:
                                            output = output + Example[A]
                                            A = int(A) + 1
                                    else:
                                        output = output + Example[A]
                                        A = int(A) + 1
                                else:
                                    output = output + Example[A]
                                    A = int(A) + 1
                            else:
                                output = output + Example[A]
                                A = int(A) + 1
                        else:
                            output = output + Example[A]
                            A = int(A) + 1
                    else:
                        output = output + Example[A]
                        A = int(A) + 1

                elif str(Example[A]) == str('>'):
                        output = output + " />"
                        A = int(A) + 1
                else:
                    output = output + Example[A]
                    A = int(A) + 1
            else:
                output = output + Example[A]
                A = int(A) + 1
        elif str(Example[A]) == str('>'):
            output = output + " />"
            A = int(A) + 1
        else:
            output = output + Example[A]
            A = int(A) + 1
    else:
        output = output + Example[A]
        A = int(A) + 1

print(output)