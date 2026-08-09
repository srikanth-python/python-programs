##functions :-
#keyswords and positional arguments
'''def details(id,name,email):
    id=10
    name="sri"
    email="sri@24.com"
    print(id,name,email)
details(id="id",name="name",email="email")'''
#keyword arguments the order is not important in the positional arguments order is important
#position arguments must come before keyword arguments
'''def details(id,name,email):
    id=10
    name="sri"
    email="sri@24.com"
    print(id,name,email)
details(10,name="name",email="email")'''
    
'''def details(id,name,email):
    id=10
    name="sri"
    email="sri@24.com"
    print(id,name,email)
details(id="id",sri,email="email")#error'''

'''def details(id,name,email):
    print(id,name,email)
details(id="id",name="name",email="email")    
details(10,"sri","sri@23")
details(id=4,name="sri",email="sri@23")
details("sri",4,"sri@33")
details(name="sri",email="sri@23",id=5)'''


#default arguments :-
'''def grocery(item,price):
    print("item is %s"%item)
    print("price is %.2f"%price)
grocery("rice",200)    


def grocery(item,price):
    print("item is ",item)
    print("price is",price)
grocery("rice",200)'''



'''def grocery(item,price=200):
    print("item is %s"%item)
    print("price is %.2f"%price)
grocery("rice",200)'''    

'''def grocery(item="rice",price=200):
    print("item is %s"%item)
    print("price is %.2f"%price)
grocery()'''    


'''def grocery(item="rice",price):
    print("item is %s"%item)
    print("price is %.2f"%price)
grocery(200) #error '''


#*arguments(* is used to unpack the elemnts)
'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)


a=(2,3,4,5,6,7,8)
print(a)
print(*a)

a={2,3,4,5,6,7,8}
print(a)
print(*a)

d={"name":"srikanth","year":2026,"section":"c"}
print(d)
print(*d)'''

#* holds only keys in the dictionary

'''a,b,c=1,2,3,4,5,6,7
print(a)
print(b)
print(c)#error 

a,b,c=1,2,3
print(a)
print(b)
print(c)

a,b,*c=1,2,3,4,5,6,7
print(a)
print(b)
print(*c)'''

'''a,b="codegnan"
print(a)
print(b)#error


a,*b="codegnan"
print(a)
print(*b)'''


#variable length arguments :-
#a variable length argument allows a function to accept any number of arguments .it is useful when you don't know in advance how many values will be passed.
#there are two types :-
#1.*args(variable-lengh positional arguments)collects multiple positional arguments into tuple
#datatype is tuple
'''def check(*a):
    print(a)
    print(type(a))
check()


def check(a):
    print(a)
    print(type(a))
check(10)

def check(a):
    print(a)
    print(type(a))
check(10,20)#error'''

'''def check(*a):
    print(a)
check(10,20,30,40,50)
b=[1,2,3,4,5,6,7]
check(*b)
d={"name":["sri","ram","sai"],"rollno":[1,2,3]}
check(*d)'''

#2.**kwargs(variable-length keywords)
#**collects multiple keyword arguments into dictionary
'''def details(**a):
    print(a)
    print(type(a))
details()'''

'''def details(**b):
    print(b)
details(name="sri",rollno=45,section="c") '''

'''def check(**g):
    print(g)
d={"name":["sri","ram","sai"],"rollno":[2,3,4],"section":["A","B","C"]}
check(**d)'''

#both * and ** usages
'''def final(*a,**b):
    d=2
    print(a)
    print(type(a))
    print(b)
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is ",i)
        print("value is",j)
#final()
data=(2,3,4,5,6,7,8)
#final(*data)
d={"name":["sri","ram","sai"],"rollno":[2,3,4],"section":["A","B","C"]}
#final(**d)
final(*data,**d)'''

#global and local variables
#first case of global variables
'''a=4
def check1():
    print("inside value is",a)
check1()
print("outside value is",a)'''

#second case of global variable
'''a=5
def check2():
    a=7
    a=a**2
    print("inside value is",a)
check2()
print("outer the value is",a)'''

#third case of both global and local variables
'''a=5
def check3():
    a=7
    print("inside value is",a)
    a=10
    print("updated value is ",a+5)
    
check3()
print("outside value is",a)
    
    



a=5
def check3():
    a=7
    print("inside value is",a)
    a=10
    print("updated value is ",a+5)
    b=12
    b=b+a
    print("value of b is",b)
check3()
print("outside value is",a)
#print("outside value is",b) error this line'''

#global variable usage
'''a=5
def final():
    global a
    print("inside value is",a)
    a=10
    print("updated value is",a)
    b=15
    b=b+a
    print("value is b",b)
final()
print("value of a is ",a)'''


