# G00364778
# Gerhard van der Linde
# Week 3 Assgnment - Collatz conjecture
# https://en.wikipedia.org/wiki/Collatz_conjecture
#
# Sample output using the value 17
#
# Please provide a starting number:17
# 52
# 26
# 13
# 40
# 20
# 10
# 5
# 16
# 8
# 4
# 2
# 1


n=int(input("Please provide a starting number:"))
while n > 1:
    if n % 2 == 0: # even number
        n/=2
    elif n % 2 > 0: # odd number
        n*=3
        n+=1
    print("%i" %n)
