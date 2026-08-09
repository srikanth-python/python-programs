'''for i in range(1,11):
    print(i)


i=1
while i<=10:
    print(i)
    i+=1

i=10
while i>=1:
    print(i)
    i-=1

for i in range(10,0,-1):
    print(i)

for i in range(1,50):
    if i%2==0:
        print(i)


for i in range(1,50):
    if i%2!=0:
        print(i)

num=int(input())
for i in range(1,11):
    print(f"{num}X{i}={num*i}")'''

#sum of n numbers:-
'''sum=0
for i in range(1,101):
    sum+=i
print("sum=",sum)


i=1
sum=0
while i<=100:
    sum+=i
    i+=1
print("sum=",sum)

#factorial

num=int(input())
fac=1
for i in range(5,0,-1):
    fac*=i
    i-=1
print("factorial=",fac)

n=int(input())
i=1
fact=1
while i<=n:
    fact*=i
    i+=1
print("factorial=",fact)

count=0
a="12345"
for i in a:
    count+=1
print(count)


#reversing a number
num=int(input())
rev=0
while num>0:
    rev=rev*10+num%10
    num//=10
print("Reverse=",rev) 


#fibnocii series
num=int(input("enter the number:"))
a=0
b=1
for i in range(1,num+1):
    print(a,end=" ")
    a,b,a+b 


#largest of three numbers
a=int(input("enter the number1"))
b=int(input("enter the number2"))
c=int(input("enter the number3"))
if a>=b and a>=c:
    print("a largest number")
elif b>=a and b>=c:
    print("b largest number")
else:
    print("c largest number")
    

a=int(input("enter the number1"))
b=int(input("enter the number2"))
c=int(input("enter the number3"))

print("largest=",max(a,b,c))


num=int(input("enter the number:"))
count=0
while num>0:
    num//=10
    count+=1
   
print("number of digits=",count)

#sum of digits
num=int(input("enter the number"))
sum=0
while num>0:
    sum+=num%10
    num//=10
print("sum of digits:",sum)

#prime number check
num=int(input("enter the number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")

#sum of first n term
num=int(input())
sum=0
for i in range(1,num+1):
    sum+=i
print("sum=",sum)

#simple calculator
while True:
    a=int(input())
    b=int(input())
    operator=input()
    if operator=="+":
        print(a+b)
    elif operator=="-":
        print(a-b)
    elif operator=="*":
        print(a*b)
    elif operator=="%":
        print(a%b)
    elif operator=="//":
        print(a//b)
    else:
        print("invalid")'''


#reverse the string
'''a=input()
for i in a:
    b=a[::-1]
print(b)

a=input()
rev=" "
for i in a:
    rev=i+rev
print(rev) 


a=[10,30,20,80,40,50]
a.sort()
print("second largest number",a[-2])

 #anagram
s1=input()
s2=input()
if sorted(s1)==sorted(s2):
    print("anagram")
else:
    print("not anagram")

#perfect numbers
while True:
    num=int(input())
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        print("perfect number")
    else:
        print("not perfect number")

#strong number
while True:
    num=int(input())
    tempt=num
    sum_fact=0
    while num>0:
        digit=num%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum_fact+=fact
        num//=10
    if sum_fact==tempt:
        print("strong number")
    else:
        print("not a strong number")


#armstrong number
while True:
    num=int(input())
    tempt=num
    digits=len(str(num))
    sum_power=0
    while num>0:
        digit=num%10
        num1=digit**digits
        sum_power+=num1
        num//=10
    if tempt==sum_power:
        print("armstrong number")
    else:
        print("not a armstrong number")



#gcd
a=int(input())
b=int(input())
while b !=0:
    a, b = b, a % b
print("gcd =",a)  '''  
        
        
#sum of cubes program using the loops
'''num=int(input())
sum_cubes=0
for i in range(1,num+1):
    cubes=i**3
    sum_cubes+=cubes
print("sum of cubes=",sum_cubes)

#lcm of two numbers in the python
a=int(input())
b=int(input())
x=a
y=b
while y!=0:
    x,y=y,x%y
lcm=(a*b)//x
print("LCM=",lcm)

#pattern programs in the python
rows=5
for i in range(rows):
    for j in range(rows):
        print("*",end=" ")
    print()      
    
rows=int(input("enter the rows:"))
for i in range(rows):
    for j in range(rows):
        print("*",end=" ")
    print()  
        
#right triangle
rows=int(input())
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=" ")
    print() 
#inverted right triangle
rows=int(input())
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end=" ")
    print() 


#pyramid pattern
rows=int(input())
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print() 
       
        
        

#inverted pyramid
rows=int(input())
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()   '''


