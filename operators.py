Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#OPERATORS
#Arthematic operators
a=8
b=4
print(a+b)
12
print(a-b)
4
print(a*b)
32
print(a//b)
2
print(a/b)
2.0
print(a%b)
0
#Assignment Operators
a=5
b=10
a+=b
a
15
a-=b
a
5
a*=b
a
50
a=//b
SyntaxError: invalid syntax
a//=b
a
5
a/=b
a
0.5
a%=b
a
0.5
b+=a
b
10.5
b-=a
b
10.0
b*=a
b
5.0
b//=a
b
10.0
b/=a
b
20.0
b%=a
b
0.0
#COMPARISION OPERATOR
a=9
b=6
a>b
True
a<b
False
b>a
False
b<a
True
a<=b
False
a>=b
True
b<=a
True
b>=a
False
a!=b
True
b!=a
True
a==b
False
#LOGICAL OPERATORS
a=4
b=8
a<b and a>b
False
a<b and b>a
True
a<=b and a>=b
False
a>=b and a<=b
False
a!=b or a==b
True
a<b or b<a
True
a<b or b>a
True
not True
False
nit False
SyntaxError: invalid syntax
not False
True
#IDENTITY OPERATORS
a-8
-4
a=8
type(a) is int
True
type(a) is float
False
type(a) is str
False
type(a) is complex
False
type(a) is bool
False
>>> type(a) is not int
False
>>> type(a) is not float
True
>>> type(a) is not str
True
>>> type(a) is not complex
True
>>> type(a) is not bool
True
>>> b=8.7
>>> type(b) is int
False
>>> type(a) is float
False
>>> type(b) is float
True
>>> type(b) is str
False
>>> type(b) is complex
False
>>> type(b) is bool
False
>>> #MEMBERSHIP OPERATTOR
>>> a=7,6,0,5,34,67,3
>>> 5 in a
True
>>> 67 in a
True
>>> 100 in a
False
>>> 5 not int a
SyntaxError: invalid syntax
>>> 5 not in a
False
>>> 7 not in a
False
>>> 0 in a
True
