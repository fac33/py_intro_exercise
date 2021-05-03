################################################################################
# Author: Fanyang Cheng
# Date: 2/11/2021
# This program calculates the discount and
#money of purchase of the discounted software.
################################################################################
n = int(input("Please input the number of packages to be purchased: ")) #let user to input their required amount.
m = 0 #preset the money user need to pay.
#determin the discount and total price for each case and print them to user.
#specifically, as the discount amount would not need to change within eacch case,
#there is no need to set a variable for it. Otherwise directly print it to user.
if n<0:
    print("  Invalid Input!")
elif n<=9 and n>=0:
    m = 99*n
    print("  No discount applied.")
    print("  The final price for purchasing ",n," packages is $",format(m,',.2f'),".",sep = "")
elif n<=19 and n>=10:
    m = 99*n*0.9
    print("  10% discount applied.")
    print("  The final price for purchasing ",n," packages is $",format(m,',.2f'),".",sep = "")
elif n<=49 and n>=20:
    m = 99*n*0.75
    print("  25% discount applied.")
    print("  The final price for purchasing ",n," packages is $",format(m,',.2f'),".",sep = "")
elif n<=99 and n>=50:
    m = 99*n*0.65
    print("  35% discount applied.")
    print("  The final price for purchasing ",n," packages is $",format(m,',.2f'),".",sep = "")
else:
    m = 99*n*0.55
    print("  45% discount applied.")
    print("  The final price for purchasing ",n," packages is $",format(m,',.2f'),".",sep = "")
