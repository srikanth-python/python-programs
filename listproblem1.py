Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=["codegnan","python","course"]
>>> #["CODEGNAN","PYTHON","COURSE"]
>>> b=str(a)
>>> b
"['codegnan', 'python', 'course']"
>>> b.upper()
"['CODEGNAN', 'PYTHON', 'COURSE']"
>>> #another method
>>> b=[]
>>> a[0]
'codegnan'
>>> a[0].upper()
'CODEGNAN'
>>> b.append(a[0].upper())
>>> b
['CODEGNAN']
>>> b.append(a[1].upper())
>>> b
['CODEGNAN', 'PYTHON']
>>> b.append(a[2].upper())
>>> b
['CODEGNAN', 'PYTHON', 'COURSE']
>>> 