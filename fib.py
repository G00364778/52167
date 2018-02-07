# Gerhard van der Linde
# A program that displays Fibonacci numbers.
# Re: Fibonacci exercise responses
# by GERHARD VAN DER LINDE - Monday, 22 January 2018, 4:14 PM
#  
# My name is Gerhard, so the first and last letter of my name (G + D = 7 + 4) give the number 11. The 25th Fibonacci number is 89. 


def fib(n):
    """This function returns the nth Fibonacci number."""
    i = 0
    j = 1
    n = n - 1

    while n >= 0:
      i, j = j, i + j
      n = n - 1

    return i

# Test the function with the following value.
x = 11
ans = fib(x)
print("Fibonacci number", x, "is", ans)