#Diamond programs
#upper pyramid
'''rows=int(input())
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
#lower pyramid    
for i in range(rows-1,0,-1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()  '''

#hollow square in the python
'''rows=int(input())
for i in range(rows):
    for j in range(rows):
        if i==0 or i==rows-1 or j==0 or j==rows-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print ()       


#hallow triangle
rows=int(input())
for i in range(1,rows+1):
    for j in range(1,i+1):
        if i==1 or i==rows or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   '''

#list comprehension
#syntax:-[expreesion for variable in collection\range]
'''a=["srikanth","srinu","prabhas","laddu"]
a=[i.upper() for i in a]
print(a)

a=["srikanth","srinu","prabhas","laddu"]
a=[i.title() for i in a]
print(a)
   

a=["srikanth","srinu","prabhas","laddu"]
a=[i.capitalize() for i in a]
print(a)'''


'''a=[1,2,3,4,5,6,7,8,9,10]
#a=[i*i for i in a]

#a=[i**2 for i in a]

a=[pow(i,2) for i in a]
print(a)

#if -usage in the list comprehension
a=[i for i in range(21) if i%2==0]
print(a)
a=[i for i in range(21) if i%2!=0]
print(a)

a=["apple","bananna","berry","kivi","orange","mango"]
a=[i for i in a if "a" in i]
print(a)

a=[i*i if i%2==0 else i*5 for i in range(21)]
print(a)'''

'''a=[2,3,4,5,6,7]
b=[7,6,5,4,3,2]
a=[a[i]+b[i] for i in range(6)]
print(a)'''

'''rows=int(input("enter the numbers:"))
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print() '''   

'''rows=5
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print() '''   

'''rows=5   
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(rows-1,0,-1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()  '''  

'''rows=int(input("enter the numbers:"))
for i in range(rows):
    for j in range(i):
        print(i,end=" ")
    print() '''

#reverse a string
'''a=input()
for i in range(a,0,-1):
    print(a)#error because the range accepts only integers not a variables '''

'''a=input()
b=a[::-1]
print(b)'''

'''a=input()
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")'''

#check wether a string is a palindrome or not
'''a=input("Enter the name:")
if a==a[::-1]:
    print("palindrome")
else:
    print("not a palindrome")'''

'''a=input()
rev="" #should not use the space between in the quotes because it will come the space " madam" then it become error
for i in range(len(a)-1,-1,-1):
    rev+=a[i]
if a==rev:
    print("palindrme")
else:
    print("not a palindrme")'''
#count the vowels and consonants of a string
'''a=input()
v=0
c=0
for i in a:
    if i.isalpha():
        if i in "aeiou":
            v+=1
        else:
            c+=1
print("vowels=",v)
print("consonants=",c)
    
    
    


a=input()
v=0
c=0
for i in a:
    if i in "aeiou":
        v+=1
    else:
        c+=1
print("vowels=",v)
print("consonants=",c)'''

'''a="srikanth"
for i in a:
    print(i)'''

#count uppercase,lowerrcase,digits,and special charaters
'''a=input()
u=0
l=0
d=0
s=0
for i in a:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isdigit():
        d+=1
    else:
        s+=1
print("uppercase=",u)
print("lowercase=",l)
print("digits=",d)
print("special character=",s)'''

#remove the spaces from the strings
'''a=input()
result=""
for i in a:
    if i!=" ":
        result+=i
print("string=",result)'''

#find the frequence of each characters
#frequence means how many times something occurs(appears or repeated)
#to find the frequency of each character in a string, use a dictionary
'''a=input()
freq={}
for i in a:
    if i in freq:
        freq[i]=+1
    else:
        freq[i]=1
print(freq) '''

#replace all space with -.
'''a=input()
print(a.replace(" ","-"))'''

#find the longest word in the setence
'''a=input()
words=a.split()
longest=words[0]
for word in words:
    if len(word)>len(longest):
        longest=word
print(longest) '''       

#count the number of words in the setences
'''a=input()
words=a.split()
count=len(words)
print("number  of words:",count)'''

#find the largest and smallest elements
'''a=[1,2,3,4,5,6,7,8,9]
b=max(a)
c=min(a)
print("largest value=",b)
print("smallestvalue=",c)'''


'''a=[3,5,6,2,9,7,8]
b=a.sort()
print(a[-1])
print(a[0])'''

