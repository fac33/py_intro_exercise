###############################################################################
# Author: Fanyang Cheng
# Date: 04/23/2021
# Description:This program will serve a game called Wheel of Fourtune which
#is a kind of gangbling game version of hangman.
###############################################################################
import random as r
#define constant list vowels and consonants
vow = ['A','E','I','O','U']
cons = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
#define spin_the_wheel function
def spin_the_wheel():
    choice = [500,500,500,500,500,550,600,600,600,600,650,650,650,700,700,700,800,900,2500,0,0]
    ch = r.randint(0,20)
    if choice[ch] == 0:
        return "BANKRUPT"
    else: return choice[ch]
#create a oop called turn to represent character and methods for each round of game.
class round:
    def __init__(self,target,turn_n = 0,old_money = 0,vow = ['A','E','I','O','U'],cons = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z'],round_n = 1,money = 0):
        self.vow = vow
        self.cons = cons
        self.round_n = round_n
        self.money = money
        self.used = set()
        self.target = target
        self.old_money = old_money
        self.turn_n = turn_n
    #define wheel_spin method
    def wheel_spin(self,target): #target is the actual word user want to guess
        #call the spin_the_wheel function
        target_up = target.upper()
        out = spin_the_wheel()
        self.turn_n = self.turn_n+1
        if out == 'BANKRUPT':
            print("The wheel landed on BANKRUPT.")
            print("You lost $",format(self.money,','),"!",sep = '')
            self.money = 0
            return  0
        else:
            print("The wheel landed on $",format(out,','),".",sep = '')
            while True:
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
                #print(self.used)
                pick = input("Pick a consonant: ")
                if pick.upper() in vow:
                    print("Vowels must be purchased.")
                elif not (pick.upper() in vow or pick.upper() in cons):
                    print("The character",pick,"is not a letter.")
                elif len(pick) > 1:
                    print("Please enter exactly one character.")
                elif pick.upper() in self.used:
                    print("The letter",pick.upper(),"has already been used.")
                else:
                    if pick.upper() not in target.upper():
                        print("I'm sorry, there are no ",pick.upper(),"'s.",sep = '')
                        self.used.add(pick.upper())
                        p = self.cons.index(pick.upper())
                        self.cons[p] = " "
                        return 0 #no change to the money amount.
                    else:
                        ind_l = [] #record for the position
                        for i in range(len(target_up)):
                            ind = target_up.find(pick.upper())
                            if not ind == -1:
                                ind_l.append(ind) #return -1
                            target_up = target_up.replace(pick.upper(),"_",1)
                        self.used.add(pick.upper())
                        self.money = self.money + len(ind_l)*out
                        #factor out the letter from consonent list.(used to display)
                        p = self.cons.index(pick.upper())
                        self.cons[p] = " "
                        print("There is ",len(ind_l)," ",pick.upper(),", which earns you $", format(len(ind_l)*out,','),".",sep = '')
                        return ind_l #can calcluate for the amount by the list and refresh the appearings.

    #then we define the buy_a_vowel funciton
    def buy_a_vowel(self,target):
        self.turn_n = self.turn_n+1
        if self.money < 250:
            print("You need at least $250 to buy a vowel.")
            return 0 #stop instantly.
        elif self.vow == [" "," "," "," "," "]:
            print("There are no more vowels to buy.")
            return 0
        else:
            target_up = target.upper()
            self.money = self.money - 250
            while True:
                pick = input("Pick a vowel: ")
                if pick.upper() in cons:
                    print("Consonants cannot be purchased.")
                elif len(pick) >1:
                    print("Please enter exactly one character.")
                elif pick in self.used:
                    print("The letter",pick.upper(),"has already been purchased.")
                elif not (pick.upper() in vow or pick.upper() in cons):
                    print("The character", pick,"is not a letter.")
                else:
                    if pick.upper() not in target_up:
                        print("I'm sorry, there are no ",pick.upper(),"'s.",sep = "")
                        self.used.add(pick.upper())
                        p = self.vow.index(pick.upper())
                        self.vow[p] = " "
                        return 0 #stop the turn
                    else:
                        ind_l = [] #index list of the chosen vowel
                        for i in range(len(target_up)):
                            ind = target_up.find(pick.upper())
                            if not ind == -1:
                                ind_l.append(ind)
                            target_up = target_up.replace(pick.upper(),"_",1)
                        self.used.add(pick.upper())
                        #still refresh the vowel list to display.
                        p = self.vow.index(pick.upper())
                        self.vow[p] = " "
                        print("There are ",len(ind_l)," ",pick.upper(),"'s.",sep = '')
                        return ind_l
    #define solve_the_puzzle function
    def solve_the_puzzle(self,clue,target):
        self.turn_n = self.turn_n+1
        print("Enter your solution.")
        print(" Clues: ",clue)
        ans = input(" Guess: ")
        if ans.upper() == target.upper():
            print("Ladies and gentelmen, we have a winner!")
            print("You earned $",format(self.money,',')," this round.",sep = '')
        else:
            print("I'm sorry. The correct solution was:")
            print(target.upper())
        self.round_n = self.round_n+1
        #new = round(round_n = self.round_n,old_money = self.old_money+self.money,target = target,cons = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z'],vow =  ['A','E','I','O','U'])
        return(self.round_n,self.old_money+self.money)
    #define quit_the_game function
    def quit_the_game(self):
        self.turn_n = self.turn_n+1
        print("You earned $",format(self.money,',')," this round.",sep = '')
        print("Thanks for playing!")
        print("You earned a total of $",format(self.old_money+self.money,','),".",sep = '')
        self.round_n = 999 #directly stop the game


def main():
    #set vowels and consonents
    #vow = ['A','E','I','O','U']
    #cons = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W']
#first read a random word from the phrases.txt file
    with open('phrases.txt') as fo:
    #read everything
        l = fo.readlines()
        #factor out '\n' tailing
        for i in range(len(l)):
            l[i] = l[i].rstrip('\n')
            #choose one of them
        rand = r.randint(0,len(l)-1)
        targ = l[rand]
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
        #print(targ)
        #begin setting game
        game = round(target = targ)
        #create a outfit for the target which used to display.
        while game.round_n<5:
            if game.turn_n == 0:
                targ_l = list(targ)
                for i in range(len(targ_l)):
                    if targ_l[i].upper() in vow or targ_l[i].upper() in cons:
                        targ_l[i] = "_"
            targ_d = "".join(i for i in targ_l)

            #start print the outings
            print(":::::::::::::::::::::::::::::::::::::::::: ROUND",game.round_n,"of 4 ::")
            print("::",targ_d.center(54),"::",sep = '')
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("::","".join(i for i in game.cons).center(27),"::","".join(i for i in game.vow).center(11),"::","         $",format(game.money,',')," ::",sep= '')
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("What would you like to do?")
            print("  1 - Spin the wheel")
            print("  2 - Buy a vowel")
            print("  3 - Solve the puzzle")
            print("  4 - Quit the game")
            choice = 0
            while not choice in ['1','2','3','4']:
                choice = input("Enter the number of your choice: ")
            choice = int(choice)

            #then based on different choice, apply different functions.
            if choice == 1:
                out_p = game.wheel_spin(targ)
                #gudge the output.
                if not out_p == 0:
                    for i in out_p:
                        targ_l[i] = targ[i]
            elif choice == 2:
                out_p = game.buy_a_vowel(targ)
                if not out_p == 0:
                    for i in out_p:
                        targ_l[i] = targ[i]
            elif choice == 3:
                round_nn,old_moneyn = game.solve_the_puzzle(targ_d,targ)

                #choose one of the word from list and fresh it.
                rand = r.randint(0,len(l)-1)
                targ = l[rand]
                game = round(round_n = round_nn,old_money = old_moneyn,target = targ)
                #game.target = targ  #reset to the new target
                #and just give a try.
                game.cons = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
                game.vow =  ['A','E','I','O','U']
            elif choice == 4:
                game.quit_the_game()
                break




if __name__ == '__main__':
    main()
