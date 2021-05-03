print("Please enter the following quantities.")
P = float(input("  How much is the initial deposit? "))
r = float(input("  What is the annual interest rate in percent? "))/100
n = float(input("  How many times per year is the interest compounded? "))
t = float(input("  How many years will the account be left to earn interest? "))
FV = P*((1+r/n)**(n*t));
print("")
print("At the end of ",t," years, the account will be worth $",format(FV,',.2f'),".",sep = "")
