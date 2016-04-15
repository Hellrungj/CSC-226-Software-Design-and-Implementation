#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hellrungj
#
# Created:     08/04/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

N = 1
N2 = 2
D = 5
D2 = 3

S1_TD = D2
S1_D = D * S1_TD
S1_N = N * S1_TD

S2_TD = D
S2_D = D2 * S2_TD
S2_N = N2 * S2_TD

##print S2_N
##print '--'
##print S2_D
##print S1_N
##print '--'
##print S1_D

T_N = S2_N + S1_N
T_D = S1_D
##print T_N
##print '--'
##print T_D