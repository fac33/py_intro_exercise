################################################################################
# Author: Fanyang Cheng
# Date: 2/12/2021
# This program calculates Reynolds number based on
# water velocity, pipe's diameter and temperature.
################################################################################
# ask user for the input of water velocity, pipe's diameter and temperature.
v = float(input("Enter the velocity of water in the pipe: "))
d = float(input("Enter the pipe's diameter: "))
c = float(input("Enter the temperature in °C as 5, 10, or 15: "))
# calculate kinematic viscosity.
if c == 5:
    k = 1.49*10**(-6)
elif c == 10:
    k = 1.31*10**(-6)
else:
    k = 1.15*10**(-6)
#calculate Reynolds number.
Re = (v*d)/k
#output
print("The Reynolds number for flow at ",v," m/s in a ",d," m diameter pipe at ",c,"°C is ",format(Re,'.2e'),".",sep = "")
