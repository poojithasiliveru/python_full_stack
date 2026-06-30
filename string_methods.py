Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#STRING METHODS
#len()
a="Python"
len(a)
6
b="Python Course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
e="Datascience"
len(e)
11
f="Data science"
len(f)
12
#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
#we should not use like a function
a.count("twinkle")
2
a.count("t")
5
a.count(" ")
3
a. count("a")
1
#FIND A STRING---find()
#find the index position of a particular character
a="code"
a.find("d")
2
a.find("e")
3
b="hello"
b.find("l")
2
b[2:4]
'll'
#ESCAPE SEQUENCES
#\n->NEW LINE
#\t->TAB SPLACE (4 to 8 spaces)
a"name\nmobile\tmailid\nclg"
SyntaxError: invalid syntax
a="name\nmobile\tmailid\nclg"
print(a)
name
mobile	mailid
clg
b="name:Poojitha\nmobile:8576385678\tmailid:Pooji@gmail.com\nclg:lbrce
SyntaxError: unterminated string literal (detected at line 1)
b="name:Poojitha\nmobile:8576385678\tmailid:Pooji@gmail.com\nclg:lbrce"
print(b)
name:Poojitha
mobile:8576385678	mailid:Pooji@gmail.com
clg:lbrce
#REPLACE->replace("old word","new word")->replaces character or word
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a
'wait until you succeed'
b="wait wait until you succeed"
b.replace("Wait","work")
'wait wait until you succeed'
b
'wait wait until you succeed'
b.replace("wait","work")
'work work until you succeed'
b.replace("wait","work",1)
'work wait until you succeed'
#UPPER->CONVERT ALL THE STRING TO UPPER
a="hello"
a.upper()
'HELLO'
b="HIII"
b.upper()
'HIII'
c="Hello"
c.upper()
'HELLO'
#LOWER->CONVERT ALL THE STRING TO LOWER
a="HELLO"
a.lower()
'hello'
b="Hello"
b.lower()
'hello'
c="hello"
c.lower()
'hello'
#CAPITALIZE-->FIRST LETTER OF THE WORD WILL BE CATALIZED
a="codegnan"
a.capitalize()
'Codegnan'
b="data"
b.capitalize()
'Data'
#TITLE-->EVERY WORD FIRST LETTER WILL BE CAPITAL
a="python course"
a.title()
'Python Course'
b="data science"
b.title()
'Data Science'


a="java"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalnum()
True
b="python course"
b.isalpha()
False
c="pythoncourse"
b.alnum()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    b.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
b.isalnum()
False
c.isalnum()
True
c.isalpha()
True
d="1234"
d.isdigit()
True
d.isalnum()
True
d.isalpha()
False
e="datat123"
e.isalpha
<built-in method isalpha of str object at 0x000001DF479AA370>
e.isalpha()
False


a="hello python"
a.startswith("h")
True
a.endswith("n")
True
b="cloud computing"
b.startswith("c")
True
b.endswith("g")
True
#STRIP->strip()-->used to remove white spaces
#lstrip->remove left space
#rstrip->remove right space
a="                 Poojitha                 "
a.strip()
'Poojitha'
a.lstrip()
'Poojitha                 '
a.rstrip()
'                 Poojitha'
b="    codenana      "
b.strip()
'codenana'
b.lstrip()
'codenana      '
b.rstrip()
'    codenana'
c="     hii    hello   how   "
c.strip()
'hii    hello   how'
c.lstrip()
'hii    hello   how   '
c.rstrip()
'     hii    hello   how'
#IR WILL NOT REMOVE MIDDLE SPACES

#SPLIT-->split()-->split the words in a scentence
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am in vijayawada"
b.split()
['i', 'am', 'in', 'vijayawada']
#LETTER SPLITING IS NOT POSSIBLE
c="Codegnan"
c.split()
['Codegnan']


#JOIN-->merges the group of words
#join()
a="vij hyd viz"
a.join()
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    a.join()
TypeError: str.join() takes exactly one argument (0 given)
"".join(a)
'vij hyd viz'
b="vij","hyd","viz"
"".join(b)
'vijhydviz'
" ".join(b)
'vij hyd viz'
"k".join(b)
'vijkhydkviz'
"k ".join(b)
'vijk hydk viz'

#CONCATINATION->ADDING TO STRINGS
a="hello"
b="world"
print(a+b)
helloworld
print(a+" "+b)
hello world
fname="poojitha"
lname="siliveru"
print(fname+lname)
poojithasiliveru
print(fname+" "+lname)
poojitha siliveru
print(fname.title()+" "+lname.title())
Poojitha Siliveru
print((fname+" "+lname).title())
Poojitha Siliveru

#FORMATING
a=4
b=9
print("The sum is",a+b)
The sum is 13
x="vij"
print("City is",x)
City is vij
#format method
a="motu"
b="patlu"
print("hello",a+b)
hello motupatlu
print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> #fstring->FORMATING STRING
>>> a="sita"
>>> b="ram"
>>> print(f"hello {a}{b}")
hello sitaram
>>> print(f"hello {a} {b}")
hello sita ram
>>> print(f"hello {a} hello {b}")
hello sita hello ram
>>> print(f"hello {a} hii {b}")
hello sita hii ram
>>> 
>>> a=4
>>> b=5
>>> print("The product is {}{}".format(a*b))
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    print("The product is {}{}".format(a*b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> c=a*b
>>> print("the product is {}}.format(c)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("the product is {}".format(c))
...       
the product is 20
>>> print(f"the product is {c}")
...       
the product is 20
>>> print("The product is {}".format(a*b))
...       
The product is 20
>>> print(f"the product is {a*b}")
...       
the product is 20
