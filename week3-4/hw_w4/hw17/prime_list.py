################################################################################
# Author: Fanyang Cheng
# Date: 2/26/2021
# This program asks user for a number and send back all the prime numbers from 2
# to that number.
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
def main():    #def the main function
    pl = []   #create a list
    num = int(input("Enter a positive integer: ")) #ask for input.
    for i in range(num):    #give the judge for each numbers
        pri = is_prime(i+1)   #have the judgement
        if pri == True:
            pl.append(i+1)  #if it is prime, append to the pl list.
    pl = ", ".join(str(i) for i in pl)   #change the list to string so that won't print brackets.
    print("The primes up to",num,"are:",pl)  #output

if __name__ == "__main__":
    main()  #run
