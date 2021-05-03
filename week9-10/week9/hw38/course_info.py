################################################################################
# Author: Fanyang Cheng
# Date: 04/04/2021
# Description: This program allows user to input a course number and return its
# room, instructor and time.
################################################################################
# define function get_course_data
def get_course_data():
    c_d = {'CS101':{'room':'3004','instructor':'Haynes','time':'8:00 a.m.'},
           'CS102':{'room':'4501','instructor':'Alvarado','time':'9:00 a.m.'},
           'CS103':{'room':'6755','instructor':'Rich','time':'10:00 a.m.'},
           'NT110':{'room':'1244','instructor':'Burke','time':'11:00 a.m.'},
           'CM241':{'room':'1411','instructor':'Lee','time':'1:00 p.m.'}}
    return c_d
def main():
    data = get_course_data() #get dataset
    req = input("Enter a course number: ")#ask user for class number.
    det = data.get(req,-1)
    if det == -1:
        print(req,"is an invalid course number.")
    else:
        print("The details for course",req,"are:")
        print("  Instructor:",det["instructor"])
        print("        Room:",det["room"])
        print("        Time:",det["time"])


if __name__ == '__main__':
    main()
