################################################################################
# Author: Fanyang Cheng
# Date: 2/11/2021
# This program calculates the number of
#days in February for the input year.
################################################################################
y = int(input("Please input a year: ")) #get input
d = 28  #preset for the output date in February
if y%100 == False:     #check structure
    if y%400 == False:
        d = 29
elif y%4 == False:
    d = 29            #change the date
print("In the year ",y,", there are ",d," days in February.",sep = "")  #output
