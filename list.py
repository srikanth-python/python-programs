Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list[]
>>> #it is mutable data type means we can changes
>>> a=[3,4.5,"python",9+7j,True,False]
>>> print(a)
[3, 4.5, 'python', (9+7j), True, False]
>>> type(a)
<class 'list'>
>>> b=9
>>> type(b)
<class 'int'>
>>> c=[9]
>>> type(c)
<class 'list'>
>>> #list methods
>>> a=["pythpon","java","c"]
>>> a.append("c++")
>>> a
['pythpon', 'java', 'c', 'c++']
>>> a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("ml","ai")
TypeError: append() takes exactly one argument (2 given)
>>> a.append(["ml","aI"])
>>> a
['pythpon', 'java', 'c', 'c++', ['ml', 'aI']]
>>> #extend()
>>> a=["java","html","css"]
>>> a.extend(["js","bs"])
>>> a
['java', 'html', 'css', 'js', 'bs']
>>> a.extend("js","bs")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.extend("js","bs")
TypeError: extend() takes exactly one argument (2 given)
>>> #insert()
>>> a=["banana","mango","grapes"]
>>> a.insert(1,"orange")
>>> a
['banana', 'orange', 'mango', 'grapes']
>>> #sort()
>>> a=["kiwi","mango","apple","dragon","berry"]
>>> a.sort()
>>> a
['apple', 'berry', 'dragon', 'kiwi', 'mango']
>>> a=[1,4,3,5,6,2,3]
>>> a.sort()
>>> a
[1, 2, 3, 3, 4, 5, 6]
>>> #reverse()
>>> a=["java","c","c++","css"]
>>> a.reverse()
>>> a
['css', 'c++', 'c', 'java']
>>> a=[1,2,3,4,5,6]
>>> a.reverse()
>>> a
[6, 5, 4, 3, 2, 1]
>>> #pop()- remove the last when itis empty
>>> a=["black","red","green","yellow"]
>>> a.pop()
'yellow'
>>> a
['black', 'red', 'green']
>>> a.pop(1)
'red'
>>> a
['black', 'green']
>>> a.pop("green")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.pop("green")
TypeError: 'str' object cannot be interpreted as an integer
>>> #remove()
>>> a=["css","html","js"]
>>> a.remove("html")
>>> a
['css', 'js']
>>> a.remove(1)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
>>> a.remove("1")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.remove("1")
ValueError: list.remove(x): x not in list
>>> #copy()
>>> a=["pooja","priya","sweety","cuty"]
>>> a.copy()
['pooja', 'priya', 'sweety', 'cuty']
>>> b=a.copy()
>>> b
['pooja', 'priya', 'sweety', 'cuty']
>>> #clear()
>>> a.clea()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.clea()
AttributeError: 'list' object has no attribute 'clea'
>>> a.clear()
>>> a
[]
>>> a=[]
>>> a.append("html")
>>> a
['html']
>>> #len()
>>> a=["hi","hello","how"]
>>> len(a)
3
>>> b="hello"
>>> len(b)
5
>>> c=["hello"]
>>> len(c)
1
>>> a.count("hello")
1
>>> #index()
>>> a.index("hello")
1
>>> 