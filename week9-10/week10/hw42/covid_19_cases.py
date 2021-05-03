################################################################################
# Author:Fanyang Cheng
# Date:04/09/2021
# Description: This program read the data from indiana_covid_19_data file add
# make a bar chart to show them.
################################################################################
import matplotlib.pyplot as plt
import datetime
import math as m
#define the read function
def get_data():
    with open('indiana_covid_19_data.txt','r') as dat:
        an,date,test,pos,die = [],[],[],[],[]
        for line in dat:
            an.append(line.rstrip())
        for i in an:
            sep = i.split(' ')
            date.append(sep[0])
            test.append(int(sep[1]))
            pos.append(int(sep[2]))
            die.append(int(sep[3]))
        return(date,test,pos,die)  #return all the info contained in the txt file.
def main():
    date,test,pos,die = get_data()
    x = []
    poss = pos.copy() #the cumulative positive cases for each day.
    for i in range(len(poss)):
        poss[i] = poss[i]/1000   #devide by 1000
    for i in range(len(poss)-1):
        poss[i+1] = (poss[i]+poss[i+1])
    fig,ax = plt.subplots() #start draw the graph
    for d in date:
        y,m,da = d.split('-')
        dt = datetime.date(int(y),int(m),int(da))
        x.append(dt)
    ax.bar(x,poss)
    ax.set_title('Positive COVID-19 Cases in Indiana')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Cases (in thousands)')
    fig.autofmt_xdate()

if __name__ == '__main__':
    main()
    plt.show()
