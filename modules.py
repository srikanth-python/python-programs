
#module
'''def greetings(name):
    print("welcome",name)'''

'''a=9
b=6
print("the sum is",a+b)'''

'''a=int(input("enter the value="))
b=int(input("enter the value="))
print(a+b)'''

'''details={"idnos":[10,20,30],"name":["sri","ram","sai"],"marks":[80,90,70]}'''


'''def greeting(name,rollno):
    print(name,rollno)
greeting("sri",396)'''

'''if __name__=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    a.extend("code")
    print(a)'''

'''def dummy():
    if __name__=="__main__":
        print("this program is a script")
    else:
        print("this program is a module")
dummy()'''

'''def add():
    a=int(input("enter the name="))
    b=int(input("enter the value="))
    print(a+b)'''
'''def add():
    a=20
    b=30
    print(a+b)
add()'''


'''def add():
    a=20
    b=30
    print(a+b)'''
a={"name":"sri","rollno":34,"branch":"aiml"}

    
#math module
#it is used to calculate the mathemetical values
'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,2))
print(math.log(10))
print(math.tan(45))
print(math.cos(60))
print(math.sin(60))
print(math.ceil(4.9))
print(math.floor(6.9))
print(math.degrees(3))'''

#from
'''from math import pi,sqrt,log,tan,cos
print(pi)
print(sqrt(20))
print(log(20))
print(tan(45))
print(cos(60))
print(sin(60))'''



#sys module
#interacts with the python interpreter and system settings
'''import sys
print(sys.path)
print(sys.version)'''

'''import sys
print(sys.path)
print(sys.version)
print(sys.version_info)
print(sys.api_version)

print(sys.platform)
print(sys.exit())'''



#os module
#works with files and folders
#it allows your program to interact with the operating system.
'''import os)
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.chdir("C:\\Users\\Srikanth Konda\\Downloads"))
print(os.listdir())'''

'''import os
print(os.path)
print(os.getcwd())#current folder
print(os.listdir())#list files and folders
print(os.chdir("C:\\Users\\Srikanth Konda\\Downloads"))
print(os.listdir())'''
      




#random modules
#random modulu is used to generate random numbers in python , randint function is used and this function defined in random module.
#sample()
'''import random
a=random.sample(range(20,40),10)#10 is the no.of elements to print
print(a)'''

#randit()->it will print single value and the last number is also included
'''import random
a=random.randint(20,50)
print(a)'''

'''import random
a=random.randint(20,50)
print(a)'''

#choice()
'''import random
a=[10,30,20,40,50]
b=random.choice(a)
print(b)'''

#dice code
'''import random
while True:
    a=input("enter the roll of dice=")
    a=random.randint(1,6)
    print(a)
    option=input("roll again (y/n)")
    if option=="y":
        continue
    elif option=="n":
        break
    else:
        print("invalid options")'''
        



#calendar module
'''import calendar
year=2026
month=8
print(calendar.month(year,month))'''

'''import calendar
year=2026
print(calendar.calendar(year))'''

'''import calendar
a=int(input("enter the year="))
b=int(input("enter the month="))
print(calendar.month(a,b))'''
#calendar module
'''import calendar
year=2026
month=8
print(calendar.month(year,month))

import calendar
year=2026
print(calendar.calendar(year))'''



#datetime module
'''from datetime import date
a=date.today()
print(a)

import datetime
a=datetime.datetime.now()
print(a)'''


'''import time
a=time.time()
print(a) #epoch time

b=time.localtime(a)
print(b) #localtime

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")#human readable

print(f"time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")

print(f"day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''


'''import random
import time
for i in range(10):
    a=random.randint(90,100)
    print(a)
    time.sleep(2)'''

#error handling
#syntax error
'''for i in range(10):
    print(i)'''

#runtime_time error
'''a=int(input("a value="))
b=int(input("b value="))
print(a//b)''' #10//0->zero division error

#logical error
'''a=10
b=20
if a<b:
    print("true")'''

                                      
'''a=10
b=20
if a>b:
    print("true")#logical error '''


#exception handling
'''while True:
    try:
        a=int(input("enter the value="))
        b=int(input("enter the value="))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exception")
    finally:
        print("program ends")'''

#regular expressions(regex)
'''a="codegnan is in vija"
print(a)


a="codegnan\nis\tin\nvija"
print(a)
    

#rstring means unmodified or same
a=r"codegnan\nis\tin\nvija"
print(a)

#complie(),search(),findall(),split(),sub()
#sequence characters
\w->it matches alphanumeric
\W->it matches non-alphanumeric #special characters
\d->it matches any digit
\D->it matches non-digit
\s->it represents white space
\S->it represents non-white space'''

#compile()
import re
a="mat map cap cup money cash cat dog mug donkey maths"
'''b=re.compile(r"m\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)'''

'''c=re.search(r"m\w+",a)#search print only one letter
print(c)'''

#findall()
'''d=re.findall(r"m\w+",a)
print(d)

d=re.findall(r"m\w+",a)
print(*d)'''

#split()
'''e=re.split(r"m",a)
print(e)

f=re.split(r"\S",a)
print(f)'''

#sub
'''g=re.sub(r"m","a",a)
print(g)'''


#check weather the mobile number is valid(10 digits)
'''import re
mobile=input("enter mobile number:")
if re.fullmatch(r"\d{10}",mobile):
    print("valid mobile nuber")
else:
    print("invalid mobile number")'''



#$ ->end with string ex:world$
#^->start of string ex:^hello
#{n}->exactly n times Ex:/d{4}
#*->zero or more ex:ab*
#+-> one or more ex:ab+
#?->zero or one ex:ab?



























































































