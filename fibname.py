# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

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
