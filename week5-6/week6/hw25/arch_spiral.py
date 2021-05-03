###############################################################################
# Author: Fanyang Cheng
# Date: 03/14/2021
# Description: This program draws Archimedean Spiral in six turns. (based on the
# outcome picture.)
###############################################################################
# add two imports
from turtle import *
from math import *

def main():
    # Don't change this block -------------------------------------------------
    setup(564, 564)
    width('5')
    # -------------------------------------------------------------------------


    # Write your mainline logic here ------------------------------------------
    # set the initial position and turtle direction
    penup()
    goto(0,0)
    setheading(0)
    pendown()
    # use a for loop to draw each point by factor of degree.
    for i in range(6*360+1):
        thet_r = i*pi/180  #convert theta from degree to radian
        goto(i*cos(thet_r)/10,i*sin(thet_r)/10)

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
