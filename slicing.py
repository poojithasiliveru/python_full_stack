Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #SLICING
>>> a="Codegnan"
>>> a[0:4]
'Code'
>>> a[4:8]
'gnan'
>>> a[:4]
'Code'
>>> a[4:]
'gnan'
>>> a[0:8]
'Codegnan'
>>> b="Work until you succeed"
>>> b[5:10]
'until'
>>> b[11:15]
'you '
>>> b[11:14]
'you'
>>> b[0:4]
'Work'
>>> b[15:22]
'succeed'
>>> c="Codegnan IT Solutions"
>>> c[10:12]
'T '
>>> c[9:11]
'IT'
>>> c[12:21]
'Solutions'
>>> c[0-8]
'o'
>>> c[0:8]
'Codegnan'
>>> c[12;20]
SyntaxError: invalid syntax
>>> c[12:20]
'Solution'
>>> #NEGATIVE SLICING
a="vijayawada"
a[-1:-5]
''
a[-1:-3]
''
a[-11:-1]
'vijayawad'
a[-12:-1]
'vijayawad'
b="Vijayawada is a royal city"
b[-10:-5]
'royal'
b[-26:-16]
'Vijayawada'
b[-4:-1]
'cit'
b[-4:]
'city'
c="Vizag is city of destiny"
c[-15:-11]
'city'
c[-24:-19]
'Vizag'
c[-7:]
'destiny'
c[11:-15]
''
c[-11:-15]
''
c[0:-8]
'Vizag is city of'
