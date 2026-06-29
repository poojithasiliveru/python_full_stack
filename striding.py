Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #STRADING
>>> #SYNTAX - [a:b:c]
>>> a="Data Science"
>>> a[::]
'Data Science'
>>> a[::1]
'Data Science'
>>> a[::2]
'Dt cec'
>>> a[::3]
'Dacn'
>>> a[::4]
'D e'
>>> a[::5]
'DSc'
>>> a[::6]
'Dc'
>>> b="Cloud Computing"
>>> b[::5]
'C u'
>>> b[::4]
'Cdmi'
>>> b[::8]
'Cm'
>>> b[2:]
'oud Computing'
>>> b[3:11]
'ud Compu'
>>> b[:9]
'Cloud Com'
>>> b[::2]
'CodCmuig'
>>> b[::6]
'CCi'
>>> c="Machine Learning"
>>> a[1:9]
'ata Scie'
>>> a[1:9:2]
'aaSi'
a[3:14:2]
'aSine'
c[1:9:2]
'ahn '
c[3:14:2]
'hn eri'
c[5:14:2]
'n eri'
c[5:15:4]
'nei'
[2:12:3]
SyntaxError: invalid syntax
c[5:15:4]
'nei'
c[2:12:3]
'cnLr'
c[0:`0:1]
SyntaxError: invalid syntax
c[0:10:1]
'Machine Le'
c[::3]
'Mheeng'
#NEGATIVE STRIDING
a="Python Course"
a[-1:-10:-2]
'ero o'
a[-3:-13:-4]
'r t'
a[-5:-11:-3]
'on'
a[-1:-5]
''
a[-1:]
'e'
a[-5:-1]
'ours'
a[-7:-4:-2]
''
a[-5:-1:-2]
''
#LOWEST TO HIGHTEST NOT POSSIBLE
a[-8:-4:-2]
''
#IN POSITIVE STRIDING HIGHEST TO LOWEST NOT POSSIBLE
a[8:5:1]
''
a[10:4:5]
''
