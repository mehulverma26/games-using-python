import time
from time import time as the_timer
import datetime
import random
d='yes'
while d=='yes' or d=='y' or d=='Yes':
    now=datetime.datetime.now()
    print(str(now))
    print("current year: {}".format(now.year))
    print("current month: {}".format(now.strftime("%B")))
    print("current day: {}".format(now.strftime("%A")))
    print("current hour: {}".format(now.strftime("%H")))
    print("current minutes: {}".format(now.strftime("%M")))
    input("please press enter to start")
    wait_time=random.randint(1,6)
    time.sleep(wait_time)
    start_time=the_timer()
    input("please press enter to stop")
    end_time=the_timer()
    print("Started at "+time.strftime("%X",time.localtime(start_time)))
    print("Ended at "+time.strftime("%X",time.localtime(end_time)))
    print("Your reaction time was {}".format(end_time-start_time))
    d=str(input("do you want to try again?(y/n)"))
if d=='no' or d=='n' or d=='No':
    print("thank you :)")