Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#INDEXING -- ACCESSING AN ELEMENT
#POSITIVE INDEXING
a="vijayawada"
a[0]
'v'
a[7]
'a'
a[6]+a[5]
'wa'
a[2]+a[4]+a[6]+a[8]
'jywd'
b="i im in class"
b[0]
'i'
>>> b[8]+b[9]+b[10]+b[11]+b[12]
'class'
>>> b[5]+a[6]
'iw'
>>> b[5]+b[6]
'in'
>>> b[1]+b[5]+[7]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b[1]+b[5]+[7]
TypeError: can only concatenate str (not "list") to str
>>> b[1]+b[5]+b[7]
' i '
>>> c="I am learing Python course"
>>> c[13]+c[14]+c[15]+[16]+c[17]+c[18]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c[13]+c[14]+c[15]+[16]+c[17]+c[18]
TypeError: can only concatenate str (not "list") to str
>>> c[13]+c[14]+c[15]+c[16]+c[17]+c[18]
'Python'
>>> c[6]+c[7]+c[8]+c[9]+c[10]
'earin'
>>> c[5]+c[6]+c[7]+c[8]+c[9]
'leari'
>>> c="I am learning Python course"
>>> c[5]+c[6]+c[7]+c[8]+c[9]
'learn'
>>> c[13]+c[14]+c[15]+c[16]+c[17]+c[18]
' Pytho'
>>> c[13]+c[14]+c[15]+c[16]+c[17]+c[18]+c[9]
' Python'
>>> c[14]+c[15]+c[16]+c[17]+c[18]
'Pytho'
>>> c[14]+c[15]+c[16]+c[17]+c[18]+c[19]
'Python'
>>> c[5]+c[6]+c[7]+c[8]+c[9]
'learn'
>>> c[21]+c[22]+c[23]+c[24]+c[25]+c[26]
'course'

a="Time is very precious"
a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'precious'
a[8]+a[9]+a[10]+a[11]
'very'
a[0]+a[1]+a[2]+a[3]
'Time'
#NEGATIVE INDEXING
a="Simple"
a[-1]
'e'
a[-5]
'i'
a[-3]
'p'
b="Simple is better than complex"
b[-29]
'S'
b[-29]+b[-28]+b[-27]+b[-26]+b[-25]+b[-24]
'Simple'
b[-12]+b[-11]+b[-10]+b[-9]
'than'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'complex'
b[-19]+b[-18]+b[-17]+b[-16]+b[-15]
'bette'
[-19]+b[-18]+b[-17]+b[-16]+b[-15]+b[-14]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    [-19]+b[-18]+b[-17]+b[-16]+b[-15]+b[-14]
TypeError: can only concatenate list (not "str") to list
b[-19]+b[-18]+b[-17]+b[-16]+b[-15]+b[-14]
'better'
c="i love python"
c[-6]+c[-5]+c[-4]+c[-3]+c[-2]+c[-1]
'python'
c[-11]+c[-10]+c[-9]+c[-8]+c[-7]
'love '
[-11]+c[-10]+c[-9]+c[-8]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    [-11]+c[-10]+c[-9]+c[-8]
TypeError: can only concatenate list (not "str") to list
c[-11]+c[-10]+c[-9]+c[-8]+c[-7]
'love '
c[-13]
'i'
[-11]+c[-10]+c[-9]+c[-8]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    [-11]+c[-10]+c[-9]+c[-8]
TypeError: can only concatenate list (not "str") to list
c[-11]+c[-10]+c[-9]+c[-8]+c[-7]
'love '
c[-11]+c[-10]+c[-9]+c[-8]
'love'
c[-13]
'i'
