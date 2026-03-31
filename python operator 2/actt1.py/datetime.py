import random
import time
def getrandomdate(startdate,enddate):
    print("generating a random date.....")
    randomgenerator=random.random()
    dateformat="%m/%d/%Y"
    startdate=time.mktime(time.strptime(startdate,dateformat))
    enddate=time.mktime(time.strptime(enddate,dateformat))
    randomtime = startdate+ randomgenerator * (enddate - startdate)
    return randomtime
print(getrandomdate("1/1/2016","12/12/2018"))