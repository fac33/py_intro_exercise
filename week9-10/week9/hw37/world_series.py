################################################################################
# Author: Fanyang Cheng
# Date: 04/03/2021
# Description:This program asks user about the of one specific year between 1903
# and 2020 and returns the name of the winning team and the total amount the team
# won.
################################################################################
#define load_winners_data
def load_winners_data():
    c = 1902 #count for the year to insert default values.
    win_l,data = [],[]  #list contains the winner team's name
    with open('WorldSeriesWinners.txt','r') as win:
        for line in win:
            data.append(line.rstrip())
        data.reverse()
        wink = set(data)   #we do not need the one include -1 version.
        for line in range(len(data)+2):  #create the list with all the outcomes of the winner including 1904 and 1994.
            c+=1
            if c == 1904 or c == 1994:
                win_l.append(-1)
            else:
                win_l.append(data.pop())
        dic2 = dict(zip(range(1903,2021),win_l)) #the second diction returned.
        dic2.pop(1904)
        dic2.pop(1994)
        dic1 = {}
        for i in wink:
            dic1[i] = win_l.count(i)
        return(dic1,dic2)


def main():
    dic1,dic2 = load_winners_data()
    inp = int(input("Enter a year in the range 1903 -- 2020: "))
    if inp<1903 or inp>2020:
        print("Data for the year",inp,"is not included in this system.")
    elif inp == 1904 or inp == 1994:
        print("The World Series wasn't played in the year ",inp,".",sep = '')
    else:
        winner = dic2[inp]
        print("The ",winner," won the World Series in ",inp,".",sep = '')
        print("They have won the World Series",dic1[winner],"times.")


if __name__ == '__main__':
    main()
