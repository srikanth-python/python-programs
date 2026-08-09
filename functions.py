#functions
'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)


def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)

def calculate(a,b):
    print("the pow is",a**b)
    print("the modules is",a%b)
    print("the integer division is",a//b)
calculate(10,20)
calculate(2,4)
calculate(5,8)

def add(4,6):
    print(a+b)
add(4,6)    

while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()

def add():
     a=int(input("a value"))
     b=int(input("b value"))
     print(a+b)
     add()
add()

def fullname():
    fname=input("first name")
    lname=input("last name")
    print((fname+" "+lname).title())
fullname()


#print vs return
def mul(a,b):
    print(a*b)
mul(4,6)

def mul(a,b):
    return a*b
print(mul(6,8))

#print vs return
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
cal(4,6)

def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
    return c,d,e
print(cal(2,3)) 


#splitbill()
def splitbill():
    a=int(input("enter the total members:"))
    b=int(input("enter the amount:"))
    print("per the person bill is:",b//a)
splitbill() 

def splitbill():
    a=int(input("enter the total memders:"))
    b=int(input("enter the amount:"))
    c=b//a
    print("per the person bill is {}".format(c))
splitbill()

    
def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the amount"))
    c=b//a
    print(f"per person is {c}")
splitbill()   

def splitbill():
    a=int(input("enter the total memders:"))
    b=int(input("enter the amount:"))
    
    print("per the person bill is {}".format(b//a))
splitbill()'''

'''def cal():
    a=int(input("enter:"))
    b=int(input("enter1:"))
    print(a+b)
    cal()
cal()'''

'''def calculate():
    a=int(input("enter the 1:"))
    b=int(input("enter the 2:"))
    option=int(input(choose the option
                           1.addition
                           2.substract
                           3.multiplication ))
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    elif option==3:
        print(a*b)
    else:
        print("invalid option")
    calculate()    
calculate()        

    
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
    a=int(input("enter the 1:"))
    b=int(input("enter the 2:"))
    option=int(input(choose the option
                           1.addition
                           2.substract
                           3.multiplication))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()'''

#keywords and positional arguments
'''def details(id,name,email):
    id=10
    name="sri"
    email="sri@23.com"
    print(id,name,email)
details(id="id",name="name",email="email")



def details(id,name,email):
    print(id,name,email)
details(id="id",name="name",email="email")
details(id=20,name="sri",email="sri@gamil.com")
details(40,"sri","sri@gmail.com")
details("sri@gmail.com",20,"srikanth")
details(email="sri@23",id=20,name="srikanth")'''

#default arguments
'''def Grocery(item,price):
    print("item is %s"%item)
    print("price is %.2f"%price)
Grocery("rice",200)    
   
    
    
def Grocery(item="sugar",price=200):
    print("item is %s"%item)
    print("price is %.2f"%price)
Grocery()


def Grocery(item,price=200):
    print("item is %s"%item)
    print("price is %.2f"%price)
Grocery("rice")  '''  
   
   

#important
'''def Grocery(item="sugar",price):
    #non def arg follows def arg
    print("item is %s"%item)
    print("price is %.2f"%price)
Grocery(200)    
   

def Grocery(item,price):
    print("item is :",item)
    print("price is:",price)
Grocery("rice",200)'''



'''def cake(cake_name,price,qty):
    print("cake name is :",cake_name)
    print("price is :",price)
    print("qty is :",qty)
cake("choclate",200,"400ml")'''

'''def cake(cake_name,price=300,qty="500g"):
    print("cake name is :",cake_name)
    print("price is :",price)
    print("qty is :",qty)
cake("choclate")'''

    

'''def cake(cake_name="choclate",price,qty):
    print("cake name is :",cake_name)
    print("price is :",price)
    print("qty is :",qty)
cake(price,qty)'''


#* arguments (* is used to unpack the elements)
'''a=[10,20,30,40,50]
print(a)
print(*a)


b=(5,6,7,8,9)
print(b)
print(*b)


c={6,7,8,9,10}
print(c)
print(*c)'''

'''d={"name":"srikanth","year":2026,"month":7}
print(d)
print(*d)#(* holds keys only)

a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8
print(a)
print(b)
print(c)#error'''

'''a,b,*c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(*c)


*a,b,c=2,3,4,5,6,7,8,9
print(*a)
print(b)
print(c)

a,*b,c=2,3,4,5,6,7,8,9
print(a)
print(*b)
print(c)

a,b,c="codegnan"
print(a)
print(b)
print(c)#error'''

'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)

a,*b,c="codegnan"
print(a)
print(*b)
print(c)


a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''

#variable length arguments
'''def check (*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8,9)
b=[2,3,4,5,6,7,8]
check(*b)
c={2,3,4,5,6,7,8}
check(*c)
d={"year":2026,"month":7}
check(*d)



#kwargs(**)
def details(**a):
    print(a)
    print(type(a))
details()
d={"name":["sri","sai","sampath"],"rollno":[2,3,4]}
def details(**a):
    print(a)
    print(type(a))'''


#both * and ** usage
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,6,7,8,9)
final(*data)
d={"name":["sai","ram","sri"],"rollno":[3,4,5],"students":["p","a","p"]}
final(**d)
final(*data,**d)'''

#railway ticket applications
'''while True:
    def railway_ticket():
        ticket=1000
        gender=input("enter the gender:")
        age=int(input("enter the age:"))
        if gender=="male":
            if age>=60:
                print("senior citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                print(ticket)
        if gender=="female":
            if age>=60:
                print("senior citizen")
                ticket=ticket-50/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
    railway_ticket()  '''              
            

         
                   

#global and local variables
#first case of global variable
'''a=3
def check1():
    print("inside value is",a)
check1()
print("outside value is",a)


#second case of global variable
a=4
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)'''

#third case of both global and local variables
'''a=5
def check3():
    a=7
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=4 #local variable
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
#print("b value is ",b)'''


#usage of global variable
'''a=5
def final():
    global a
    print("inside value is",a)
    a=10
    print("updated value is",a)
    b=15
    b=b+a
    print("value of b",b)
final()
print("value of a is",a)'''


#attendence tracking report
'''students=int(input("enter the students"))
p=0
a=0
for i in range(1,students+1):
    attendence=input(f"student{i} (p/a)")
    
    if attendence=="p":
        p+=1
    elif attendence=="a":
        a+=1
print("total students=",students)
print("total presenties=",p)
print("total absenties=",a)'''

#Generators:-
#a=[expr for var in collections/range]
'''a=[i for i in range(21)]
print(a)
print(type())'''

#syntax
#a=(exprs for var in collection/range)
'''a=(i for i in range(21))
print(a)
print(type(a))
print(*a)

print(list(a))
print(tuple(a))
print(set(a))'''
#inthe generators we should use * or data type any one
#no dictionary

'''a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        yield a
        a=a+1
        #yield a
print(*check(a,b)) '''

'''
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))'''

#yield v/s return
'''def mygen():
    #return "vija"
    #return "java"
    #return "dsa"
    return "vija","hyd","vzg"
print(mygen())


def mygen():
    #return "vija"
    #return "java"
    #return "dsa"
    return "vija","hyd","vzg"
print(*mygen())'''


'''def mygen():
    yield "python"
    
    yield "java"
    yield "dsa"
    
print(*mygen())    

#next()
#d=mygen()
#print(next(d))
#print(next(d))
#print(next(d))

a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))#error
#fromkeys()
b=dict.fromkeys(a)
print(b)
c=dict.fromkeys(a,"sri")
print(c)

c["d"]="sam"
print(c)'''


#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''



'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)


while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''


'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''


#zip()->we can combine multiple collections into one collection
'''a=[10,20,30,40,50]
names=["sri","ram","sai","ramma","teja"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)'''

#enumerate()->we can give counter to the collections
'''names=["mythri","darshini","sarvani","teja","srivarna"]
for i in range(len(names)):
    print(i,names[i])

b=dict(enumerate(names))
print(b)

b=dict(enumerate(names,1))
print(b)

b=list(enumerate(names,1))
print(b)'''

#ASCII
#chr(),ord()

'''print(chr(65))

print(chr(90))

#print(chr("a"))

#ord()
print(ord("a"))
print(ord("z"))
#print(ord(56))'''

#print A to Z
'''for i in range(65,91):
    print(chr(i),end=" ")
print()
for i in range(97,123):
    print(chr(i),end=" ")'''

'''a=input("enter the name:")
for i in a:
    print(i,ord(i))'''

#max(),min(),sum()
'''print(max(2,3,4,5,6,7,8,9))
print(min(2,3,4,5,6,7,8,9))
#print(sum(2,3))#error


a=2,3,4,5,6,7,8,9
print(sum(a))'''


#annonymous functions(nameless functions)
'''def cal():
    x=5
    sum=2*x+5
    print(sum)
cal()'''


'''def f():
    x=int(input())
    print(2*x+9)
f() '''

#syntax:
#a=lambda arg:expression

'''a=lambda x:2*x+5
print(a(5))


a=int(input())
b=lambda x:2*x+5
print(b(a))'''

#take 2 arguments and multiply it
'''a=lambda x,y:x*y
print(a(3,4))

a=int(input())
b=int(input())
c=lambda a,b:a*b
print(c(a,b))'''

#a="codegnan"
#CODEGNAN
'''a="codegnan"
b=lambda a:a.upper()
print(b(a))

a=lambda a:a.upper()
print(a("codegnan"))


b="python course"
c=lambda a:a.title()
print(c(b))'''

#firstname+lastname=fullname
'''fname=input("first name")
lname=input("last name")
fullname=lambda fname,lname:(fname+" "+lname).title()

print(fullname(fname,lname))'''


'''fname,lname=(str(x) for x in input("enter the name").split(","))
fullname=lambda fname,lname:(fname+" "+lname).title()

print(fullname(fname,lname))'''


#filter()
#a=[10,20,30,40,45,5,55,65,75]

'''for i in a:
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda x:x%2==0,a))
print(b)

b=list(filter(lambda x:x%2!=0,a))
print(b)'''


'''a=[[],(),set(),{},"",None,3,4.5,5+7j,"sri",True,False]
b=list(filter(None,a))
print(b)'''

#map()->each object from a collection and forms a new collections
'''a=[2,4,6,8,9,10,20,30,50]
b=[1,3,5,6,11,12,14,15,7]
c=list(map(max,a,b))
d=list(map(min,a,b))
print(c)
print(d)'''



#run_time input formats
#string runtime formats
'''a=input("data 1=")
b=input("data 2=")
print(a+b)'''

'''a,b=input("enter the data").split(",")
print(a+b)'''

'''a,b=[x for x in input("enter data").split(",")]
print(a+b) '''#list comprehension


'''a,b=(x for x in input("enter data").split(","))
print(a+b)#generators


a,b=map(str,input("enter teh value").split(","))
print(a+b)'''
#in map must mention the data type


#integer runtime formats
'''a=int(input("a value="))
b=int(input("b value="))
print(a+b)

a,b=[int(x) for x in input("enter the values").split(",")]
print(a+b)


a,b=(int(x) for x in input("enter the values").split(","))
print(a+b)


a,b=int(input("enter the values").split(","))
print(a+b) #error

a,b=map(int,input("enter the value").split(","))
print(a+b)'''

#list runtime format
'''a=list(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a=list(map(eval,input("enter the values").split(",")))
print(a)'''


#tuple runtime format
'''a=tuple(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

#if we need different runtime inputs in list,tuple use the eval in the datatype 
#set runtime format
'''a=set(map(int,input("enter the values").split(",")))
print(a)'''


#dictionary runtime format
#map is not work for dictionary
'''a=input("enter the key and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)'''



#spilbill
def spiltbill():
    a=int(input("enter the total amount="))
    b=int(input("enter the total numbers="))
    print(a/b)
spiltbill()













        
       



































































