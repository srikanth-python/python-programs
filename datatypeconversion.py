Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #datatype conversions
>>> #init()
>>> int(9)
9
>>> int(9.0)
9
>>> int('code')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int('code')
ValueError: invalid literal for int() with base 10: 'code'
>>> int(3+5j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+5j)
TypeError: can't convert complex to int
>>> int(True)
1
>>> #float()
>>> float(3)
3.0
>>> float(5.0)
5.0
>>> float('sri')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float('sri')
ValueError: could not convert string to float: 'sri'
>>> float(4+6j)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(4+6j)
TypeError: can't convert complex to float
>>> float(True)
1.0
>>> int(False)
0
>>> float(False)
0.0
>>> #str()
>>> str(3)
'3'
>>> str(9.0)
'9.0'
>>> str("hello")
'hello'
>>> str(3+9j)
'(3+9j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex()
>>> complex(9)
(9+0j)
>>> complex(4.9)
(4.9+0j)
>>> complex('hi')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex('hi')
ValueError: complex() arg is a malformed string
>>> complex(3+9j)
(3+9j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(8)
True
>>> bool(9.0)
True
>>> bool('code')
True
>>> bool(5+7j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> bool()
False
>>> 