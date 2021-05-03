###############################################################################
# Author: Fanyang Cheng
# Date: 03/12/2021
# Description: This program use get_computer_choice to get the choice of computer.
# Use get_player_choice to get the choice of the user. And paly the rock, paper,
# scissors game to find the final winner.
###############################################################################
import random as r
def get_computer_choice():
    c = int(r.uniform(1,4))
    if c == 1:
        return "rock"
    elif c == 2:
        return "paper"
    else:
        return "scissors"
def get_player_choice():
    while True:
        c = input("Choose rock, paper or scissors: ")
        if c != "paper" and c != "rock" and c != "scissors":
            print("You made an invalid choice. Please try again.")
        else:
            break
    return c
def get_winner(comp,pla):
    if (comp == "rock" and pla == "paper") or (comp == "paper" and pla == "rock"):
        if comp == "rock":
            return "player"
        else:
            return "computer"
    elif (comp == "rock" and pla == "scissors") or (comp == "scissors" and pla == "rock"):
        if comp == "scissors":
            return "player"
        else:
            return "computer"
    elif (comp == "paper" and pla == "scissors") or (comp == "scissors" and pla == "paper"):
        if comp == "paper":
            return "player"
        else:
            return "computer"
    else:
        return "tie"
def main():
    # Write your mainline logic here ------------------------------------------
    while True:    #loop to paly again if tie
        comp = get_computer_choice()
        pla = get_player_choice()
        print("  The computer chose ",comp,", and you chose ",pla,".",sep = "")
        #print the rule
        if (comp == "rock" and pla == "paper") or (comp == "paper" and pla == "rock"):
            print("  paper beats rock")
        elif (comp == "rock" and pla == "scissors") or (comp == "scissors" and pla == "rock"):
            print("  rock beats scissors")
        elif (comp == "paper" and pla == "scissors") or (comp == "scissors" and pla == "paper"):
            print("  scissors beats paper")
        #start gudgement function
        win = get_winner(comp,pla)
        if win == "player":
            print("  You won the game!")
            break
        elif win == "computer":
            print("  You lost.  Better luck next time.")
            break
        else:
            print("  Its a tie. Starting over.")
            print("")
    print("Thanks for playing.")
# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
