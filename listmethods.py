Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list[]
>>> #it is mutable datatype and used to store a collection of items and it allows duplicates
>>> a=[1,2,3,4,5,6]
>>> a
[1, 2, 3, 4, 5, 6]
>>> a=list((1,2,3,4,5))
>>> a
[1, 2, 3, 4, 5]
>>> #creating a list
>>> a=list((1,2,3,4))
>>> a
[1, 2, 3, 4]
>>> #it is ordered collections of data
>>> a=[10,20,30]
>>> print(a[1])
20
>>> a[0}=50
SyntaxError: invalid syntax
>>> a[0]=50
>>> a
[50, 20, 30]
>>> #mutable
>>> a=[10,20,30]
>>> a[0]=50
>>> a
[50, 20, 30]
>>> a=[10,2.9."sri",4+7j,True,False]
SyntaxError: invalid syntax
>>> a=[10,2.9,"sri",4+7j,True,False]
>>> a
[10, 2.9, 'sri', (4+7j), True, False]
>>> #indexing-->positive and negetive indexing
>>> a=[10,20,30,40,50]
>>> print(a[1])
20
>>> print(a[3])
40
>>> #slicing syntax:list[start:end:step]
>>> a=[1,2,3,4,5,6]
>>> print(a[1:4])
[2, 3, 4]
>>> print(a[:5])
[1, 2, 3, 4, 5]
>>> #adding of elements
>>> #append()
>>> a=[1,2,3]
>>> a.append(5)
>>> a
[1, 2, 3, 5]
>>> #insert()
>>> a.insert(1,100)
>>> a
[1, 100, 2, 3, 5]
>>> a.insert(5,200)
>>> a
[1, 100, 2, 3, 5, 200]
>>> #extend()-->add multiple elements
>>> a=[1,2,3,4]
>>> a.extend([8,9])
>>> a
[1, 2, 3, 4, 8, 9]
>>> #removing elements
>>> a=[2,3,4,5,6,7,8]
>>> #remove()
>>> a.remove(8)
>>> a
[2, 3, 4, 5, 6, 7]
>>> #pop()
>>> #removes by indexing
>>> a.pop(4)
6
>>> a
[2, 3, 4, 5, 7]
>>> #clear()
>>> a.clear()
>>> a
[]
>>> a=[]
>>> a.extend([2,3,4,5])
>>> a
[2, 3, 4, 5]
>>> #list operations
>>> #concentenation
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> print(a+b)
[1, 2, 3, 4, 5, 6]
>>> #repetitions
>>> print(a*2)
[1, 2, 3, 1, 2, 3]
>>> #membership
>>> print(2 in a)
True
>>> print(3 not in a)
False
>>> #list functions
>>> a=[1,2,3,4,5,6,7]
>>> len(a)
7
>>> max(a)
7
>>> min(a)
1
>>> sum(a)
28
>>> a=[3,2,1,5]
>>> sorted(a)
[1, 2, 3, 5]
>>> b=a.copy(a)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    b=a.copy(a)
TypeError: copy() takes no arguments (1 given)
>>> b=a.copy()
>>> b
[3, 2, 1, 5]
>>> #copy()
>>> #reverse()
>>> a=[1,2,3,4,5]
>>> a.reverse()
>>> a
[5, 4, 3, 2, 1]
>>> 