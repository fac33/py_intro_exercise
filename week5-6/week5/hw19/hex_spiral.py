################################################################################
# Author: Fanyang Cheng
# Date: 02/03/2021
# Description: This program uses a for loop to draw a graph of concentric hexagon.
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width('5')
    # --------------------------------------------------------------------------

    # Write your code here
    #start for loop
    for i in range(39):
        forward(6+i*6)
        right(60)

# Don't change this
if __name__ == '__main__':
    main()
    done()