#find the second largest number
'''a=[2,5,7,9,8,6,4,3]
b=a.sort()
print(a[-2])'''

#remove duplicates elements
'''a=[2,3,4,6,7,6,7,8,8,9,9]
b=set(a)
c=list(b) #b=list(set(a))
print(c)'''


'''a=[10,20,30,40,10,20,30]
result=[]
for i in a:
    if i not in result:
        result.append(i)
print(result)'''


#count even or odd numbers
'''a=[10,20,5,6,7,8,9,2]
even=0
odd=0
for i in a:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even=",even)
print("odd=",odd)'''

#reverse a list
'''a=[1,2,3,4,5,6]
#a.reverse()
#print(a)
print(a[::-1])'''


#sort a list without using sort()
'''a=[1,3,2,4,8,7,6]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)'''


#merge of lists
'''a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=a+b
print(c)'''


'''a=[1,2,3,4]
b=[5,6,7,8]
a.extend(b)
print(a)'''


'''a=[1,2,3,4]
b=[5,6,7,8]
c=[]
for i in a:
    c.append(i)
for i in b:
    c.append(i)
print(c)  '''

#find the common elements in two lists
'''a=[1,2,3,4,5]
b=[1,3,4,6,7]
c=[]
for i in a:
   if i in b:
       c.append(i)
print(c)'''


#find the sum and average of list
'''a=[1,2,3,4,5,6,7,8]
sum=0
for i in a:
    sum+=i
average=sum/len(a)
print("sum=",sum)
print("Average=",average)'''

'''a={1,2,3}
b={4,5,6}
if a.isdisjoint(b):
    print("disjoint set")
else:
    print("not disjoint set")'''

'''a=[1,2,3,4,2,3]
b=set(a)
print(b)'''

'''a={1,2,3,4}
b={3,4,5,6}
result=a.difference(b)
print(result)'''


#find unique elements in a list using a set
'''a=[1,2,3,4,5,6,7,8]
unique_elements=len(set(a))
print(unique_elements)'''


#Add and remove elements from a set
'''a=set()
a.add(2)
a.add(3)
a.add(4)
a.remove(4)
a.discard(2)
a.pop()
print(a)'''

#pyramid
'''rows=int(input("enter the number:"))
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()  '''


#merge two dictionaries.
'''a={"name":"sri","rollno":34}
b={"name1":"ram","rollno1":55}
a.update(b)
print(a)'''



'''a={"name":"sri","rollno":34}
b={"name1":"ram","rollno1":55}
c={**a,**b}
print(c)'''

#functions
'''def f():
    print("Hello,Welcome")
f()

def f():
    return "Hello,Welcome"
print(f())'''

#add two numbers and return result
'''def add():
    a=int(input("enter the value="))
    b=int(input("enter the value="))
    print("addition is=",a+b)
    add()
add() '''   


'''def add(a,b):
    print(a+b)
add(2,3)
add(8,9)'''

'''while True:
    def add():
        a=int(input("enter the number="))
        b=int(input("enter the number="))
        return (a+b)
        
    print(add())'''

#square of a number
'''def square(a,b):
    print(a**2,b**2)
square(2,3) '''   
    
'''def square():
    return num*num
num=int(input("enter the number="))
print(square())'''
    
'''def square(num):
    return num*num
n=int(input("enter the number="))
print(square(n))'''


#check weather the number is even or odd
'''def even_odd():
    a=int(input("enter the number="))
    if a%2==0:
        print("even number")
    else:
        print("odd number")
    even_odd()    
even_odd() '''

'''while True:
    def even_odd():
        a=int(input("enter the number"))
        if a%2==0:
            return "even number"
        else:
            return "odd number"
        
    print(even_odd()) '''


#find the maximum of two numbers
'''def max():
    a=int(input("enter the number="))
    b=int(input("enter the number="))
    if a>b:
        print("maximum number is=",a)
    else:
        print("maximum number is=",b)
    max()    
max()'''

#calculate the factorial of number
'''def factorial():
    fact=1
    a=int(input("enter the number="))
    for i in range(1,a+1):
        fact*=i
    print(fact)
    factorial()
factorial() '''   

        
'''while True:
    def factorial():
        fact=1
        a=int(input("enter the number="))
        for i in range(1,a+1):
            fact*=i
        return(fact)
        
    factorial()  '''

#round()
'''num=float(input())
print(round(num))
print(round(num,2))'''



#calculate the prime numbers
'''def prime_num():
    count=0
    num=int(input("enter the number="))
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print("prime number")
    else:
        print("not a prime number")
    prime_num()    
prime_num()  '''      
            
    

