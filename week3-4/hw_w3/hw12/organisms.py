################################################################################
# Author: Fanyang Cheng
# Date: 2/16/2021
# This program predicts the approximate size of a population of organism by
# asking users for the starting population, daily increase in percent and
# number of days to multiply.
################################################################################
# start asking.
p = float(input("Starting number, in million: "))
i = float(input("Average daily increase, in percent: "))
d = int(input("Number of days to multiply: "))
print("Day   Approx. Pop")   #print title
#start the calculation loop.
for j in range(d):
    print(format(j+1,'3'),format(p,'13.4f'))
    p = p*(1+i/100)  #update new population
