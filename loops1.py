#while loop()->continous iterations
'''a=10
while a>1:
    print(a)

a=10
while a>1:
    print(a)
    a=a-1

a=10
while a>=1:
    print(a)
    a=a-1

a=10
while a>1:
    a=a-1
    print(a)'''
    
'''a=20
while a>5:
    a=a-1
print(a)

a=30
while a>2:
    print(a)
    a+=1

a=30
while a>2:
    print(a)
    a-=1

#voting  while loop real time use
while True:
    age=int(input("enter the age:"))
    if age>=18:
    
        print("eligible")
    else:
        print("not eligible")'''

#range() :-
#the function return a sequence of numbers, and start from 0 by default incerment by 1 and stop the before value.
#start-stop-step
'''for i in range(10):
    print(i)
for i in range(5,15):
    print(i)
for i in range(30,45):
    print(i,end=",")'''

'''for i in range(2,20,2):
    print(i,end=",")

for i in range(5,50,5):
    print(i,end=",")'''
    
'''for i in range(0,30,3):
    print(i,end=",")

#grades tasks
while True:
    marks=int(input("enter the marks:"))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range(81,91):
        print("Grade-B")
    elif marks in range(71,81):
        print("Grade-C")
    elif marks in range(61,71):
        print("Grade-D")
    elif marks in range(51,61):
        print("Grade-E")
    else:
        print("fail,study well for next time")


while True:
    marks=int(input("enter the marks:"))
    for marks in range(91,101):
        print("Grade-A")

#Break
a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        break

a=30
while a>2:
    a=a-1
    if a==20:
        break
    print(a)

for i in range(40,65):
    if i==55:
        break
            
    
#continue
a=15
while a>3:
    print(a)
    a=a-1
    if a==11:
        continue

a=15
while a>3:
    
    a=a-1
    if a==11:
        continue
    print(a)

for i in range(18):
    if i==14:
        continue
    print(i)

a="python"
for i in a:
    if i=="t":
        continue
    print(i)'''

#pass
'''a=12
while a>4:
    print(a)
    a=a-1
    if a==10:
        pass

a=20
while a>10:
    print(a)
    a=a-1
    if a==15:
        pass'''


a=15
while a>3:
   
    a=a-1
    if a==11:
        continue
    print(a)
    
    























        
            
    






































    
