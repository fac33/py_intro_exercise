################################################################################
# Author: Fanyang Cheng
# Date: 2/16/2021
# This program ask user to give the print line number(x) and
# print a x lines of hash pattern.
################################################################################
m = int(input("Enter the number of lines: "))  #ask user for the input.
for i in range(m):   #first loop (outer loop)
    print("#",end = '')
    for j in range(i):  #second loop (inner loop)
        print(" ",end = '')
    print("#")
