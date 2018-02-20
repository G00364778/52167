# Gerhard van der Linde - 19 February 2018
# G00364778
# Excercise #4
# Euler Problem # 5
#
# Write a Python program using for and range to calculate the smallest 
# positive number that is evenly divisible by all of the numbers from 1 to 20.

# ANSWER: Smallest value devisable by 1 to 20 is 232792560. (calculated in 46.820 s)

# Optimisation steps were required to arrive at a workable solution.
# The factors were reduce to 11,12,13,14,15,16,17,18,19,20 since the 
# smaller values were all factors of the bigger ones in any case. Also
# by incrementing by twenty every cycle reduced a lot of unnessesary attemps
# that wold have failed in a test in any case, so this resulted in a 47 second
# solution that was more acceptable.

import time # to calculate the execution time

foundanswer=False # set the starting condition of the value to false
c=20 # Start the test value at twenty
maxval=20

tstart=time.time()
while foundanswer == False:
    c+=20 # increment the test value by twenty every cycle the answer is not found
    testval=0 # reset the testval for the next test cyle
    for x in range(11,maxval+1):
        testval+=c%x # sum all the test values and test for zero
    if testval==0:
        foundanswer=True
        tend=time.time()
        print('Smallest value devisable by 1 to %i is %i. (calculated in %0.3f s)' %(maxval, c,tend-tstart))
