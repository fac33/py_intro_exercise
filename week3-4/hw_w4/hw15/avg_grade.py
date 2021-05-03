################################################################################
# Author: Fanyang Cheng
# Date: 2/23/2021
# This program asks user for five grads,gives the letter grade and calculate
# average.
################################################################################
def get_valid_score():      #define get_valid_score.
    while True:             # start the asking loop.
        s = float(input("Enter a score: ")) #ask for input.
        if s<=100 and s>=0:
            break                         #meet the need, stop asking.
        print("Invalid Input. Please try again.") #or give the warning.
    return s      # return output.
def calc_average(l):    #define the function calc_average. And the l is a list, which would allow any amount of scores.
    s = sum(l) #give the sum of all scores.
    avg = s/len(l)  #then the average.
    return avg         # return result.
def determine_grade(s):     #define determine_grade.
    #a typical if-elif structure.
    if s<=100 and s>=90:
        return "A"
    elif s<90 and s>=80:
        return "B"
    elif s<80 and s>=70:
        return "C"
    elif s<70 and s>=60:
        return "D"
    else:
        return "F"
def main():      #define main function.
    score = []  #define a list to store score.
    for i in range(5):    #give five scores
        s = get_valid_score()
        lg = determine_grade(s)  #find the letter grade.
        print("The letter grade for ",format(s,'.1f')," is ",lg,".",sep = "") # show the letter grade.
        score.append(s)  #add the grade into score list.
    avg = calc_average(score)  #calculate average score.
    print("The average score is ",format(avg,'.2f'),".",sep = "")

if __name__ == "__main__":
    main()  #run.
