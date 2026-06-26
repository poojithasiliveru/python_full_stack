Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=78
type(a)
<class 'int'>
b=9.6
type(b)
<class 'float'>
c='Codegnan'
type(c)
<class 'str'>
d="Course"
type(d)
<class 'str'>
e='''Vijayawada'''
type(e)
<class 'str'>
f=7+9j
type(f)
<class 'complex'>
g=8j+4
type(g)
<class 'complex'>
h=6j
type(h)
<class 'complex'>
i=True
type(i)
<class 'bool'>
j=False
type(j)
<class 'bool'>
k="True"
type(k)
<class 'str'>
#Datatype Conversions
int(8)
8
int(7.6)
7
int("Code")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int("Code")
ValueError: invalid literal for int() with base 10: 'Code'
int(6+4j)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int(6+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
float(7)
7.0
float(9.6)
9.6
float("Python")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float("Python")
ValueError: could not convert string to float: 'Python'
float(6+9j)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    float(6+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#STRING
str(1)
'1'
str(7.5)
'7.5'
str("Viyayawada")
'Viyayawada'
>>> str(8+7j)
'(8+7j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #COMPLEX
>>> complex(1)
(1+0j)
>>> complex(4.7)
(4.7+0j)
>>> complex(8+6j)
(8+6j)
>>> complex("Data")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    complex("Data")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #BOOLEAN
>>> bool(8)
True
>>> bool(6.8)
True
>>> bool("Code")
True
>>> bool(7+7j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> bool(1)
True
>>> bool(0)
False
