Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #BITWISE
>>> a=4
>>> b=8
>>> a&b
0
>>> bin(4)
'0b100'
>>> bin(8)
'0b1000'
>>> a=5
>>> b=7
>>> a&b
5
>>> bin(5)
'0b101'
>>> bin(7)
'0b111'
>>> c=9
>>> d=7
>>> c&d
1
>>> bin(9)
'0b1001'
>>> bin(7)
'0b111'
>>> #OR
>>> a=3
>>> b=6
>>> a|b
7
>>> c=4
>>> d=8
>>> c|d
12
>>> a=7
>>> b=9
>>> a|b
15
#NEGOCIATION
#formula -(a+1)
a=5
~a
-6
a=9
~a
-10
b=-9
~b
8
c=-12
~c
11
#XOR
a=3
b=5
a^b
6
a=7
b=9
a^b
14
c=8
d=7
c^d
15
#LEFT SHIFT
a=3
a<<2
12
b=4
b<<3
32
a<<3
24
b<<2
16
#RIGHT SHIFT
a=6
a>>3
0
b=14
b>>2
3
bin(14)
'0b1110'
