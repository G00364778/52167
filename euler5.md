# Euler 5 

The answer to Euler #5 is a simple multiplication:

```math
N = 2 * 3 * 2 * 5 * 7 * 2 * 3 * 11 * 13 * 2 * 17 * 19 = 232792560
```

The multiplication includes all the prime numbers in the range plus all the occurrences of prime factors in the range, so lines 4, 8, 9 and 16 in the table below.


n|Pfact|Prime|Prime Multiple|N
:---------:|:---:|:---:|:---:|:---:
1| -       | | | 
2| 2       |y| |2
3| 3       |y| |3
4| 2x2     | |y|2
5| 5       |y| |5
6| 2x3     | | | 
7| 7       |y| |7
8| 2x2x2   | |y|2
9| 3x3     | |y|3
10| 2x5    | | |
11| 11     |y| |11
12| 2x2x3  | | |
13| 13     |y| |13
14| 2x7    | | |
15| 3x5    | | |
16| 2x2x2x2| |y|2
17| 17     |y| |17
18| 2x3x3  | | |
19| 19     |y| |19
20| 2x2x5  | | |

So from the truth table above as a guide, construct a software algorithm to solve the problem.

The answer is a simple multiplication and includes all the prime numbers in the range plus 
all the occurrences of prime factors in the range, so lines 4, 8, 9 and 16, so the final formula
for the sample range(20) is: N = 2 * 3 * 2 * 5 * 7 * 2 * 3 * 11 * 13 * 2 * 17 * 19 = 232792560

Constructing an algorithm from this information then:
1. For the range of values(20 as in the example) list the prime numbers
1. generate a sorted list of prime factors in same range to test against
1. create a list of primes and and prime factors in the range
1. multiply the list to get the final answer

```python
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

```