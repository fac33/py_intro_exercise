################################################################################
# Author: Fanyang CHeng
# Date: 04/10/2021
# Description: This program plot a sin and a cos wave on the canvas.
################################################################################
import matplotlib.pyplot as plt
import math as m
def main():
    y_s,y_c,x = [],[],[]  #define the x axis and sin&cos functions.
    u = range(0,100+1) #in total 100 points
    for i in u:
        x.append(2*m.pi*i/len(u))
        y_s.append(m.sin(2*m.pi*i/len(u)))
        y_c.append(m.cos(2*m.pi*i/len(u)))
    fig,ax = plt.subplots()
    ax.plot(x,y_s,c = 'red')
    ax.plot(x,y_c,c = 'blue')
    #then we start spine setting.
    for spine in ['top','right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom','left']:
        ax.spines[spine].set_position('zero')
    #then set the ticks
    ax.set_xticks([25*2*m.pi/len(u),50*2*m.pi/len(u),75*2*m.pi/len(u),100*2*m.pi/len(u)])
    ax.set_xticklabels(['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$'])
    ax.set_yticks([-1,1])

if __name__ == '__main__':
    main()
    plt.show()
