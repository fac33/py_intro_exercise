################################################################################
# Author: Fanyang Cheng
# Date: 2/23/2021
# This program asks user to enter two numbers and gives back the greater one.
################################################################################
def max_of_two(a,b):        # define the function max_of_two.
    m = max(a,b)            # find the max one. Here we directly use the built in function, or we can use if statement.
    return m
def main():                 # define main function
    a = int(input("Enter the first integer: ")) #ask for first integer
    b = int(input("Enter the second integer: "))#ask for the second integer.
    max = max_of_two(a,b) #call function max_of_two.
    print(max,"is greater.")      #print output.

if __name__ == '__main__':
    main()  # run
