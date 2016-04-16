#-------------------------------------------------------------------------------
# Name:        Test Run for if statement that use >= or/and <=
# Purpose:
#
# Author:      hellrungj
#
# Created:     02/02/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
Player1 = raw_input("1-4")

if int(Player1) <= 4 and int(Player1) >= 1:
    print "pass"
else:
    print "Failer"