################################################################################
# Author: Fanyang Cheng
# Date: 03/20/2021
# Description: This program rolls one pair of dies for specific times and calculate
# percentage of each points relative to the total number of rolling.
################################################################################
#import random
import random as r
#define roll_d6
def roll_d6():
    return r.randint(1,6)
#define roll_2d6, give the number of the rolls
def get_2d6_rolls(n):
    l_r = []
    for i in range(n):
        d1 = roll_d6()
        d2 = roll_d6()
        sum = d1+d2
        l_r.append(sum)
    return l_r
    #main function
def main():
    t = 900000
    p = []
    l_a = get_2d6_rolls(t)
    for i in range(11):
        p.append(100*l_a.count(i+2)/t)
    #print answer
    print("Roll  Frequency")
    for j in range(11):
        print(" ",format(j+2,'2'),"    ",format(p[j],'5.2f'),"%",sep = "")



if __name__ == '__main__':
    main()
