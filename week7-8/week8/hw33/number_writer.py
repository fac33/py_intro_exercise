################################################################################
# Author: Fanyang Cheng
# Date: 27/03/2021
# Description: This program ask user to provide how many random numbers they want
# to add into the random_numbers.txt and generate the txt file.
################################################################################
import random as r
def main():
    #ask user for the amount of number.
    n = int(input("Enter the number of random numbers to be written to the file: "))
    with open('random_numbers.txt','w') as ran:  #open the file or create one.
        for i in range(n):
            ran.write(str(r.randint(1,500))+"\n")  #for every time write a random number into the file and press one enter.

if __name__ == '__main__':
    main()
