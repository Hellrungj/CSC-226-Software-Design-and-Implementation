#-------------------------------------------------------------------------------
# Name:       csc226E2-part2.py
# Purpose: A program that takes a list of movie titles and a specific title and
#   determines how many times that title appears on the list.
#
# Created:     Mar/21/2014
# ------------------------------------------------------------------------------
# Exam E1 Part B
# Instructions:
#   (9 points)
#   First, you are to define a fruitful function called how_many_times_seen_movie
#   takes takes as parameters (1) a list of movie titles and (2) a movie title,
#   and returns the number of times that title appears on the list.
#   THIS FUNCTION SHOULD NOT OUTPUT TO THE SCREEN!
#
#   (6 points)
#   Secondly, you are to create at least 3 unit tests to ensure that the
#   how_many_times_seen_movie(...) function works correctly.
#
#   As always, you must include comments and appropriate docstrings in your
#   code that explains what it is doing.
#-------------------------------------------------------------------------------

#------------ Do not change these functions. They work correctly. --------------
import sys

def testit(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def ask_user_movies():
    '''Repeatedly ask the user for movie titles until she responds "y" to
        the question "Are you done?" All the titles are put into a list that
        is returned.'''
    movie_list = [] # variable to hold the list of movie titles
    #ask to whether to continue and test for a 'y' in the same line.
    while raw_input("Are you done? (type 'y' to finish)") != "y":
        # ask the user for the title of the movie and append it in one line.
        movie_list.append(str(raw_input("Movie title? ")))

    return movie_list
#------------ Do not change these functions. They work correctly. --------------


# ##########################################################################
#    YOUR PART STARTS BELOW!!
# ##########################################################################
#
# Your Name:  John Hellrung
#
# ##########################################################################
# PART 1:
#   Complete this function
# ##########################################################################
def how_many_times_seen_movie( movie_list, movie_title ):
    ''' Given a list of movies and the title of a specific one, return
    how many times that movie was in the list.'''
    num_times = 0 # varable for a count of times the name(movie-title) show up n the string movie_list
    index = 0 # to keep an index for refering a part a string movie_list
    name = movie_title # sets name to movie_title
    while int(index) < len(movie_list): # while the index is less than the length of movie list run the follow lins of code
        if name == movie_list[index]: # if name is equal to movie_list[index](witch is the title chocen by the index) proform the following code
            num_times = num_times + 1 # add one to the num_times or counts
        index = index + 1 # add one to the index or counts
    return num_times # returns the vaule of num_times

# ##########################################################################
# PART 2:
#   Put at least three unit tests using the testit() function that checks
#   to make sure your how_many_times_seen_movie function works. Be sure to
#   include the test for when there are no movies in the list.
#   We included a sample list for you to test your function, but you should
#   also create your own list.
# ##########################################################################
movie_title = ask_user_movies
sample_movie_list = ["gravity", "jaws", "brave", "brave", "wall-e", "muppets most wanted"]
testit((how_many_times_seen_movie(("Jaws","Jaws","Jaws","Jack"),"Jack")) == (1))
testit((how_many_times_seen_movie(("Hall","James","HJS","JACK","Starwars","Starwars"),"Starwars")) == (2))
testit((how_many_times_seen_movie(("John","John","Fast5","John"),"John")) == (3))
