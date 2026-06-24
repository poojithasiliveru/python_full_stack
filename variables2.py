Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=4;b=9
print(a+b)
13
a,b=2,3
print(a+b)
5
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
a=b=c=10
print(a,b,c)
10 10 10
a,b,c=2,3,4
print(a,b,c)
2 3 4
a,b,c=1,2,3,4,5,6,7,8
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a,b,c=1,2,3,4,5,6,7,8
ValueError: too many values to unpack (expected 3, got 8)
#UNPACK
a,b,c=
SyntaxError: invalid syntax
a,b,c=(3,4,5)
>>> print(a,b,c)
3 4 5
>>> #do not uses spaces
>>> first name="Poojitha"
SyntaxError: invalid syntax
>>> first_name="Poojitha"
>>> print(first_name)
Poojitha
>>> firstname="Poojitha"
>>> print(firstname)
Poojitha
>>> #STRING CONCATINATION
>>> fname="Poojitha"
>>> lname="Siliveru"
>>> print(fname+lname)
PoojithaSiliveru
>>> print(fname+" "+lname)
Poojitha Siliveru
>>> print(fname,lname)
Poojitha Siliveru
>>> #CASE SENSITIVE
>>> name="Poojitha"
>>> print(name)
Poojitha
>>> Name="Poojitha"
>>> print(Name)
Poojitha
>>> NAME="Poojitha"
>>> print(NAME)
Poojitha
>>> #DELETE THE VARIABLE
>>> a=89
>>> print(a)
89
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
