#-------------------------------------------------------------------------------
# Name:        John Hellrung & Xhafer Rama
# Purpose:      Practice more breaking a larger problem down into smaller pieces using functions
#               Gain practice using strings
#               Introduce concepts about DNA
#               This lab can be completed in a pair using pair programming or individually.
#
# Usernames:      hellrungj & ramax
# Driver:       hellrungj
# Navigator:    ramax
# Created:     26/02/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Acknowledgements:
#1.)http://cs.berea.edu/courses/csc226/tasks/L2.DNA.html
#2.)http://cs.berea.edu/courses/csc226/tasks/craps-dice-rolls.py
#3.)http://cs.berea.edu/courses/csc226/tasks/yourusername-L2.py
#-------------------------------------------------------------------------------
import time

def all_nudeotide(sequence):
    '''checks that the string sequence provided is a valid string
    consisting only of the 4 nucleotides A, C, G, and T'''
    S = True  # S is equal to true, so that if any character proven false, it will return false
    for sequence in sequence: # loops for every character in sequence.
        if sequence == "T" or sequence == "C" or sequence == "A" or sequence == "G": #Tests to see if the nudeotide is true and if it is not than it returns false
            pass
        else:
            S = False
    return S
#if the function finds the senqunce contants T or C or A OR G the function returns true but if it doesn't it returns false.

def num_times(sequence):
    '''Returns count of how many times nucleotide is found in sequence.'''
    nucleotide = len(sequence)//3   #Set nucleotide to the length fo sequence divded by three
    return nucleotide               #returns the nucleotide varable

def complement_strand(sequence):
    '''returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs.'''
    output = ''
    for sequence in sequence:   # loops for each character in sequence
        if sequence == "A": # if sequence is equal to "A" add 'T' to the output
            output += 'T'
        if sequence == "T": # if sequence is equal to "T" add 'A' to the output
            output += 'A'
        if sequence == "C": # if sequence is equal to "C" add 'G' to the output
            output += 'G'
        if sequence == "G": # if sequence is equal to "G" add 'C' to the output
            output += 'C'
    return output # Returns the fixed code

def mRNA(sequence):
    '''using the return from complement_strand(sequence) with each occurrence of the
    nucleotide T replaced with the nucleotide U'''
    output = ''         #Makes a output list for mRNA(sequence)
    for sequence in sequence:   #Loops the sequence for each character in the list of sequence
        if sequence == 'T':     #if sequence is equal to 'T' add a 'U' to output but if it does not equal to 'T' then the code just add the character to output
            output += 'U'
        else:
            output += sequence
    return output       #Returns the fixed code
                                                        #*********!!!!!!!!Important!!!!!!!*******
def amino_acid_translation(mRNAcode,numtimes):          #We combined the amino_acid_translation fuction and amino_acid function.
    '''expects a three character string as a parameter and returns
    the corresponding single character AminoAcid'''
    list = ""   #list to make a output for the amino acids
    i = 0       #i is start index varable
    e = 3       #e is an end index varable
    a = 0       #a for counting how times the code translate the nucleotide sequences
    while a != numtimes:    #while the (a or the count) is not equal numtimes(Is the number of nucleotide).
        g = mRNAcode[i:e]   #mRNAcode[i:e] is an index cuting for the nucleotide
        i = i + 3   #Add 3 to i
        e = e + 3   #Add 3 to e
        a = a + 1   #Add 1 to a
        print(g)
        '''expects a three character string as a parameter and returns
        the corresponding single character AminoAcid'''
        translator = { "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A",
                            "AGA":"R", "AGG":"R", "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R",
                            "GAC":"D", "GAU":"D",
                            "AAC":"N", "AAU":"N",
                            "UGC":"C", "UGU":"C",
                            "GAA":"E", "GAG":"E",
                            "CAA":"Q", "CAG":"Q",
                            "GGA":"G", "GGC":"G", "GGU":"G", "GGG":"G",
                            "CAC":"H", "CAU":"H",
                            "AUA":"I", "AUC":"I", "AUU":"I",
                            "UUA":"L", "UUG":"L", "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L",
                            "AAA":"K", "AAG":"K",
                            "AUG":"M",
                            "UUC":"F", "UUU":"F",
                            "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P",
                            "AGC":"S", "AGU":"S", "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S",
                            "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T",
                            "UGG":"W",
                            "UAC":"Y", "UAU":"Y",
                            "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V",
                            "UAA":"*", "UAG":"*", "UGA":"*" }
        if g in translator.keys():  #translates the nucleotide into amino acids
            print translator[g]     #prints translation for the nucleotide
            list += translator[g]   #Collects each transltion and when add them to a list
        else:
            print "?"
    print("")

    j = ''  #j is a varable for a list
    b = 0   #b is a starting varable for a index
    z = 3   #z is a ending varable for a index
    I = 0   #I is a varable that keeps keep of how times the loop is ran
    Number = len(list)//3   #Divides the length of the list by three and sets the value to the varable named Namber
    print("Here are the amino acids:")
    if Number == 0: #if that prints the amino acids when Numder equal 0
        for list in list:
            j += list
        return j
    else:
        while I < Number:       #while I(a varable for the # of times ran through the loop) less than Number(The value of the lenght of the list divide by three)
            j += list[b:z]  #list[b:z] is index for the amino acids
            j += " "    #Adds a space
            b += 3      #Add 3 to the varable b
            z += 3      #Add 3 to the varable z
            I += 1      #Add 1 to the varable I
        return j        #Returns the a varable like (AGH AGH AHJ)

print("Welcome to GENE_LAB.")
print("")
sequence = raw_input("Make a sequence with only these charcter C,A,T,G(Type is all CAPs)")  # The code asks for a Nucleotide from the user
print("The sequence that you inputed is " + str(sequence) + '.')
if all_nudeotide(sequence) == True:     #test to see if function is true and if is then run the following code but if not shoot to the end of the code
    time.sleep(1)
    print("They are " + str(num_times(sequence)) + " nucleotides in your sequence.")
    time.sleep(1)
    print("The suplement strand of your sequence is " +  str(complement_strand(sequence)) + ".")
    time.sleep(1)
    sequence = complement_strand(sequence)
    time.sleep(1)
    print("The mRNA sequence of your sequence is " + str(mRNA(sequence)) + ".")
    time.sleep(1)
    mRNAcode = mRNA(sequence)
    time.sleep(1)
    numtimes = num_times(sequence)
    time.sleep(1)
    print("")
    print("Here are now your amino acids for your translated squence.")
    time.sleep(1)
    print amino_acid_translation(mRNAcode,numtimes)
    print("")
    time.sleep(1)
    print("Thank you and have a nice day.")
    time.sleep(10)
else:
    print("Try again, you did not input the right characters for the sequence.")