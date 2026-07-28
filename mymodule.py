#MODULES

'''def greetings(name):
    print("Welcome",name)'''

'''
a=4
b=5
print(a+b)'''


'''
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print(a+b)
'''

'''
details={"idnos":[10,20,30],
         "names":["poojitha","varshitha","chaitra"],
         "marks":[60,70,80]}
'''

'''
if __name__=="__main__":  #by writing this line the code will not be converted into module & it will stay as a script only
    a=[10,20,30,40]
    a.append("code")
    a.extend("code")
    print(a)
'''

'''
def dummy():
    if __name__=="__main__":
        print("This program run as script")  #it will stay as a script only because it is inside this "__name__=="__main__" " block.
    else:
        print("This program run as module")   #it will execute as a module because it is written outside this "__name__=="__main__"" block.

dummy()
'''


#math module
'''
import math
print(math.pi)
print(math.pi+9)
print(math.pi*3)
print(math.sqrt(2))
print(math.log(2))
print(math.tan(45))
print(math.cos(60))
print(math.sin(30))
print(math.pow(2,4))
print(math.ceil(4.6))
print(math.floor(8.11))
'''

#by using "from" keyword we can import packages at a time
'''
from math import pi,sqrt,log,tan
print(pi)
print(sqrt(4))
print(log(6))
print(tan(90))
'''

#sys module->
'''
import sys
print(sys.version)
print(sys.path)
'''


#os module
'''
import os
print(os.path)
print(os.getcwd())   #the current directory will be printd
print(os.listdir())  #list of directies will be printed
print(os.chdir("C:\\Users\\poojitha\\Downloads"))
print(os.listdir())  #prints all list of dir in the Downloads
'''

#random module->it is used to generate a random numbers in python,randint function is used & this function is defines in random module.
#examples->otp generation,verification codes,passwords,ludo games,games

#random module
#sample->prints some random numbers within the given range & how many numbers we want to print
'''
import random
a=random.sample(range(10,50),10)
print(a)


#randint()->used to print a single random value within the given range
import random
a=random.randint(10,30)
print(a)


#choice()->it print the single random value from the given list of values
a=[10,20,30,40,50]
b=random.choice(a)
print(b)
'''


#Task-->Dice Game
'''
import random
while True:
    input("Enter the role of dice:")
    a=random.randint(1,6)
    print(a)

    option=input("Roll again? (y/n)")
    if option=="y":
        continue
    elif option=="n":
        break
    else:
        print("Invalid Option")

'''


#calender module

'''
import calendar
year=2026
mon=8  #we have to give numericals only
print(calendar.month(year,mon))
'''

'''
import calendar
year=2027
print(calendar.calendar(year))
'''

'''
import calendar
year=int(input("Enter the year:"))
print(calendar.calendar(year))
'''

'''
import calendar
year=int(input("Enter the year:"))
mon=int(input("Enter the mon:"))
print(calendar.month(year,mon))
'''

#datetime module
'''
from datetime import date
a=date.today()
print(a)
'''

'''
import datetime
a=datetime.datetime.now()
print(a)
'''


#time
'''
import time
a=time.time()
print(a)  #epoch time (from 1970 jan 1 to now)
b=time.localtime(a)  #coverte into local time
print(b)
#converting into human readable format
print(f"Today date is:{b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"Now the time is:{b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"day is:{b.tm_mday}-{b.tm_yday}-{b.tm_isdst}")
'''


#Task
'''
import random
import time

for i in range(10):
    a=random.randint(100,200)
    print(a)
    time.sleep(1)   #it will hold some time between two printings statements
'''


    

















































