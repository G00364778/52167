# Gerhard van der Linde - 19 February 2018
# G00364778
# Excercise #4
# Euler Problem # 5
#
# Write a Python program using for and range to calculate the smallest 
# positive number that is evenly divisible by all of the numbers from 1 to 20.

# ANSWER: Smallest value devisable by 1 to 20 is 232792560. (calculated in 46.820 s)

# Optimisation steps were required to arrive at a workable solution.
# The factors was reduce to 11,12,13,14,15,16,17,18,19,20 since the 
# smaller values were all factors of the bigger ones in any case. Also
# by incrementing by twenty every cycle reduced a lot of unnessesary attemps
# that would have failed in a test in any case, so this resulted in a 47 second
# solution that was more acceptable.

''' 
import time # to calculate the execution time

foundanswer=False # set the starting condition of the value to false
c=20 # Start the test value at twenty
maxval=20
#devisors=[2,3,5,7,11,13,17,19]
devisors=[11,13,14,15,16,17,18,19]
#devisors=[11,12,13,14,15,16,17,18,19]

tstart=time.time()
while foundanswer == False:
    c+=20 # increment the test value by twenty every cycle the answer is not found
    testval=0 # reset the testval for the next test cyle
    #for x in range(11,maxval+1):
    for x in range(len(devisors)):
        #print(c,devisors[x],c%devisors[x])
        testval+=c%devisors[x] # sum all the test values and test for zero
    if testval==0:
        foundanswer=True
        tend=time.time()
        print('Smallest value devisable by 1 to %i is %i. (calculated in %0.3f s)' %(maxval, c,tend-tstart))
'''
# script output sample
# Smallest value devisable by 1 to 20 is 232792560. (calculated in 19.231 s)

# A lengthy group discussion on the topic showed some smarter mathmatical approaches is possible. 

# n  Pfact   Prime   Prime Multiple  N
# 1  -
# 2  2       y                       2
# 3  3       y                       3
# 4  2x2             y               2
# 5  5       y                       5
# 6  2x3                              
# 7  7       y                       7
# 8  2x2x2           y               2
# 9  3x3             y               3
# 10 2x5                              
# 11 11      y                      11
# 12 2x2x3                            
# 13 13      y                      13
# 14 2x7                              
# 15 3x5                              
# 16 2x2x2x2         y               2
# 17 17      y                      17
# 18 2x3x3                            
# 19 19      y                      19
# 20 2x2x5                            

# So in order to calculate the number the table above aims to provide a mathmatical guid
# for developing an improved algorythm to solve the question.

# The answer is a simple multiplcation and includes all the prime numbers in the range plus 
# all the occurances of prime facors in the range, so lines 4, 8, 9 and 16, so the final formula
#  for the sample range(20) is: N = 2 * 3 * 2 * 5 * 7 * 2 * 3 * 11 * 13 * 2 * 17 * 19 = 232792560

# Constructing an algorythm from this information then:
# 1. For the range of values(20 for example) list the prime numbers
# 2. generate a sorted list of prime factors in same range to test against 
# 3. create a list of primes and and prime factors in the range
# 4. multiply the list to get the final answer

import numpy as np # to calculate product of list N
import time # to calculate the execution time
tstart=time.time()
TestRange = 27
max_r=int(TestRange**.5)# experimental - not sure about this
#max_r=TestRange
print('\n                     Test range: 1 - ',TestRange)
#print('max_r:',max_r) # determine the range of primes to explore for factors
#l=[i for i in range(2,TestRange+1)] # generate a list of numbers to test
p=[] # prime numbers
pf=[] # prime factors
def testprimes(x):
    if x < 2:
        return False
    for n in range(2,x):
        if x % n == 0:
            return False
    return True

for i in range(1,TestRange+1):
    test=testprimes(i)
    if test==True:
        p.append(i) # 1. generate a list of primes numbers in the range
print('prime numbers in the test range:',p)

for i in p:
    if i <= max_r: # only check for number possible smaller than testrange
        #print('\t',i)
        for j in range(2,max_r+1):
            if i**j<TestRange:
                pf.append(i) # 2. Generate the list of prme factors in the range
                #print('\t',i,'^', j,'=', i**j)
print('prime factors in the test range:',pf)
N=pf+p # 3. Combine the two lists 
print('   product of the two lists (N): {} = {:,d}'.format(N,np.prod(N)))# calculate the product ofthe list
tend=time.time()
print('                Processing Time: {:f} ms\n'.format((tend-tstart)*100))

# Sample output generated during testing: 

#                      Test range: 1 -  20
# prime numbers in the test range: [2, 3, 5, 7, 11, 13, 17, 19]
# prime factors in the test range: [2, 2, 2, 3]
#    product of the two lists (N): [2, 2, 2, 3, 2, 3, 5, 7, 11, 13, 17, 19] = 232,792,560
#                 Processing Time: 0.100327 ms