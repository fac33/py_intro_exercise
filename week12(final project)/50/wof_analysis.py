###############################################################################
# Author: Fanyang Cheng
# Date: 05/03/2021
# Description: This program serves a conclusion of the character frequencies in
#the phrases.txt file and draw a bar chart to show the result.
###############################################################################
import numpy as np
import matplotlib.pyplot as plt
char_l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
time_l = np.zeros(26)
def main():
    with open('phrases.txt') as fo:
        l = fo.readlines()
        #factor out '\n' tailing
        for i in range(len(l)):
            l[i] = l[i].rstrip('\n')
        for j in l:
            temp_l = list(j)
            for k in range(len(temp_l)):
                for m in range(len(char_l)):
                    if char_l[m] == temp_l[k].upper():
                        time_l[m] = time_l[m] + 1
        #calculate frequency
        su = sum(time_l)
        for i in range(len(time_l)):
            time_l[i] = time_l[i]/su
        #then we start to draw the bar chart.
        fig,ax = plt.subplots()
        ax.bar(char_l,time_l)
        #set appearings
        ax.set_xlabel('Letter')
        ax.set_ylabel('Letter Appearance Frequency')
        ax.set_title('Letter Frequency in Puzzle Phrases')
        ax.grid() #add grid


if __name__ == '__main__':
    main()
    plt.show()
