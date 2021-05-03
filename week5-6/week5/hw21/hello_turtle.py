################################################################################
# Author: Fanyang Cheng
# Date: 03/05/2021
# Description: this program draws the "hello turtle" by calling funtions and
#print it.
################################################################################

# Don't change this
from turtle import *

def draw_e(x,y):
    # Write this function
    penup()
    goto(x,y+30)
    pendown()
    setheading(0)
    forward(60)
    left(90)
    circle(30,320)
def draw_h(x,y):
    # Write this function
    penup()
    goto(x,y+100)
    pendown()
    right(90)
    forward(100)
    penup()
    goto(x+50,y+20)
    pendown()
    left(180)
    circle(25,180)
    penup()
    goto(x+50,y+30)
    pendown()
    forward(30)

def draw_l(x,y):
    # Write this function
    penup()
    setheading(0)
    goto(x+30,y+100)
    right(90)
    pendown()
    forward(100)
def draw_o(x,y):
    # Write this function
    penup()
    setheading(0)
    goto(x+60,y)
    pendown()
    circle(30)
def draw_r(x,y):
    # Write this function
    penup()
    setheading(0)
    goto(x,y+55)
    pendown()
    right(90)
    forward(55)
    penup()
    goto(x+30,y+55)
    setheading(180)
    pendown()
    circle(30,90)

def draw_t(x,y):
    # Write this function
    penup()
    setheading(0)
    goto(x+30,y+100)
    pendown()
    right(90)
    forward(100)
    penup()
    goto(x+0,y+70)
    pendown()
    left(90)
    forward(60)

def draw_u(x,y):
    # Write this function
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
def main():

    # Don't change this block --------------------------------------------------
    setup(600, 400)
    width(9)
    # --------------------------------------------------------------------------

    # Write your main function code here
    #posite each letters.
    draw_h(-250,0)
    draw_e(-180,0)
    draw_l(-130,0)
    draw_l(-90,0)
    draw_o(-50,0)
    draw_t(-250,-120)
    draw_u(-190,-120)
    draw_r(-100,-120)
    draw_t(-70,-120)
    draw_l(-10,-120)
    draw_e(50,-120)



# Don't change this
if __name__ == '__main__':
    main()
    done()
