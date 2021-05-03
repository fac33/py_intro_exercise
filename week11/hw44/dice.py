################################################################################
# Author: Fanyang Cheng
# Date: 04/12/2021
# Description: This program use class method to set the die's sides and time of
# rolling and roll the dice.
################################################################################
import random as r
#define the class dice
class Dice:
    def __init__(self,sides):
        self.sides = sides
    #then define the two functions roll and n_rolls
    def roll(self):
        return(r.randint(1,self.sides))
    def n_rolls(self,t):
        ot = []
        for i in range(t):
            ot.append(str(self.roll()).rstrip())
        print('Rolling a ',self.sides,' sided die ',t,' times: ',', '.join(ot),sep = '')

def main():
    #create three required dices
    s_6 = Dice(6)
    s_10 = Dice(10)
    s_20 = Dice(20)
    #roll 1o times
    s_6.n_rolls(10)
    s_10.n_rolls(10)
    s_20.n_rolls(10)



if __name__ == '__main__':
    main()
