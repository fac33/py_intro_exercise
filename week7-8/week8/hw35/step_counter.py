################################################################################
# Author:Fanyang Cheng
# Date:27/03/2021
# Description: This program read the step conting file to read the user's steps
# for each day and calculate average steps for each month.
################################################################################

def main():
    #preset for the amount of days for each month.
    md_n = [31,28,31,30,31,30,31,31,30,31,30,31]
    month = ['January','February','March','April','May','June','July','August','September','October','November','December']
    s = []  #this is the content holder.
    add = []#this is the sum step of each month
    with open('steps.txt','r') as step:
        temp_sum = 0
        for line in step:
            s.append(int(line.rstrip()))
        s.reverse()
        for i in range(len(md_n)):
            for j in range(md_n[i]):
                temp_sum = temp_sum+s.pop()
            add.append(temp_sum)
            temp_sum = 0 #reset to zero
        for i in range(len(add)):
            add[i] = add[i]/md_n[i]
        print("The average steps taken each month were:")
        for i in range(len(md_n)):
            print("{:>{}}".format(month[i],'10'),":",format(add[i],'.1f'))

if __name__ == '__main__':
    main()
