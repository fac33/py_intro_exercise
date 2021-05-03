################################################################################
# Author: Fanyang Cheng
# Date: 04/04/2021
# Description: This program get the input file of Xian_1 and Xian_2, and outputs
#four files about the words' frequency and the words in common as well as the Words
#in difference.
################################################################################
#prepare for environment
import string as s
#predefine two functions
def get_word_list(file):  #return the word list.
    l_l = []  #line list.
    with open(file,'r') as x1:
        for line in x1:
            l_l.append(line.rstrip())
        l_a = " ".join(l_l)
        w_l_r = l_a.split(" ") #raw word list without factor out '' and punctuation.
        w_l_aw = [i for i in w_l_r if i] #now it is all words but containing punctuation.
        for i in range(len(w_l_aw)):
            w_l_aw[i] = w_l_aw[i].strip(s.punctuation).lower() #remove punctuations.
        return(w_l_aw)
#get list as input and return the dictionary about appearing frequency.
def get_freq(list):
    keys = set(list)
    dict = {}
    for i in keys:
        dict[i] = list.count(i)
    return(dict)

def main():
    #deal with Xian_1
    l1 = get_word_list('xian_1.txt') #the key list
    l1.sort()
    dic1 = get_freq(l1) #the frequency dictionary
    with open('xian_1_word_frequency.txt','w') as fre:
        for i in sorted(dic1.keys()):
            s = i+": "+str(dic1[i])+"\n"
            fre.write(s)

    #deal with Xian_2
    l2 = get_word_list('xian_2.txt')
    l2.sort()
    dic2 = get_freq(l2)
    with open('xian_2_word_frequency.txt','w') as fre:
        for i in sorted(dic2.keys()):
            s = i+": "+str(dic2[i])+"\n"
            fre.write(s)
    #now deal with the intersection and difference of the words.
    s1 = set(l1)
    s2 = set(l2)
    l_int = list(s1&s2)
    l_int.sort()
    l_dif = list(s1^s2)
    l_dif.sort()
    with open('common_words.txt','w') as com:
        for i in l_int:
            com.write(i+"\n")
    with open('eitherbutnotboth.txt','w') as dif:
        for i in l_dif:
            dif.write(i+"\n")


if __name__ == '__main__':
    main()
