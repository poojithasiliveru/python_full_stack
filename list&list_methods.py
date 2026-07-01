Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#LIST
#list[]->COLLECTION OF DATA,,MUTABLE
a=[2,5.6,"Python",6+9j,True,False]
a
[2, 5.6, 'Python', (6+9j), True, False]
type(a)
<class 'list'>
c=[5]
c
[5]
type(c)
<class 'list'>
a=["Pythpn","c","c++","java"]
a.append("AI")
a
['Pythpn', 'c', 'c++', 'java', 'AI']
b=["ml","ds","php"]
b.append("c","Python")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b.append("c","Python")
TypeError: list.append() takes exactly one argument (2 given)
b.append(["c","Python"])
b
['ml', 'ds', 'php', ['c', 'Python']]
#EXTEND-->extend()-->we can give more than one value
a=["ml","ds","ai"]
a.extend(["c","c++","python"])
a
['ml', 'ds', 'ai', 'c', 'c++', 'python']
#INSERT-->insert(index,"value")-->inser i aparticular position
b=["vij","hyd"]
b.insert(1,"viz")
b
['vij', 'viz', 'hyd']
b.insert(1,"bengluru")
b
['vij', 'bengluru', 'viz', 'hyd']
#INDEX-->index("value")
#returns the index value
a=["black","white","pink","red"]
a.index("white")
1
a.index("red")
3
#COPY--->copy()--->copies the values of the another list
a.copy()
['black', 'white', 'pink', 'red']
b=a.copy()
b
['black', 'white', 'pink', 'red']
#COUNT -->count("data")-->gives the count of that data
b.count("pink")
1
#SORT-->sort()-->sorted in a alphabetical or ascending order
a=["grapes","apple","mango","banana"]
a.sort()
a
['apple', 'banana', 'grapes', 'mango']
b=[4,6,2,9,44,0]
b.sort()
b
[0, 2, 4, 6, 9, 44]
c=["67,90,34,22,11]
   
SyntaxError: unterminated string literal (detected at line 1)
c=[67,90,34,22,11]
   
c.sort()
   
#REVERSE--->reverse()-->prints from last to first
   
a=[7,5,4,9,55,3]
   
a.reverse()
   
a
   
[3, 55, 9, 4, 5, 7]
b=["css","html","javascript"]
   
b.sort()
   
b.reverse()
   
b
   
['javascript', 'html', 'css']
#POP-->pop(index_position)-->delete last element
   
a=["c"."c++","ml","ai"]
   
SyntaxError: invalid syntax
a=["c","c++","ml","ai"]
   
a.pop()
   
'ai'
a.pop(1)
   
'c++'
a
   
['c', 'ml']
#
   
#REMOVE-->remove("data")-->remove the particular data
   
a=["c","c++","ml","ai"]
   
a.remove("c++")
   
a
   
['c', 'ml', 'ai']
>>> a.remove("ai")
...    
>>> a
...    
['c', 'ml']
>>> #LENGTH-->len()-->gives the length of the list
...    
>>> a=["Poojia","Priya","Prince","Sweety"]
...    
>>> len(a)
...    
4
>>> b="Poojitha"
...    
>>> len(b)
...    
8
>>> b=["Poojitha"]
...    
>>> len(b)
...    
1
>>> #CLEAR-->clear()-->used to delete a variable
...    
>>> a.clear()
...    
>>> a
...    
[]
>>> a.append("Hii")
...    
>>> a
...    
['Hii']
>>> a.extend(["hello","how"])
...    
>>> a
...    
['Hii', 'hello', 'how']
