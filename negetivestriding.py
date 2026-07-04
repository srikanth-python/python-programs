Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #negetive striding
>>> a="python course"
>>> a[-1:-11:-3]
'eu h'
>>> a[-2:-12:-4]
'sch'
>>> a[-5:-13:-5]
'oh'
>>> a[8:4:2]
''
>>> a[4:8:2]
'o '
>>> a[-9:-3:-1]
''
>>> a[-3:-9:-1]
'ruoc n'
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
>>> a[:-1]
'python cours'
>>> a[-1:]
'e'
>>> a[0:]
'python course'
>>> a[-1:]
'e'
>>> a[-1:-14]
''
>>> a[-14:-1]
'python cours'
>>> a[::-1]
'esruoc nohtyp'
>>> a[-3:-9]
''
>>> a[::-1]
'esruoc nohtyp'
>>> #in slicing reverse is not possible
>>> a[-3:-9]
''
>>> 