# G00364778
# Gerhard van der Linde
# Week 3 Assgnment - Collatz conjecture
# https://en.wikipedia.org/wiki/Collatz_conjecture
import matplotlib.pyplot as plt
range=[]
n=int(input("Please provide a starting number:"))
nstart = n
while n > 1:
    if n % 2 == 0: # even number
        n/=2
    elif n % 2 > 0: # odd number
        n*=3
        n+=1
    print("%i" %n)
    range.append(int(n))
plt.plot(range)
plt.xlabel("iterations")
plt.ylabel("Vlaue of n")
plt.title("Collatz Conjecture starting at %i" % nstart)
plt.show()
