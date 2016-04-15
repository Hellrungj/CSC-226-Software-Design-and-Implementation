######################################################################
# Author: John hellrung(Driver) and Ross Miller(Navigator)
# username: hellrungj and millerro

# Assignment: A15
# Purpose: To improve the module ppm
######################################################################
# Acknowledgements:
    # Ben Stephenson: http://pages.cpsc.ucalgary.ca/~jacobs/Courses/cpsc217/W10/code/Topic7/ppm.py
    # working from a class: http://bytes.com/topic/python/answers/520360-trouble-displaying-image-tkinter

# You need to acknowledge having modifed this code and all other code you modify or use for assitance.
#   To do so, you will indicate something like:
#   Mopidied from code written by Dr. Jan Pearce
#   Original code downloaded from:
#   http://cs.berea.edu/csc226/tasks/yourusername-A15.py and
#   http://cs.berea.edu/csc226/tasks/ppm.py
######################################################################

from ppm import *
# Be sure you work with a single ppm object at a time

# The following interaction is just for testing.  You will improve this.
filename=raw_input("Please input name of PPM-P3 file:")
ppmobject=PPM(filename)
#ppmobject=PPM() also works

# The following is a very small image list which differs from the default image
testlist=[[[0, 0, 255], [0, 255, 0], [0, 30, 30]],[[40, 40, 40], [50, 50, 50],[60, 60, 60]]]

edits=raw_input("""Do you want to update from list (input 0)?
Do you want to turn red(input 1)?
Do you want to horizontal flip(input 2)?
Do you want to rotate clockwise(input 3)?
Do you want to greyscale(input 4)?
Do you want the image to flip colors(input 5)?
Do you wan tthe image's brightness fliped?(input 6)
If you want more than one changes to the image then input two or more numbers like so 12 or 1234""")
for index in edits: # loops every charter in the string make by the raw_input function
    if index=='0': #if the charter the string is a zero do the following
        ppmobject.PPM_updatefrompixellist(testlist) #calls the class funcation called PPM_updatefrompixellist and input the varable called testlist

    if index=='1': #if the charter the string is a one do the following
        ppmobject.PPM_make_red() #calls the class funcation called PPM_make_red

    if index=='2': #if the charter the string is a two do the following
        ppmobject.PPM_flip_horizontal() #calls the class funcation called PPM_flip_horizontal

    if index=='3': #if the charter the string is a three do the following
        ppmobject.PPM_rotateclockwise() #calls the class funcation called PPM_rotateclockwise

    if index=='4': #if the charter the string is a fouth do the following
        ppmobject.PPM_greyscale() #calls the class funcation called PPM_greyscale

    if index=="5": #if the charter the string is a five do the following
        ppmobject.PPM_flip_colors() #calls the class funcation called PPM_flip_colors

    if index=="6": #if the charter the string is a six do the following
        ppmobject.PPM_Filp_Brightness() #calls the class funcation called PPM_Filp_Brightness

root.mainloop() #needed to use Tkinter with the ppm class