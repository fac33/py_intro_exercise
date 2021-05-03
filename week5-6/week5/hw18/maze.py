################################################################################
# Author: Fanyang Cheng
# Date: 03/04/2021
# Description this program uses turtle to find the solution go out from the maze.
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    bgpic('maze.png')
    shape('turtle')
    color('green')
    width('5')
    step = 12
    # --------------------------------------------------------------------------

    # Write your code here (the step of the turtle.)
    forward(10)
    left(90)
    forward(35)
    right(90)
    forward(25)
    left(90)
    forward(75)
    left(90)
    forward(25)
    right(90)
    forward(95)
    right(90)
    forward(25)
    left(90)
    forward(23)
    right(90)
    forward(193)
    right(90)
    forward(227)
    left(90)
    forward(35)

# Don't change this
if __name__ == '__main__':
    main()
    done()
