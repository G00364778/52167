# Read the and display the values from a csv file
# Gerhard van der Linde
# GMIT G00364778
# 27 February 2018

def makefloat(teststr):
  try:
    return float(teststr) # return a floating point value if possibe.
  except:
    return teststr # otherwise return the string as is

with open(r'data\iris.csv','r') as file: #open and read the csv file
    for line in file: # loop through the file a line at a time
      #print(line)
      #exit()
      dat=line.strip().split(',') # strip the space and newline and split on commas
      dat=[makefloat(i) for i in dat] # user function to convert list to floats in numbers
      print('{2:4.1f} {3:4.1f} {0:4.1f} {1:4.1f}'.format(dat[0], dat[1], dat[2],dat[3]))
      #print('sepal l:{:4.1f} sepal w:{:4.1f} petal l:{:4.1f} petal w:{:4.1f}'.format(float(dat[0]),float(dat[1]),float(dat[2]),float(dat[3])))

# sample of output generated by the commented code on line 18
# sepal l: 5.1 sepal w: 3.5 petal l: 1.4 petal w: 0.2
# sepal l: 4.9 sepal w: 3.0 petal l: 1.4 petal w: 0.2
# sepal l: 4.7 sepal w: 3.2 petal l: 1.3 petal w: 0.2

# sample of output generated by code
#  6.7  3.0  5.2  2.3
#  6.3  2.5  5.0  1.9
#  6.5  3.0  5.2  2.0