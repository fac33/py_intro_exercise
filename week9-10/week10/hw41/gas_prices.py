################################################################################
# Author: Fanyang Cheng
# Date: 04/07/2021
# Description: This program read the weekly gas average price txt file as input
# and draw a graph for to show the data.
################################################################################
import matplotlib.pyplot as plt
#read file
def get_data():
    data = []
    with open('2008_Weekly_Gas_Averages.txt','r') as dat:
        for line in dat:
            data.append(float(line.rstrip())) #use the float conversion to get the data.
    return data
def main():
    dat = get_data()
    fig,ax = plt.subplots()
    week = range(1,len(dat)+1)     #week's number should start from 1
    ax.plot(week,dat)
    ax.grid()   #put the grid on
    ax.set_title('2008 Weekly Gas Prices')    #set labels
    ax.set_xlabel('Weeks (by number)')
    ax.set_ylabel('Average Price (dollars/gallon)')
    ax.set_xlim(1,len(dat))   #set the limits.
    ax.set_ylim(1.5,4.25)

if __name__ == '__main__':
    main()
    plt.show()
