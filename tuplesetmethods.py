Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuple()
>>> #it is immutable datatype means we cannot change
>>> #it is denoted by ()
>>> a=(4,6.5,"sri",5+8j,True,False)
>>> print(a)
(4, 6.5, 'sri', (5+8j), True, False)
>>> type(a)
<class 'tuple'>
>>> len(a)
6
>>> #there are two methods in the tuple there are 1.index  2.count
>>> a.index(8+9j)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.index(8+9j)
ValueError: tuple.index(x): x not in tuple
>>> a.index(5+8j)
3
>>> a.count(True)
1
>>> a.count("sri")
1
>>> #set{}
>>> #it is mutable datatype means we can changea
>>>  #it is unorder collection of data and it does not allow dublecates
>>> a={3,4.6,"python",4+7j,True,False}
>>> print(a)
{False, True, 3, 4.6, 'python', (4+7j)}
>>> type(a)
<class 'set'>
>>> b={6,7,8,9,20,5}
>>> print(b)
{5, 6, 7, 8, 9, 20}
>>> b={5,6,7,8,9,5,6,20,10}
>>> print(b)
{5, 6, 7, 8, 9, 10, 20}
>>> #methods of set
>>> a={2,3,4,5,6,7,8,9}
>>> b={6,7,8,9}
>>> b.subset(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b.subset(a)
AttributeError: 'set' object has no attribute 'subset'
>>> b.issubset(a)
True
>>> a.issubset(b)
False
>>> #superset-->if every element of setB is present in setA then A is a superset of B
>>> a={2,3,4,5,6,7,8}
>>> b={6,7,8}
>>> a.issuperset(b)
True
>>> b.issuperset(a)
False
>>> #union() means marging of two sets and remove dublicates
>>> a={1,2,3,4,5,6,7}
>>> b={6,7,8,9,10,20}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20}
>>> #intersections()-->print the common values
>>> a={3,4,5,6,7,8,9}
>>> b={7,8,9,10,20,40}
>>> a.intersection(b)
{8, 9, 7}
>>> #difference()
>>> a={10,11,12,13,14,15,16}
>>> b={6,7,8,12,13,14,15,16,17}
>>> a.difference(b)
{10, 11}
>>> b.difference(a)
{8, 17, 6, 7}
>>> #symmentric_difference()-->it removes the same values
>>> a={2,3,4,5,6,7,8,9}
>>> b={5,6,8,9,10,11,7}
>>> a.symmenteric_difference(b)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.symmenteric_difference(b)
AttributeError: 'set' object has no attribute 'symmenteric_difference'
>>> a.symmetric_difference(b)
{2, 3, 4, 10, 11}
>>> b.symmetric_difference(a)
{2, 3, 4, 10, 11}
>>> #update()
>>> a={1,2,3,4,5}
>>> b={4,5,6,7,8}
>>> a.update(b)
>>> a
{1, 2, 3, 4, 5, 6, 7, 8}
>>> b.update(a)
>>> b
{1, 2, 3, 4, 5, 6, 7, 8}
>>> #intersection_update()
>>> a={1,2,3,4,5,6,7,8}
>>> b={2,4,6,7,10,11,12}
>>> a
{1, 2, 3, 4, 5, 6, 7, 8}
>>> a.intersection_update(b)
>>> a
{2, 4, 6, 7}
>>> b.intersection_update(a)
>>> b
{2, 4, 6, 7}
>>> #difference_update()
>>> a={2,3,4,5,6,7,8}
>>> b={1,5,6,7,8,9,10}
>>> a.difference_update(b)
>>> a
{2, 3, 4}
>>> b.difference_update(a)
>>> b
{1, 5, 6, 7, 8, 9, 10}
>>> a
{2, 3, 4}
>>> b
{1, 5, 6, 7, 8, 9, 10}
>>> #campare the atlast update value first given value is deleted after update
>>> a={2,3,4,5,6,7,8,9}
>>> b={5,6,7,8,9,10,11}
>>> a.symmentric_difference_update(b)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.symmentric_difference_update(b)
AttributeError: 'set' object has no attribute 'symmentric_difference_update'
>>> a.symmetric_difference_update(b)
>>> a
{2, 3, 4, 10, 11}
>>> b.symmetric_difference_update(a)
>>> b
{2, 3, 4, 5, 6, 7, 8, 9}
>>> #add()
>>> a={2,3,4,5,6,7}
>>> a.add(10)
>>> a
{2, 3, 4, 5, 6, 7, 10}
>>> #copy
>>> a.copy()
{2, 3, 4, 5, 6, 7, 10}
>>> b=a.copy()
>>> b
{2, 3, 4, 5, 6, 7, 10}
>>> #clear()
>>> a.clear()
>>> a
set()
>>> a=set()
>>> a.add(30)
>>> a
{30}
>>> #add only one number not multiple numbers in the set atatime
>>> a=set{}
SyntaxError: invalid syntax
>>> #pop()-->removes the first element
>>> a={2,3,4,5,6,7}
>>> a.pop()
2
>>> a
{3, 4, 5, 6, 7}
>>> #remove()
>>> a.remove(7)
>>> a
{3, 4, 5, 6}
>>> #discard()-->remove element is same to the remove
>>> a.discard(4)
>>> a
{3, 5, 6}
>>> #isdisjoint()-->should have a two different set
>>> a={1,2,3,4,5,6}
>>> b={7,8,9,10,11,12}
>>> a.isdisjoint(b)
True
>>> b.isdisjoint(a)
True
>>> #len()
>>> a={2,3,4,5,6,7}
>>> len(a)
6
>>> a.count(7)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a.count(7)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    a.index(2)
AttributeError: 'set' object has no attribute 'index'
>>> #index and count is not possible in the set