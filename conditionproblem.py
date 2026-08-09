#voting
'''age=int(input("enter the age:"))
if age>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")


#even or odd
num=int(input("enter the number:"))
if num%2==0:
    print("even")
else:
    print("odd")


#leap years
year=int(input("enter the year:"))
if year%4==0:
    print("leave year")
else:
    print("not a leave year")

#guest code
name=input("enter the name:")
if name=="srikanth":
    print("welcome",name)
else:
    print("welcome guest")


name=input("enter the name:").lower()
if name=="srikanth":
    print("welcome",name)
else:
    print("welcome guest")


#for multiple users
names=["sri","ram","sai","sriram","ramesh"]
a=input("enter the name:").lower()
if a in names:
    print("welcome",a)
else:
    print("welcome guest")



#vowels
letter=input("enter the letter:").lower()
if letter in "aeiou":
    print("vowel")
else:
    print("consonant")


vowels=["a","i","e","o","u"]
letter=input("enter the letter:")
if letter in vowels:
    print("it is vowel")
else:
    print("it is consonant")

#social-media login
#By using nexted if
username=input("enter the username:")
password=int(input("enter the password:"))
if username=="srikanth":
    if password==810654:
        print("login successful")
else:
    print("invalid credentials")

    


username=input("enter the username:")
password=int(input("enter the password:"))
if username=="srikanth":
    if password==810654:
        print("login successful")
    else:
        print("incorrect password")
else:
    print("invalid username")


username=input("enter the username:")
password=input("enter the password:")
if username=="srikanth" and password=="sri@123":
    print("login successful")
else:
    print("invalid credentials")


#multiple-if conditions
#student credentials
age=int(input("enter the age:"))
marks=int(input("enter the marks"))
attendence=int(input("enter the attendence:"))
if age>18:
    print("eligible for vote")
if marks>=80:
    print("eligible for scholarship")
if attendence>80:
    print("eligible for exams")


age=int(input("enter the age:"))
marks=int(input("enter the marks"))
attendence=int(input("enter the attendence:"))
if age>18:
    print("eligible for vote")
else:
    print("not for vote")
if marks>=80:
    print("eligible for scholarship")
if attendence>80:
    print("eligible for exams")


#cake
price=int(input("enter the price:"))
if price==1200:
    print("redveluet cake")
elif price==1000:
    print("almond cake")
elif price==1800:
    print("choclate")
elif price==600:
    print("betterscote cake")
else:
    print("cake is not available")

#Banking
age=int(input("enter the age:"))
if age<18:
    print("minor account")
else:
    print("major account")

#fertizer
price=int(input("enter the price:"))
if price==1200:
    print("urea")
if price==1300:
    print("dap")
if price==1400:
    print("mop")
if price==1500:
    print("sop")
if price==2000:
    print("potassium nitrate")
else:
    print("not available")

#hostel rooms
price=int(input("enter the price:"))
if price==8000:
    print("three sharing")
elif price==7000:
    print("four sharing")
else:
    print("room is not available")

#pizza
a=int(input("enter the pizza name:"))
if a=="bbq pizza":
    print(1000)
elif a=="cripy chicken pizza":
    print(1200)
elif a=="panner pizza":
    print(1300)
elif a=="chicken pizza":
    print(1400)


    
          
d={"year":2026,"month":"july","date":10}
for i in d:
    print(i)
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i)

#while loop():
a=10
while a>1:
    print(a)
    a=a-1

a=20
while a<100:
    print(a)
    a=a+1  

for i in range(1,6):
    print(i)

#break
a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        break'''


#continue
a=30
while a>3:
   
    a=a-1
    if a==20:
        continue
print(a)

    


    
    

   
        

    















































    
