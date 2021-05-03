V = int(input("How many cookies do you want to make? "))
rate = V/48
s = 1.5*rate
b = rate
f = 2.75*rate
print("To make",V,"cookies, you will need:")
print(format(s,'7.2f'),"cups of sugar")
print(format(b,'7.2f'),"cups of butter")
print(format(f,'7.2f'),"cups of flour")
