Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #string indexing
>>> #positive indexing starts from 0
>>> a="srikanth"
>>> a[1]
'r'
>>> a[0]
's'
>>> a[3]
'k'
>>> a[0]+a[1]+a[2]
'sri'
>>> a="i am in class"
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'class'
>>> a[2]+a[3]
'am'
>>> a[5]+a[6]
'in'
>>> a="simple is better than complex"
>>> a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
>>> a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'
>>> a[0]+a[1]a[2]+a[3]+a[4]+a[5]
SyntaxError: invalid syntax
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'
>>> b="codegnan it solutions"
>>> a[12]+a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'tter than'
>>> b[12]+b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'solutions'
>>> b[9]+b[10]
'it'
>>> b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]
'codegnan'
>>> #negetive indexing starts from -1
>>> a="i am leaning python"
>>> a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
>>> a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]
'nohtyp'
>>> a[-18]+a[-19]
' i'
>>> a[-18]+a[-17]
' a'
>>> a[-17]+a[-16]
'am'
>>> a="python fullstack"
>>> a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'stack'
>>> a[-9]+a[-8]+a[-7]+a[-6]
'full'
>>> a[-16]+a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'python'
>>> #slicing
>>> a="codegnan"
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[ :4]
'code'
>>> a[4:]
'gnan'
>>> a="Time is very precious"
>>> a[8:12]
'very'
>>> a[:4]
'Time'
>>> a[13:]
'precious'
>>> a="work until you succeed"
>>> a[15:]
'succeed'
>>> a[5:10]
'until'
>>> a[:4]
'work'
>>> a[11:14]
'you'
>>> #negetive slicing
>>> a="vizag is city destiny"
>>> a[-12:-8]
'city'
>>> a[-7:]
'destiny'
>>> a[-21:-16]
'vizag'
>>> b="hi hello how are you'
SyntaxError: EOL while scanning string literal
>>> b="hi hello how are you"
>>> b[-16:-12]
'ello'
>>> b[-17:-12]
'hello'
>>> b[-11:-8]
'how'
>>> b[-7:-4]
'are'
>>> b[-3:]
'you'
>>> b[-3:0]
''
>>> #striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
>>> a="machine learning"
>>> a[::5]
'mnag'
>>> a[::7]
'm n'
>>> a[::2]
'mcielann'
>>> a[3:11]
'hine lea'
>>> a[:8]
'machine '
>>> a[9:]
'earning'
>>> a[::10]
'ma'
>>> a[::4]
'miln'
>>> a="cloud computing"
>>> a[1:9:2]
'lu o'
>>> a[2:13:3]
'o mt'
>>> a[6:14:4]
'cu'
>>> a[5:12:2]
' opt'
>>> a[3:9:5]
'um'
>>> 