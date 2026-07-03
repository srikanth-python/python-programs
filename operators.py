Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #0perators
>>> #Arthematic operators
>>> a=3
>>> b=2
>>> print(a+b)
5
>>> print(a-b)
1
>>> print(a*b)
6
>>> print(a/b)
1.5
>>> print(a//b)
1
>>> print(a%b)
1
>>> print(a**b)
9
>>> #assignment operators
>>> a=4
>>> b=6
>>> print(a+=b)
SyntaxError: invalid syntax
>>> a+b
10
>>> #it uses the latest updated value and it is used in the loops
>>> a+=b
>>> a
10
>>> a-=b
>>> a
4
>>> a*=b
>>> a
24
>>> a/=b
>>> a
4.0
>>> a**=b
>>> a
4096.0
>>> a//=b
>>> a
682.0
>>> a%=b
>>> a
4.0
>>> a*=2
>>> a
8.0
>>> #comparsion operators
>>> a=4
>>> b=6
>>> a<b
True
>>> b>a
True
>>> b<a
False
>>> a!=b
True
>>> a==b
False
>>> a>=b
False
>>> b>=a
True
>>> a=8
>>> b=8
>>> a==b
True
>>> #Logical operators
>>> a=5
>>> b=7
>>> a>b and b<a
False
>>> a<b and b>a
True
>>> a<=b and b>=a
True
>>> a!=b and a==b
False
>>> a>b or b<a
False
>>> a<b and b<a
False
>>> a<b and b>a
True
>>> a<b or b<a
True
>>> a!=b or a==b
True
>>> not True
False
>>> not False
True
>>> #identify operators
>>> a=4
>>> type(a) is int
True
>>> type(a) is not int
False
>>> a=6.7
>>> type(a) is float
True
>>> type(a) is not float
False
>>> a='sri'
>>> type(a) is str
True
>>> type(a) is not str
False
>>> a=3+4j
>>> type(a) is complex
True
>>> type(a) is not complex
False
>>> a=True
>>> type(a) is bool
True
>>> #membership operators
>>> #it is used to check weather the value is there or not
>>> a=1,2,3,4,5,6,7,8,9
>>> 8 in a
True
>>> 10 not in a
True
>>> 20 in a
False
>>> #Bitwise operators
>>> a=2
>>> b=6
>>> a&b
2
>>> a=5
>>> b=7
>>> a&b
5
>>> #it is binary format
>>> bin(2)
'0b10'
>>> bin(6)
'0b110'
>>> #1,1-->1
>>> #0,0-->0
>>> #0,1-->0
>>> a=3
>>> b=5
>>> a|b
7
>>> #or
>>> #1,1-->1
>>> #0,1-->1
>>> #0,0-->0
>>> a=6
>>> b=7
>>> a|b
7
>>> bin(6)
'0b110'
>>> bin(7)
'0b111'
>>> #not formula=-(a+1)
>>> a=2
>>> ~a
-3
>>> a=9
>>> ~a
-10
>>> a=-10
>>> ~a
9
>>> a=-8
>>> a
-8
>>> ~a
7
>>> b=-15
>>> ~b
14
>>> #xor
>>> #1,1-->0
>>> #0,0-->0
>>> #0,1-->1
>>> a=6
>>> b=7
>>> a^b
1
>>> a=2
>>> b=4
>>> a^b
6
>>> a=5
>>> b=7
>>> a^b
2
>>> a=3
>>> a<<2
12
>>> bin(3)
'0b11'
>>> a=5
>>> a<<3
40
>>> #left shift means add zeros to the right side
>>> #001100=12
>>> #right shift means add zeros to the left side
>>> a=4
>>> a>>2
1
>>> bin(4)
'0b100'
>>> #in right shift there will be eliminates the right side zeros
>>> #00001=1
>>> a=9
>>> a>>3
1
>>> #eliminates 0 and 1s in right side
>>> bin(9)
'0b1001'
>>> #001001=000001=1