################################################################################
# Author: Fanyang Cheng
# Date: 2/16/2021
# This program repeatedly asks user to enter a series of non-negative
# numbers and gives the sum and average of these numbers. negative
# number means the end of loop.
################################################################################
m,sum,amo = 0,0,-1  #preset sum and amount.
while True:   #start the loop.
    sum+=m
    amo+=1
    if amo !=0:      #factor out the condition that when the first input is negative.(no need to calculate the average.)
        avg = sum/amo
    m = float(input("Enter a non-negative number (negative to quit): ")) #give input
    if m<0 and amo != 0:      #if the first input is not negative.
        print("Sum =", format(sum,'.2f'))
        print("Average =",format(avg,'.2f'))
        break
    elif m<0 and amo == 0:     #if the first input is negative.
        print("No input.")
        break
