################################################################################
# Author: Fanyang Cheng
# Date: 2/12/2021
# This program converts input of seconds into
#day(s), hour(s), minute(s) and second(s) if needed.
################################################################################
#ask user for input in second.
i = int(input("Please enter a time in seconds. "))
#then start the conversion structure.
if i <60:  #less than a min.
    print("  The number of seconds is less than one minute.") #output
elif i>=60 and i<3600:   #less than an hour.
    s = int(i%60)   #give the number of seconds.
    m = int((i-s)/60) #give the number of minutes.
    #output
    if s == 0:
        print("  ",format(i,',')," seconds is: ",m," minute(s).",sep = "")
    else:
        print("  ",format(i,',')," seconds is: ",m," minute(s) and ",s," second(s).",sep = "")
elif i>=3600 and i<86400:    #less than a day.
    s = int(i%60)    #give the number of seconds.
    m = int(((i-s)%3600)/60)   #give the number of minutes.
    h = int((i-m*60-s)/3600)   #give the number of hours.
    #output
    if m == 0 and s == 0:
        print("  ",format(i,',')," seconds is: ",h," hour(s).",sep = "")
    elif s == 0:
        print("  ",format(i,',')," seconds is: ",h," hour(s) and ",m," minute(s).",sep = "")
    elif m == 0:
        print("  ",format(i,',')," seconds is: ",h," hour(s) and ",s," second(s).",sep = "")
    else:
        print("  ",format(i,',')," seconds is: ",h," hour(s), ",m," minute(s) and ",s," second(s).",sep = "")
else:
    s = int(i%60)    #give the number of seconds.
    m = int(((i-s)%3600)/60)   #give the number of minutes.
    h = int(((i-m-s)%86400)/3600)  #give the number of hours.
    d = int((i-h*3600-m*60-s)/86400)   #give the number of days.
    #output
    if s == 0 and m == 0 and h == 0:
        print("  ",format(i,',')," seconds is: ",d," day(s).",sep = "")
    elif s == 0 and m == 0:
        print("  ",format(i,',')," seconds is: ",d," day(s) and ",h," hour(s).",sep = "")
    elif s == 0 and h == 0:
        print("  ",format(i,',')," seconds is: ",d," day(s) and ",m," minute(s).",sep = "")
    elif m == 0 and h == 0:
        print("  ",format(i,',')," seconds is: ",d," day(s) and ",s," second(s).",sep = "")
    elif s == 0:
        print("  ",format(i,',')," seconds is: ",d," day(s), ",h," hour(s) and ",m," minute(s).",sep = "")
    elif m == 0:
        print("  ",format(i,',')," seconds is: ",d," day(s), ",h," hour(s) and ",s," second(s).",sep = "")
    elif h == 0:
        print("  ",format(i,',')," seconds is: ",d," day(s), ",m," minute(s) and ",s," second(s).",sep = "")
    else:
        print("  ",format(i,',')," seconds is: ",d," day(s), ",h," hour(s), ",m," minute(s) and ",s," second(s).",sep = "")
