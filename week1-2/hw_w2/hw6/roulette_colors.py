################################################################################
# Author: Fanyang Cheng
# Date: 2/12/2021
# This program gives the color of pocket on roulette wheel.
################################################################################
#ask user which pockt's color they want to know
p = int(input("Please enter a pocket number: "))
#then start the gudgement structure to figure out the color.
if p == 0 :
    print("  Pocket",p,"is green.")
elif (p>=1 and p<=10)or(p>=19 and p<=28):
    if p%2 == 0:
        print("  Pocket",p,"is black.")
    else:
        print("  Pocket",p,"is red.")
elif (p>=11 and p<=18)or(p>=29 and p<=36):
    if p%2 == 0:
        print("  Pocket",p,"is red.")
    else:
        print("  Pocket",p,"is black.")
else:
    print("  Invalid Input!")