'''while True:
    def prime_num():
        count=0
        num=int(input("enter the number="))
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count==2:
            return("prime number")
        else:
            return("not a prime number")
        
    print(prime_num()) '''

'''def prime(num):
    if num<=1:
        return "not prime"
    for i in range(2,num):
        if num%i==0:
            return "not prime"
    return "prime"
num=int(input("enter the number="))
print(prime(num))'''

'''def vowels():
    name=input("enter the number=")
    v=0
    for i in name:
        if i in "aeiou":
            v+=1
    return v
print(vowels())'''

#reverse a string
'''def reverse():
    a=input("enter the number=")
    b=a[::-1]
    return b
print(reverse())'''

'''def reverse():
    rev=" "
    a=input("enter the string=")
    for i in a:
        rev=i+rev
    return rev
print(reverse())'''



#sum of elements in the list
'''a=[10,20,30,40,50]
sum=0
for i in a:
    sum+=i
print("the sum of list elements=",sum)'''

'''def list_sum():
    a=[10,20,30,40,50,60]
    total=0
    for i in a:
        total+=i
    print("the sum of list elements=",total)
list_sum()'''

#find the maximum element in a list
'''def list_elements():
    a=[10,20,30,40,50]
    print(max(a))
list_elements()'''    

        
#remove the duplicates in the list
'''a=[1,2,3,3,4,4,5,5]
b=list(set(a))
print(b)'''

'''def duplicate():
    result=[]
    a=[1,2,2,3,3,4,4,5,5,6]
    for i in a:
        if i not in result:
            result.append(i)
    print(result)
duplicate() '''

#calculate the sum of digits in the number
'''def calculate():
    total=0
    num=12345
    while num>0:
        digit=num%10
        total+=digit
        num//=10
    print(total)
calculate() '''

#merge two list using the functions
'''def merge():
    a=[1,2,3,4]
    b=[5,6,7,8]
    print(a+b)
merge() '''

'''def merge():
    result=[]
    a=[1,2,3,4,5]
    b=[6,7,8,9,10]
    for i in a:
        result.append(i)
    for i in b:
        result.append(i)
    print(result)
merge() '''

#find the common elements in the list
'''def common():
    a=[10,20,30,40,50]
    b=[20,10,30,60,70]
    result=[]
    for i in a:
        if i in b:
            result.append(i)
    yield result
print(*common())'''

#count the frequency of elements
'''def frequency():
    a=list(map(int,input("enter the values=").split(",")))
    freq={}
    for i in a:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    return freq
print(frequency())'''


#print pascal's triangle
'''row=int(input("enter the rows="))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()'''    
            

  
'''row=int(input("enter the rows="))
for i in range(row):
    num=1
    for j in range(row-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    print()'''


#functions hackerrank problems
'''def find_max(num):
    b=max(num)
    return b
a=[1,23,34,56,84]
c=[1,30,40,50,55]
print(find_max(a))
print(find_max(c))'''
        
#inside the function input is not reusable but the outside the function is reusable of code
'''def find_max():
    num=[10,20,30,40,50]
    b=max(num)
    return b
print(find_max())'''

#count vowels
'''def count_vowels(text):
    count=0
    for i in text:
        if i in "aeiou":
            count+=1
    return count
name="HACkERRANk".lower()
print(count_vowels(name))'''

#prime number
'''def is_prime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
        if count!=1:
            return "True"
        else:
            return "False"
num=17
b=6
print(is_prime(num))
print(is_prime(b))'''


#reverse a string
'''def reverse_string(text):
    rev=""
    for i in text:
        rev=i+rev
    return rev
name="python"
print(reverse_string(name))'''


#remove duplicates
'''def remove_duplicates(num):
    result=[]
    for i in num:
        if i not in result:
            result.append(i)
    return result
numbers=[1,2,2,3,1,4]
print(remove_duplicates(numbers))'''

#find the second largest number
'''def second_largest(nums):
    result=[]
    for i in nums:
        if i not in result:
            result.append(i)
    b=result[-2]
    return b
list=[10,20,30,40,40]
print(second_largest(list))'''

#sum of digits
'''def sum_digits(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n//=10
    return sum
number=548
print(sum_digits(number))'''


#count frequency of elements
'''def count_frequency(num):
    freq={}
    for i in num:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
list=[1,2,2,2,3,1,2]
print(count_frequency(list))'''

