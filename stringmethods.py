Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #string methods
>>> #len()-->it is used to find the number of characters
>>> a="python"
>>> len(a)
6
>>> b="python course"
>>> len(b)
13
>>> c=" "
>>> len(c)
1
>>> d=""
>>> len(d)
0
>>> #count()-->it is used to count number of characters or words in a given string
>>> a="twinkle twinkle little star"
>>> count("twinkle")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count("twinkle")
NameError: name 'count' is not defined
>>> a.count("twinkle")
2
>>> a.count("k")
2
>>> a.count("t")
5
>>> a.count(" ")
3
>>> b="twinkletwinkle"
>>> b.count("twinkle")
2
>>> b.count("twinkletwinkle")
1
>>> c="twinkle.twinkle"
>>> c.count("twinkle")
2
>>> c.count("twinkle.twinkle")
1
>>> #find a string
>>> #find()-->it is used to find index of a character
>>> a="python"
>>> a[2]
't'
>>> a.find("t")
2
>>> a.find("n")
5
>>> b="hello"
>>> b.find("l")
2
>>> b[2:4]
'll'
>>> b.find("ll")
2
>>> #repeated finding index is not possible
>>> a.find("m")
-1
>>> #escape sequences
>>> #\n-->new line
>>> #\t-->tab space(1tab space=4 to 8 between)
>>> a="name\nmobileno\tmailid\ncollege\tbranch"
>>> print(a)
name
mobileno	mailid
college	branch
>>> a="name:srikanth\nmobileno:9949894096\tmailid:sir2006@gmail.com\ncollege:jbiet\tbranch:aiml"
>>> print(a)
name:srikanth
mobileno:9949894096	mailid:sir2006@gmail.com
college:jbiet	branch:aiml
>>> #replace()-->it is used to replace words
>>> a="wait until you succeed"
>>> a.replace("wait","work")
'work until you succeed'
>>> b="i love python"
>>> b="i love java java"
>>> b.replace("python")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    b.replace("python")
TypeError: replace() takes at least 2 arguments (1 given)
>>> b.replace("java","python")
'i love python python'
>>> #upper()
>>> a="hello"
>>> a.upper()
'HELLO'
>>> b="HI"
>>> b.lower()
'hi'
>>> c="python"
>>> c.upper("p")
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    c.upper("p")
TypeError: upper() takes no arguments (1 given)
>>> c[0].upper()
'P'
>>> c.capitalize()
'Python'
>>> d="python course"
>>> d.title()
'Python Course'
>>> d.capitalize()
'Python course'
>>> e="i will work hard"
>>> e.capitalize()
'I will work hard'
>>> e.title()
'I Will Work Hard'
>>> #conditions
>>> a="python"
>>> a.isupper()
False
>>> a.islower()
True
>>> a.isalpha()
True
>>> b="python course"
>>> b.isalpha()
False
>>> b="pythoncourse"
>>> b.isalpha()
True
>>> d=1234
>>> d.isdigit()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
>>> d="12345"
>>> d.isdigit()
True
>>> f="srikanth"
>>> f.isalnum()
True
>>> g="srikanth123"
>>> g.isalnum()
True
>>> f="srikanth@123"
>>> f.isalnum()
False
>>> x="sri_123"
>>> x.isalnum()
False
>>> a="java"
>>> a.startswith("j")
True
>>> a.endswith("a")
True
>>> #strip()-->it removes the space
>>> #lstrip(),rstrip()
>>> a="   srikanth    "
>>> a.strip()
'srikanth'
>>> a.lstrip()
'srikanth    '
>>> a.rstrip()
'   srikanth'
>>> #split()
>>> a="python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
>>> b="i am in class room"
>>> b.split()
['i', 'am', 'in', 'class', 'room']
>>> #join()
>>> b="vja","hyd","vzg"
>>> "".join(b)
'vjahydvzg'
>>> " ".join(b)
'vja hyd vzg'
>>> "k".join(b)
'vjakhydkvzg'
>>> #endig string we cannot join
>>> a="python"
>>> "k".join(a)
'pkyktkhkokn'
>>> join(b)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    join(b)
NameError: name 'join' is not defined
>>> 