'''def final():
    a=20
    global a
   
    print("inside value is",a)
final()
print("outside value is",a)#error'''


'''def final():
    global a
    a=40
    print("inside value is",a)
final()
print("outside value is",a) '''

#Generators :-
#syntax :-
#a=(expr for var in collection/range)
a=(i for i in range(21))
print(a)
print(*a)
print(type(a))
#without * generators will not be work
#in generator we should *arguments otherwise the datatype
#print(list(a))
#print(tuple(a))
#print(set(a))

#for dictionary it will not work because of it is key value pairs

'''a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''        


'''a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        
        a=a+1
        return a
print(check(a,b))'''        

#return v/s yield
'''def mygen():
    #return "vija"
    #return "hyder"
    #return "vzg"
    return "vija","hyd","vzg"

print(mygen())'''

'''def mygen():
    #return "vija"
    #return "hyder"
    #return "vzg"
    return "vija","hyd","vzg"
#to unpack it we should use *
print(*mygen())'''

'''def mygen():
    yield "python"
    yield "java"
    yield "dsa"
print(*mygen())
#next build in function
d=mygen()
print(next(d))
print(next(d))
print(next(d))'''

#eval()
'''while True:
    a=eval(input("enter the number:"))
    b=eval(input("enter the number:"))
    print(a+b)'''

#zip()->we can combine multiple colletions into one collections
'''a=[10,20,30,40,50]
names=["sri","ram","sai","rammma","teja"]
print(a+names)

c=zip(a,b)
print(c)#error while using the build in functions we should use datatype or *

c=list(zip(a,names))
print(c)

d=tuple(zip(a,names))
print(d)

e=set(zip(a,names))
print(e)

f=dict(zip(a,names))
print(f)'''

#enumerate()->we can give counter to the collections
'''name=["sri","ram","ramma","sai","money"]
for i in range(len(name)):
    print(i,name[i])
b=list(enumerate(name,1))#1 is starting number that your wise to give from where wants to start

print(b)

e=dict(enumerate(name,101))
print(e
    

f=set(enumerate(name,200))
print(f)'''



#ascii
#chr(),#ord()
'''print(chr(65))

#ord()
print(ord("a"))'''

#annonymous functions
#syntax:
#a=lambda argument:expression
'''a=lambda x:x**2+5
print(a(2))

a=lambda x,y:x*y
print(a(2,4))

a=lambda x,y,z:x*y**z
print(a(2,3,4))'''

'''a="codegnan"
b=lambda a:a.upper()
print(b(a))

a=lambda a:a.upper()
print(a("codegnan"))'''

#filter():-
'''a=[10,20,30,40,50,60]
for i in a:
    if i%2==0:
        print(i)

b=list(filter(lambda x:x%2==0,a))
print(b)
b=set(filter(lambda x:x%2==0,a))
print(b)
c=set(filter(lambda i:i%2!=0,a))
print(c)
      

        
a=[[],(),{},set(),"python",2,4.9,True,False]
b=list(filter(None,a))
print(*b) '''      

#map():-
'''a=[2,30,40,5,60]
b=[6,7,8,90,10]
c=list(map(max,a,b))
print(c)'''

#runtime_inputs formats
#string runtime format
'''a=input("enter the name")
b=input("enter the name")
print(a+b)'''

'''a,b=input("enter the names=").split(",")
print(a+b)'''

'''a,b=[x for x in input("enter the name=").split(",")]
print(a+b)'''

'''a,b=(x for x in input("enter the names=").split(","))
print(a+b)'''

'''a,b=map(str,input("enter the names=").split(","))
print(a+b)'''

#integer runtime inputs
'''a=int(input("enter the values="))
b=int(input("enter the values="))
print(a+b)'''

'''a,b=int(input("enter the value=").split(","))
print(a+b)#error'''

'''a,b=[int(x) for x in input("enter the values=").split(",")]
print(a+b)'''

'''a,b=[float(x) for x in input("enter the values=").split(",")]
print(a+b)


a,b=[complex(x) for x in input("enter the values=").split(",")]
print(a+b)

a,b=(int(x) for x in input("enter the values=").split(","))
print(a+b)'''

'''a,b=map(int,input("enter the values").split(","))
print(a+b)

a,b=map(complex,input("enter the values").split(","))
print(a+b)'''


#list runtime formats
'''a=list(map(int,input("enter the values=").split(",")))
print(a)'''
       
'''b=tuple(map(eval,input("enter the values=").split(",")))
print(b)'''

#dictionary runtime inputs
#map is not work
a=input("enter the keys and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)















    
    
