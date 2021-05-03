################################################################################
# Author: Fanyang Cheng
# Date: 27/03/2021
# Description: This program read the file created in exercise 33 and calculate
#the total number, max,min, sum and average of the numbers.
################################################################################

def main():
    with open('random_numbers.txt','r') as rand:
        l = []   #create a list to get the number line by line.
        for line in rand:
            l.append(int(line.rstrip()))  #append the number without the "\n" mark.
        print(format(len(l),','),"numbers were read from the file.") #output
        print("Max:",max(l))
        print("Min:",min(l))
        print("Sum:",format(sum(l),','))
        print("Avg:",format(sum(l)/len(l),'.1f'))


if __name__ == '__main__':
    main()
