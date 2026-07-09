Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dictionary{}
>>> #it should be in the key value pairs
>>> a={"name":"sri","year":2026,"month":6}
>>> print(a)
{'name': 'sri', 'year': 2026, 'month': 6}
>>> type(a)
<class 'dict'>
>>> b={"name","pooja"}
>>> type(a)
<class 'dict'>
>>> c={2027:7}
>>> type(c)
<class 'dict'>
>>> #methods in the dictionary
>>> #update-it is the add of key value pairs in the dictionary
>>> a={"year":2026,"month":"july","date":4}
>>> a.update({"time":7})
>>> a
{'year': 2026, 'month': 'july', 'date': 4, 'time': 7}
>>> a.update({"name":"pooja"},{"city":"vija"})
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.update({"name":"pooja"},{"city":"vija"})
TypeError: update expected at most 1 arguments, got 2
>>> a.update({"name":"pooja","city":"vija"})
>>> a
{'year': 2026, 'month': 'july', 'date': 4, 'time': 7, 'name': 'pooja', 'city': 'vija'}
>>> #setdefault()
>>> a.setdefault("duration",4)
4
>>> a
{'year': 2026, 'month': 'july', 'date': 4, 'time': 7, 'name': 'pooja', 'city': 'vija', 'duration': 4}
>>> a={"course":"python"}
>>> a.setdefault("duration",4)
4
>>> a
{'course': 'python', 'duration': 4}
>>> #accessing of dict
>>> a={"color":"black","food":"biryani","icecream":"nuts"}
>>> a["color"]
'black'
>>> #in the accessing only keyonly possible
>>> a["black"]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a["black"]
KeyError: 'black'
>>> #get() - we can take any one key or value
>>> a.get("food")
'biryani'
>>> a
{'color': 'black', 'food': 'biryani', 'icecream': 'nuts'}
>>> a.get("biryani")
>>> a
{'color': 'black', 'food': 'biryani', 'icecream': 'nuts'}
>>> #get means read
>>> #keys()
>>> a={"month":7,"day":"sat","time":7}
>>> a.keys()
dict_keys(['month', 'day', 'time'])
>>> #values
>>> a.values()
dict_values([7, 'sat', 7])
>>> #items()-both key and value will print
>>> a.items()
dict_items([('month', 7), ('day', 'sat'), ('time', 7)])
>>> a={"city":"vija","country":"india","state":"ap"}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> #pop()-in pop should not keep empty always should enter the key in the pop()
>>> a.pop("city")
'vija'
>>> a
{'country': 'india', 'state': 'ap'}
>>> #popitem()
>>> a.popitem()
('state', 'ap')
>>> a
{'country': 'india'}
>>> #popitem isalso remove the key value pair it will take the last key value pair
>>> #len()
>>> a={"name":"sri","mail":"sri@2006.com"}
>>> len(a)
2
>>> #copy()
>>> a.copy()
{'name': 'sri', 'mail': 'sri@2006.com'}
>>> b=a.copy()
>>> b
{'name': 'sri', 'mail': 'sri@2006.com'}
>>> #clear()
>>> a.clear()
>>> a
{}
>>> #dictionary is a mutable and does not allow duplicates
>>> a={"name":"sri","year":2026,"name":"sri"}
>>> print(a)
{'name': 'sri', 'year': 2026}
>>> b={"name":"sri","year":2026,"name":"ram"}
>>> d
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> b
{'name': 'ram', 'year': 2026}
>>> #key should be different and values same also no problem.
>>> a={"name1":"sri","year":2026,"name2":"sri"}
>>> a
{'name1': 'sri', 'year': 2026, 'name2': 'sri'}
>>> #passing multiple values in the one key.
>>> a={"idnos":[10,20,30],"name":["sri","ram","sai"],"marks":[90,80,70]}
>>> a
{'idnos': [10, 20, 30], 'name': ['sri', 'ram', 'sai'], 'marks': [90, 80, 70]}
>>> a.keys()
dict_keys(['idnos', 'name', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['sri', 'ram', 'sai'], [90, 80, 70]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('name', ['sri', 'ram', 'sai']), ('marks', [90, 80, 70])])
>>> #in dictionary count() and index() does not possible.
>>> a={"year":2026,"month":7}
>>> a.count("year")
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.count("year")
AttributeError: 'dict' object has no attribute 'count'
>>> a.index("month")
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.index("month")
AttributeError: 'dict' object has no attribute 'index'
>>> 