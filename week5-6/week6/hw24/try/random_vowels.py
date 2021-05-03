###############################################################################
# Author: Fanyang Cheng
# Date: 03/14/2021
# Description: This file import the function from vowels.py and draw the five
# letters in random order on the turtle canvas.
###############################################################################

from turtle import *

# Add your imports here -------------------------------------------------------
import vowels as v
import random as r

def main():
    # Don't change this block -------------------------------------------------
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)
    # -------------------------------------------------------------------------
    # Write your mainline logic here ------------------------------------------
    wl = r.sample([1,2,3,4,5],k = 5) #randomly select the order of vowels.
    j = 0  #add a counter to calculate the actual appearing order of each vowels.
    # write the letters.
    for i in wl:
        penup()
        goto(-220+j*90,-30)  # preset each letter's postition
        if i ==1:
            v.draw_a()
        if i == 2:
            v.draw_e()
        if i == 3:
            v.draw_i()
        if i == 4:
            v.draw_o()
        if i == 5:
            v.draw_u()
        j+=1



# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
