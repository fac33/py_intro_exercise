###############################################################################
# Author: Fanyang Cheng
# Date: 03/13/2021
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
    pos_x,pos_y = -220,-30 #set the initial position
    # write the letters.
    for i in wl:
        if i ==1:
            pos_x,cur_y = v.draw_a(pos_x,pos_y)
            pos_x = pos_x+30 #every time a letter is written, the pen should move left for the next one.
        if i == 2:
            pos_x,cur_y = v.draw_e(pos_x,pos_y)
            pos_x = pos_x+30
        if i == 3:
            pos_x,cur_y = v.draw_i(pos_x,pos_y)
            pos_x = pos_x+30
        if i == 4:
            pos_x,cur_y = v.draw_o(pos_x,pos_y)
            pos_x = pos_x+30
        if i == 5:
            pos_x,cur_y = v.draw_u(pos_x,pos_y)
            pos_x = pos_x+30



# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
