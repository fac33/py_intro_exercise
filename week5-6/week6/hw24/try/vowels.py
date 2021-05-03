###############################################################################
# Author: Fanyang Cheng
# Date: 03/14/2021
# Description: This file works as a package to serve the turtle function which
#draws the vowels' letter (a,e,i,o,u).
###############################################################################

from turtle import *


def draw_a():
    penup()
    setheading(0)
    forward(30)
    pendown()
    circle(30)
    penup()
    forward(30)
    setheading(90)
    forward(60)
    setheading(270)
    pendown()
    forward(60)
def draw_e():
    penup()
    setheading(90)
    forward(30)
    pendown()
    setheading(0)
    forward(60)
    left(90)
    circle(30,320)
def draw_i():
    penup()
    setheading(0)
    forward(30)
    left(90)
    forward(70)
    setheading(270)
    pendown()
    forward(1)
    penup()
    forward(10)
    pendown()
    forward(59)
def draw_o():
    penup()
    setheading(0)
    forward(60)
    pendown()
    circle(30)
def draw_u():
    penup()
    setheading(0)
    forward(10)
    left(90)
    forward(55)
    setheading(0)
    pendown()
    right(90)
    forward(30)
    circle(25,180)
    penup()
    forward(35)
    pendown()
    right(180)
    forward(55)
def main():

    # You can use this for your own testing.
    draw_e(0,60)
    x,y = draw_a(60,60)
    print(x,y)

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
