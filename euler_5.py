# Gerhard van der Linde - 19 February 2018
# G00364778
# Excercise #4
# Euler Problem # 5
#
# Write a Python program using for and range to calculate the smallest 
# positive number that is evenly divisible by all of the numbers from 1 to 20.
import time

foundanswer=False # set the starting condition of the value to false
c=0 # Start the test value at zero
maxval=20

tstart=time.time()
while foundanswer == False:
    c+=1 # incrememyt the test value by one every cycle the answer is not found
    testval=0 # reset the testval for the next test
    for x in range(1,maxval+1):
        testval+=c%x # if all the tests result on zero
    if testval==0:
        foundanswer=True
        tend=time.time()
        print('Smallest value devisable by 1 to %i is %. (calculated in %0.3f s)' %(maxval, c,tend-tstart))