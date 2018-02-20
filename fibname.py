# Topic 1: Basics of programming - Excercise 1
# Gerhard van der Linde
# Copied from Ian McLoughlin
# A program that displays Fibonacci numbers.
#
# Re: Fibonacci exercise responses
# by GERHARD VAN DER LINDE - Monday, 22 January 2018, 4:14 PM
#  
# My name is Gerhard, so the first and last letter of my name 
# (G + D = 7 + 4) give the number 11. The 25th Fibonacci number is 89. 


# Topic 2: State, variables and statements - Excercise 2
# Gerhard van der Linde
# Copied from Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.
#
# Re: Week 2 task
# by GERHARD VAN DER LINDE - Tuesday, 30 January 2018, 8:40 PM
#  
# running  "python fibname.py" yields:
# 
# My surname is "van der Linde"
# The first letter v is Unicode number 118
# The last letter e is Unicode number 101
# The Fibonacci number for the sum of the Unicode numbers 219 
# is 2623059926317798754175087863660165740874359106
# ================ About the Python ord() function ==================
# One of the many Python built-in functions is ord().
# The ord() function returns an integer value representing the Unicode 
# value of the character passed to ord().

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = '"van der Linde"'
first = name[1]
last = name[-2]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is unicode number", firstno)
print("The last letter", last, "is unicode number", lastno)
print("The Fibonacci number for the sum of the unicode numbers", x ,"is", ans)
print("""\

================ About the Python ord() function ==================

One of the many Python builtin functions is ord(). 

The ord() function returns an integer value representing the Unicode
value of the character passed to ord().

""")
