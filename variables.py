Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #variables
>>> print(2+3)
5
>>> a=10
>>> print(a)
10
>>> b=20
>>> print(b)
20
>>> x=20
>>> print(X)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined
>>> print(x)
20
>>> z=40
>>> print(z)
40
>>> 3=40
SyntaxError: can't assign to literal
>>> a3=90
>>> print(a3)
90
>>> 5a=40
SyntaxError: invalid syntax
>>> b123456=300
>>> print(b123456)
300
>>> @=60
SyntaxError: invalid syntax
>>> print(@)
SyntaxError: invalid syntax
>>> _=50
>>> print(_)
50
>>>  =90
 
SyntaxError: unexpected indent
>>> _=90
>>> print(_)
90
>>> if=45
SyntaxError: invalid syntax
>>> a=4,b=5
SyntaxError: can't assign to literal
>>> a=4;b=5
>>> print(a+b)
9
>>> a,b=3,4
>>> print(a,b)
3 4
>>> a=2,3,4
>>> print(a)
(2, 3, 4)
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a=b=c=10
>>> print(a,b,c)
10 10 10
>>> a,b,c=(2,3,4)
>>> print(a,b,c)
2 3 4
>>> a,b,c=2,3,4,5,67
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a,b,c=2,3,4,5,67
ValueError: too many values to unpack (expected 3)
>>> first name="srikanth"
SyntaxError: invalid syntax
>>> first_name="sri"
>>> print(first_name)
sri
>>> firstname="sri"
>>> print(firstname)
sri
>>> fname="srikanth"
>>> lname="k"
>>> print(fname+" "+lname)
srikanth k
>>> print(fname+lname)
srikanthk
>>> print(fname,lname)
srikanth k
>>> a=5
>>> print(a)
5
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> name="sri"
>>> print(name)
sri
>>> NAME="sri"
>>> print(NAME)
sri
>>> 