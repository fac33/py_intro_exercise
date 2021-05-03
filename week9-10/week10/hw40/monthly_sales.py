################################################################################
# Author: Fanyang Cheng
# Date: 05/04/2021
# Description: This program asks user to input monthly sale data of a year and
#display them in a pie chart.
################################################################################
#define input function
def get_data():
    inp = []
    month = ['January','February','March','April','May','June','July','August','September','October','November','December']
    for i in month:
        am = int(input('Enter the sales for '+str(i)+': '))
        inp.append(am)
    return inp
def main():
    #import the matplotlib module.
    import matplotlib.pyplot as plt
    #get the list
    dat = get_data()
    fig,ax = plt.subplots()
    c = ('#4D4038','#BAA892','#5B6870','#6E99B4','#A3D6D7','#085C11','#849E2A','#C3BE0B','#E9E45B','#6B4536','#B46012','#FF9B1A') #colors
    l = ('January','February','March','April','May','June','July','August','September','October','November','December') #label
    ax.pie(dat,colors = c, labels = l)
    ax.set_title('Monthly Sales Values')
    plt.show()
if __name__ == '__main__':
    main()
    plt.show()
