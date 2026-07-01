Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #TUPLE
>>> #tuple-->OLLECTION OF DATA--->IMMUTABLE
>>> a=(4,6.5,"code",4+7j,True,False)
>>> type(a)
<class 'tuple'>
>>> print(a)
(4, 6.5, 'code', (4+7j), True, False)
>>> a.count(4+7j)
1
>>> a.count("code")
1
>>> count(6.5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    count(6.5)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.index(True)
4
>>> a.index(6.5)
1
>>> a.index("code")
2
