################################################################################
# Author: Fanyang Cheng
# Date:02/19/2021
# Description: Use the gaved list and one gaved specific number to find the element
# in the list which could be divided by the given number.
################################################################################
# define multiple_of function
def multiples_of(n,l):
    ind = 0 #position of list
    num_a = 0 #numbers of replaced a.
    for i in l:
        if i%n:
            l[ind] = 'a'
            num_a+=1
        ind+=1
    for j in range(num_a):
        l.remove('a')
    return l
def main():

    number_list = [19, 2940, -189, 10, 28, -58, 1, 85, 201, -15, 122, 799, 406] #set the list
    print("Original list of numbers:")
    print(number_list)
    print("Numbers in the list that are multiples of 7:")
    li_m = multiples_of(7,number_list)
    print(li_m)

if __name__ == '__main__':
    main()
