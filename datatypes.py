Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #datatypes
>>> a=20
>>> type(a)
<class 'int'>
>>> print(type(a))
<class 'int'>
>>> b=2.9
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="python"
>>> type(d)
<class 'str'>
>>> e='''codegnan'''
>>> type(e)
<class 'str'>
>>> f=5+9j
>>> type(f)
<class 'complex'>
>>> g=4j+5
>>> type(g)
<class 'complex'>
>>> h=7j
>>> type(h)
<class 'complex'>
>>> a=3+5i
SyntaxError: invalid syntax
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
>>> c=true
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    c=true
NameError: name 'true' is not defined
>>> d="true"
>>> type(d)
<class 'str'>
>>> 