'''dict={"name":"srikanth","rollno":345}
#for i in dict:
print(dict["name"])
print(dict["rollno"])'''

#count vowels and consonants
'''def count_vc():
    a=input("enter the string=")
    v=0
    c=0
    for i in a:
        if i in "aeiou":
            v+=1
        else:
            c+=1
    print("consonants=",c)
    print("vowels=",v)
count_vc() '''

#reverse only the even numbers
'''def even():
    a=[1,2,3,4,5,6]
    result=[]
    for i in a:
        if i%2==0:
            result.append(i)
    b=result[::-1]
    print(b)
even() '''

#second largest number in a list without using the sort() function
'''def largest(num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]>num[j]:
                num[i],num[j]=num[j],num[i]

    reverse=num[-2]
    print(reverse)
list=[1,2,4,3,6,5,9]
largest(list)'''

#Alternating sum
'''def alternate_sum(num):
    total=0
    for i in range(1,num+1):
        if i%2==0:
            total-=i
        else:
            total+=i
    print(total)
number=int(input("enter the number="))
alternate_sum(number)'''

#ascending order
'''def ascending(num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if a[i]>a[j]:
                return "false"
            else:
                return "true"
a=list(map(int,input("enter the elements=").split(",")))

print(ascending(a))'''

#method2
'''def ascending(number):
    for i in range(len(number)-1):
        if number[i]>number[i+1]:
            return "false"
    return "true"
num=list(map(int,input("enter the number=").split(",")))
print(ascending(num))'''

#remove duplicates from characters
'''def duplicates(name):
    str=""
    for i in name:
        if i not in str:
            str+=i
    return str
num=input("enter the name=")
print(duplicates(num))'''

#find the common elements
'''def common_element(a,b):
    result=[]
    for i in a:
        for j in b:
            if i==j:
                result.append(i)
    print(result)
a=[1,2,3,4,5]
b=[6,7,8,4,5]
common_element(a,b)'''
#count positive ,negetive and zero numbers
'''def count_pnz(num):
    p=0
    n=0
    z=0
    for i in num:
        if i>0:
            p+=1
        elif i<0:
            n+=1
        else:
            z+=1
    print("positive=",p)
    print("negetive=",n)
    print("zeros=",z)
list=[1,2,3,4,5,0,0,-3,-4,-5,0,9,0,-1,-2]
count_pnz(list)'''

'''i=5
while i<10:
    i+=1
    print(i)
    #break
else:
    print("return")'''

'''for i in range(1,21):
    print(i)
else:
    print("return")'''
#pattern functions
'''def pattern(num):
    for i in range(1,num+1):
        for i in range(1,i+1):
            print(i,end="")
        print()    
            
         
num=5
pattern(5)'''

#password validator
'''def validate_password(password):
    upper=False
    lower=False
    digit=False
    if len(password)<8:
        print("invalid password")
    for i in password:
        if i.isupper():
            upper=True
        elif i.islower():
            lower=True
        elif i.isdigit():
            digit=True
    if upper and lower and digit:
        print("valid password")
    else:
        print("invalid password")
pwd=input("enter the password=")
validate_password(pwd)'''

#calculate the area of a triangle
'''base=float(input("enter the base of the triangle="))
height=float(input("enter the height of the triangle="))
area=0.5*base*height
print("Area of triangle=",area)'''

#exceptional handling
#write a program to divide two numbers using try and except 
'''try:
    num1=int(input("enter the number="))
    num2=int(input("enter the number="))
    result=num1/num2
    print("Result=",result)
except ZeroDivisionError:
    print("Error:cannot divide by Zero")
except ValueError:
    print("Error:please enter teh valid intergers ")'''

#handling zeroDivisionError when the denominator is 0
'''try:
    num1=int(input("enter the number="))
    num2=int(input("enter the number="))
    result=num1/num2
    print("result=",result)
except ZeroDivisionError:
    print("Error:division by zero is not allowed ")'''

#only try block does not exsits

#generators
#print numbers from 1 to 5
'''def count():
    for i in range(1,6):
        yield i
        #print()    
        
print(*count())'''

#write a generator to yield numbers from 1 to 10
'''def count():
    for i in range(1,11):
        yield i
print(*count())'''

def count():
    for i in range(1,6):
        yield i
for i in count():
    print(i)
    
        
def count():
    for i in range(1,6):
        yield i
print(*count())
next(i)
       
            



        
        
    
        
    


            

    
    
    
    



    


            
        
        
    

        
        


























            
























        
    



















    



















    

























        
    



















    



















    
