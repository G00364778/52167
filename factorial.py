# Gerhard van der Linde - 4 March 2018
# GMIT Programming and scripting excercise week 6

def factorial(num):
    answer=1
    for i in range(1,num+1):
        answer*=i
    return answer

x=[5,7,9]
for i in x:
    print (f'The factorial of {i:1d} is: {factorial(i):6d}')

# Sample output of script
# The factorial of 5 is: 120
# The factorial of 7 is: 5040
# The factorial of 9 is: 362880