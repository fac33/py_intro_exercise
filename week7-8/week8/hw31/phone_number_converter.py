################################################################################
# Author: Fanyang Cheng
# Date: 27/03/2021
# Description: This file ask user to give a "letter phone number" and it will
# convert it into a typical phone number.
################################################################################
#define convert_number function
def convert_number(n):
    n = n.lower() #lower case all of the letters
    nl = []
    for i in n:
        nl.append(i)#chagne it into a list
    #build a list include all alphabetical options
    value = [["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
    for i in range(len(nl)):
        for j in range(len(value)):
            if nl[i] in value[j]:
                nl[i] = str(j+2)
    return("".join(nl))
def main():
    n = input("Enter a telephone number: ")
    o = convert_number(n)
    print("The phone number is",o)

if __name__ == '__main__':
    main()
