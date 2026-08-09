#List comprehension:
'''
#a=["CODEGNAN","PYTHON","COURSE"]
b=str(a)
print(b.upper())

for i in a:
    print(i.upper(),end=" ,")

b=[]
for i in a:
    b.append(i.upper())
print(b)

#syntax
#a=[expression for var in collection\range]

a=[i.upper() for i in a]
print(a)


a=["vja","hyd","vizag"]
#[Vja","Hyd","Vizag"]
b=[i.title() for i in a]
print(b)


a=[1,2,3,5,6,8,12,13]
a=[i*i for i in a]
a=[i**2 for i in a]
a=[pow(i,2) for i in a]
print(a)

#if-usage in list comprehension
a=[i for i in range(16) if i%2==0]
print(a)

a=[i for i in range(16) if i%2!=0]
print(a)

a=[i for i in range(1,21)]
print(a)


fruits=["apple","banana","grapes","kivi","mango","dragon","berry"]
a=[i for i in fruits if "a" in i]
print(a)



fruits=["apple","banana","grapes","kivi","mango","dragon","berry"]
a=[i for i in fruits if "a" not in i]
print(a)

#no-elif usage in list comprehension
#if-else usage in list comprehension
a=[i*i if i%2==0 else i*5 for i in range(21)]
print(a)


a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
    a=[a[i]+b[i] for i in range(5)]
a=[a[i]+b[i] for i in range(len(a))]
print(a)'''




'''for i in range(1,11):
    print(i)


i=1
while i<=10:
    print(i)
    i+=1'''

'''i=10
while i>=1:
    print(i)
    i-=1

for i in range(10,0,-1):
    print(i)

a=[1,2,3,4,5,6,7,8,9]
a=[i*i if i%2==0 else i*5 for i in a]
print(a)'''

#practise :-
'''a=["fruits","mango","grsphes","orange","kivi"]
a=[i for i in a if "a"in i]
print(a)


a=["srikanth","mango","banana","sairam"]
a=[i.upper() for i in a]
print(a)

#a=[i*i for i in range(1,21)]
#a=[i**2 for i in range(1,21)]
a=[pow(i,2) for i in range(1,21)]
print(a)


a=[1,2,3,4,5,6]
b=[6,5,4,3,2,1]
a=[a[i]+b[i] for i in range(6)]
print(a)'''

#ATM application
'''card=input("Insert the card=")
password=int(input("enter the password="))
option=int(input("choose the option 1.Balance_enq 2.withdrawal"))
Balance_enq=100000
withdrawal=int(input("enter the withdrawal amount="))
                
if card=="c":
    print("welcome srikanth")
else:
    print("Invalid card")
if password==123:
    print("correct password")
else:
    print("incorrect password")
if Balance_enq>=withdrawal:
    balance=Balance_enq-withdrawal
    print("withdrawal is successfully")
else:
    print("founds are insufficient")
print("remaining balance=",balance)'''


'''num=int(input("enter the number:"))
temp=num
rev=0
while num>0:
    rev=rev*10+num%10
    num//=10

if temp==rev:
     print("palindrome")

else:

    print("not a palindrome")'''



#ATM application
'''while True:
    account=100000
    pwd=1234
    card=input("insert the card=")
    if card=="c":
        print("welcome srikanth")
        password=int(input("enter the password="))
        if password==pwd:
            option=int(input(choose the option
                                 1.balance enq
                                 2.withdraw))
            if option==1:
                print("your acc bal is",account)
            elif option==2:
                money=int(input("enter the amount="))
                print(money)
                balance=account-money
                print("remaining balance=",balance)
            else:
                print("Invalid option")
        else:
            print("Incorrect password")
    else:
        print("Invalid card")'''


'''#count vowels in string
name=input("enter a string:")
count=0
for i in name:
    if i in "aeiouAEIOU":
        count+=1
print("number of vowels:",count)  '''

 #fibonacci series
'''num=int(input("enter the number:"))
a=0
b=1
for i in range(num+1):
    print(a,end=" ")
    a, b=b ,a+b'''

'''a=[i for i in range(20)]
print(a)

a=[i if i%2==0 else i*5 for i in range(20)]
print(a)


a=[1,2,3,4,5,6,7,8,9]
b=[pow(i,2) for i in a]
print(b)'''

'''a=[i for i in range(20) if i%2==0]
print(a)

a=[2,3,4,5,6,7]
b=[7,6,5,4,3,2]
a=[a[i]+b[i] for i in range(len(a))]
print(a)'''





























    


    
    
             











