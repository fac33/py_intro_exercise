################################################################################
# Author: Fanyang Cheng
# Date: 2/23/2021
# This program repeat ten times to calculate falling distance within ten seconds.
################################################################################
def falling_distance(time): #define the function falling_distance.
    d = 0.5*9.81*time**2   #calculate distance
    return d               # push back the result.

def main(): #define the main function
    print("Time (s)  Distance (m)")
    print("----------------------")    #print form title
    for i in range(10): #loop 10 times
        dist = falling_distance(i+1) #get the outcome from falling_distance
        print(format(i+1,'8'),format(dist,'13.2f')) #print each line for each turn

main()   #run
