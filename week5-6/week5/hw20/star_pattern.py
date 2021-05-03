################################################################################
# Author: Fanyang Cheng
# Date: 03/04/2021
# Description: This program ask user for the points of star and draws it.
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()
    # --------------------------------------------------------------------------

    # Write your code here
    strn = int(input("How many points do you want?: ")) #get the number of points.
    A = 360/strn #the inner angle
    B = 2*A #outer angle
    color('black','blue')
    begin_fill()
    right((180-B)/2) #head to the correct direction.
    for i in range(strn):
        forward(side_length)
        left(180-A)
        forward(side_length)
        right(180-B)
    end_fill()


# Don't change this
if __name__ == '__main__':
    main()
    done()
