###############################################################################
# Author: Fanyang Cheng
# Date: 03/12/2021
# Description: This program use one fuction to generate specific digits' number
# and ask an addition question to user. Then it will let the user answer it to
# judge the correctness.
###############################################################################
import random as r
def random_number(d):
    return int(r.uniform(10**(d-1),10**d))

def main():
    # Write your mainline logic here ------------------------------------------
    a = random_number(2)
    b = random_number(3)   #get two numbers
    print(format(a,'5'))
    print("+",b)
    print("-----")         #display
    r = int(input("= "))      #return user's answer
    if r == a+b:
        print("Correct -- Good Work!")
    else:
        print("Incorrect. The correct answer is ",a+b,".",sep = "") #judge


# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
