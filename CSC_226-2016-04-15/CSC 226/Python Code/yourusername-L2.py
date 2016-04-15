######################################################################
# Author: Dr. Jan Pearce  ****** CHANGE THIS!! ******
# username: pearcej ****** CHANGE THIS!! *****
# Lab: L2
# Purpose: Add something here!!
#
#
######################################################################
# Acknowledgements:

#   Modified from code written by Dr. Jan Pearce
#   Original lab specifications modified from:
#   http://www.cs.uni.edu/~schafer/1140/assignments/pa9/index.htm
######################################################################
import sys
import doctest

def testit(did_pass):
    """ Print the result of a test. """
    # This function works correctly
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def all_nucleotide(sequence):
    '''checks that the string sequence provided is a valid string
    consisting only of the 4 nucleotides A, C, G, and T'''
    return True # Obviously, this should not always return True

def num_times(sequence, nucleotide):
    '''Returns count of how many times nucleotide is found in sequence.'''
    return 0 # Obviously, this should not always return 0

def complement_strand(sequence):
    '''returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs.'''
    return "" # Obviously, this should not always return ""

def mRNA(sequence):
    '''using the return from secondStrand(sequence) with each occurrence of the
    nucleotide T replaced with the nucleotide U'''
    return "" # Obviously, this should not always return ""

def amino_acid_translation(threecharseq):
    '''expects a three character string as a parameter and returns
    the corresponding single character AminoAcid'''
    # This funciton is already completed correctly
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
    if threecharseq in translator.keys():
        return translator[threecharseq]
    else:
        return "?"

def amino_acid(sequence):
    '''uses mRNA(sequence) and divides it into substrings of length 3,
    translates each nucleotide triple into it's corresponding Amino Acid
    using aminoAcidTranslation(threecharseq)'''
    return ""   # Obviously, this should not always return ""

testit(all_nucleotide("CGTAGGCAT")==True)
testit(all_nucleotide("CGTAFLCAT")==False)


# Be sure to change the filename of this file to your yourusernames-L2.py
