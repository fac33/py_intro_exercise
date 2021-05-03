################################################################################
# Author:Fanyang Cheng
# Date:27/03/2021
# Description: This file read one sepcific text file and track the number of words
#, number of lines and the average words per line.
################################################################################

def main():
    with open('rumpelstiltskin.txt','r') as fo:
        cont = fo.read()
        cont_l = cont.split("\n")   # split by enter.
        l_n = len(cont_l)
        while not (cont_l[-1]):   #at the end of file, if there are several blank lines, then delete them.
            l_n -= 1
            cont_l.pop()
        cont_wm = " ".join(cont_l)
        cont_wt = cont_wm.split(" ")   # split by blank
        cont_w = [i for i in cont_wt if i]    #delete the '' item in the list created by split method.
        w_n = len(cont_w)
        avg = w_n/l_n
        print("Total number of words:",w_n)
        print("Total number of lines:",l_n)
        print("Average number of words per line:",format(avg,'.1f'))

if __name__ == '__main__':
    main()
