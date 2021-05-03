################################################################################
# Author: Fanyang Cheng
# Date: 03/20/2021
# Description: This program asks user to input 10 floating point numbers and
# calculate for the max, min, average and sum of them.
################################################################################
# def the get_number_list function (in total 10 of them)
def get_number_list():
    l = []
    for i in range(10):
        inp = float(input("  Enter number "+str(format(i+1,'2'))+ " of 10: "))
        l.append(inp)
    return l
def main():
    li = get_number_list()
    print("Lowest number:",format(min(li),'.2f'))
    print("Highest number:",format(max(li),'.2f'))
    print("Total:",format(sum(li),'.2f'))
    print("Average:",format(sum(li)/len(li),'.2f'))



if __name__ == '__main__':
    main()
