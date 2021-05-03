################################################################################
# Author: Fanyang Cheng
# Date: 2/16/2021
# This program ask for the number of years and then repeatedly ask for the
# rainfall rate for each month. Finally gives out the amount of month, rainfall
# and monthly average rainfall.
################################################################################
mon = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"] #preset for months' name.
total,raf,rat = 0,0,0  #other presets.
y = int(input("Enter the number of years: ")) #ask for number of year.
# one condition structure to figure out if the input is less than one.
if y<1:
    print("Invalid input.")
else:
    for i in range(y):    #first loop (outer loop for year.)
        print("  For year No.",i+1)
        for j in mon:     #second loop (1st inner loop for each month.)
            while True:  # third loop (2nd inner loop to make sure the rainfall is non-negative)
                print("    Enter the rainfall for ",j,".: ",sep = '',end = '')
                raf = float(input(""))
                if raf>=0:
                    break
                else:
                    print("    Invalid input, please try again.")
            rat+=raf   #calculate the total rainfall inches.
    mon_t = 12*y #total number of months
    avg_r = rat/mon_t  #average rainfall inches each month.
    print("There are", mon_t,"months.")
    print("The total rainfall is",format(rat,'.2f'),"inches.")
    print("The monthly average rainfall is",format(avg_r,'.2f'),"inches.")
