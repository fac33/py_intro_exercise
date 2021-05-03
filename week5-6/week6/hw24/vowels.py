###############################################################################
# Author: Fanyang Cheng
# Date: 03/13/2021
# Description: This file works as a package to serve the turtle function which
#draws the vowels' letter (a,e,i,o,u).
###############################################################################

from turtle import *


def draw_a(x,y):
    penup()
    setheading(0)
    goto(x+30,y)
    pendown()
    circle(30)
    penup()
    goto(x+60,y+60)
    setheading(270)
    pendown()
    forward(60)
    return position()
def draw_e(x,y):
    penup()
    goto(x,y+30)
    pendown()
    setheading(0)
    forward(60)
    left(90)
    circle(30,320)
    return position()
def draw_i(x,y):
    penup()
    setheading(270)
    goto(x+30,y+70)
    pendown()
    forward(1)
    penup()
    forward(10)
    pendown()
    forward(59)
    return position()
def draw_o(x,y):
    penup()
    setheading(0)
    goto(x+60,y)
    pendown()
    circle(30)
    return position()
def draw_u(x,y):
    penup()
    setheading(0)
    goto(x+10,y+55)
    pendown()
    right(90)
    forward(30)
    circle(25,180)
    penup()
    goto(x+60,y+55)
    pendown()
    right(180)
    forward(55)
    return position()
def main():

    # You can use this for your own testing.
    draw_e(0,60)
    x,y = draw_a(60,60)
    print(x,y)

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
