################################################################################
# Author: Fanyang Cheng
# Date: 2/24/2021
# This program asks user for a number and send back the answer whether it is
# a prime number or not.
################################################################################
def is_prime(n):    #define function is_prime.
    #use a loop to test all of the reserves devided by the number less than
    #the input.
    judge = 1  #give a judgement parameter.
    if n == 1:    #give 1 a specific case as range would not be applicable to it.
        judge = 0
    else:
        for i in range(1,round((n-1)**0.5+1)):
            if not(n%(i+1)) and n != i+1:  #if in this turn it has a remain of 0 and it is not the number itself.
                judge = 0   #then change the judgement to "not prime".
    return bool(judge) #well, we can directly return judge but it is a boolean function so return the boolean value.
                          # 1 for Ture, it is a prime number. 0 for false, it is not a prime number.

    return True  # If only 1 and n meet the need, then it is a prime number.

def main():   #define main function.
    inp = int(input("Enter a positive integer (-1 to quit): "))
    while inp != -1:    #check if input is -1
        p = is_prime(inp)  #else check for the prime or not.
        if p:
            print(inp,"is a prime number.")
        else:
            print(inp,"is not a prime number.")
        inp = int(input("Enter a positive integer (-1 to quit): "))

if __name__ == '__main__':
    main()   #run.
