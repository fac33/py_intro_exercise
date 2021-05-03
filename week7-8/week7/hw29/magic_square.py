################################################################################
# Author:Fanyang Cheng
# Date:03/20/2021
# Description:This program get the 3*3 squre and determine if it is Lo Shu square.
################################################################################
#define print_square and is_magic funtion
def print_square(l):
    for i in l:
        i_t = [str(x) for x in i] #change to str list
        print(" ".join(i_t))
def is_magic(l):
    #first, the 3*3 matrix should contain exactly 1 to 9.
    cont = [] #generate a containing list.
    for i in l:
        for j in i:
            cont.append(j) #push every containing into this number_list
    cont.sort()
    # check from 1 to 9
    for k in range(9):
        if k+1 != cont[k]:
            return False
    #next, check for the in total 15 requirement.
    sum_h,sum_v,sum_d1,sum_d2 = 0,0,0,0  #temp sum
    for i in range(3):
        for j in range(3):
            sum_h = sum_h+l[i][j]
            sum_v = sum_v+l[j][i]
        if sum_h !=15 or sum_v != 15:
            return False
        sum_h,sum_v = 0,0 #reset the horizontal and vertical sum.
        sum_d1 = sum_d1+l[i][i]
        sum_d2 = sum_d2+l[2-i][i]
    if sum_d1 != 15 or sum_d2 != 15:
        return False
    return True
def main():

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    m3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    L = [m1,m2,m3] #answer list
    for i in L:
        print("Your square is:")
        print_square(i)
        jud = is_magic(i)
        if jud:
            print("It is a Lo Shu magic square!\n")
        else:
            print("It is not a Lo Shu magic square.\n")

if __name__ == '__main__':
    main()
