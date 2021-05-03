################################################################################
# Author: Fanyang Cheng
# Date:03/24/2021
# Description: This program get one input from user in string and return the
# pig-string as output.
################################################################################
# define the function pig
def pig(i):
    i = i.lower() #set the input string to lower letter.
    l = i.split() #change the string into a list with words.
    for j in range(len(l)):
        l_s = list(l[j])
        f = l_s.pop(0) # pop the first letter out for each word
        l_s.append(f)
        l_s.append("ay")
        l[j] ="".join(l_s)
    o = " ".join(l)  #re-construct the string.
    o = o.capitalize()
    return(o)
def main():
    inp = input("Enter a string: ")
    outp = pig(inp)
    print(outp)

if __name__ == '__main__':
    main()
