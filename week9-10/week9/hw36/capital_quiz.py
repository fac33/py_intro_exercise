################################################################################
# Author: Fanyang Cheng
# Date: 02/04/2021
# Description: This program asks user question about the capital of each states.
################################################################################
#define the get_state_data function
def get_state_data():
    cont_l = []
    with open('state_capitals.txt','r') as str:
        for line in str:
            ele = line.rstrip()
            ele = ele.split(', ')
            ele[0],ele[1] = ele[1],ele[0]  #swap the order of states and their capitals
            cont_l.append(ele)
        cont = dict(cont_l)
        return(cont)
def main():
    info = get_state_data() #get the information pair.
    keys = list(info.keys())#get the states' names
    all,corr,ans = 0,0,0 #set the counter and answer recorder.
    #now ask for the questions in a while loop so it could continuously asking.
    while True:
        st = keys[0]
        ans = input("What is the capital of "+st+" (enter 0 to quit)? ")
        if ans == "0":
            print("You answered",corr,"out of",all,"questions correctly.")
            break
        ans = ans.lower()
        #gudge if the input is correct.
        if ans == info.get(st).lower():
            mark = info.pop(st,-1)
            del keys[0]
            print("That is correct!")
            all+=1
            corr+=1
        else:
            mov = keys[0]
            del keys[0]
            keys.append(mov)
            print("That is incorrect.")
            print("The capital of ",mov," is ",info.get(mov),".",sep = '')
            all+=1
        if not keys:
            print("You answered",corr,"out of",all,"questions correctly.")
            break

if __name__ == '__main__':
    main()
