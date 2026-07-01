Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#SETS
#DOES NOT ALLOW DUPLICATE DATA
#it uses {}
#it is unordered
a={5,8.9,"Poojitha",6+7j,True,False}
a
{False, True, 5, 'Poojitha', 8.9, (6+7j)}
type(a)
<class 'set'>
#SUBSET
a={3,4,5,6,7,8}
b={4,5,6,7,8}
b.issubset(a)
True
b.issuperset(a)
False
a.issubset(b)
False
b.issuperset(a)
False
a.issuperset(b)
True
#UNION-->MERGING OF TWO SETS WITHOUT ALLOWING DUPLICATES
a={3,4,5,6,78}
b={1,2,3,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 9, 10, 78}
c={6,7,8,9,10,6,7}
print(c)
{6, 7, 8, 9, 10}
#INTERSECTION-->intersection-->prints common values
a={3,4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.intersection(b)
{8, 9, 6, 7}
c={11,4,9}
b.intersection(c)
{9, 11}
#UPDATE-->updated the sets
a={10,20,30,40,50}
b={40,50,60,70,80}
a
{50, 20, 40, 10, 30}
a.update(b)
a
{70, 40, 10, 80, 50, 20, 60, 30}
b
{80, 50, 70, 40, 60}
b.update(a)
b
{70, 40, 10, 80, 50, 20, 60, 30}
#ADD A ELEMENTS TO B AND A SET IS UPDATED
#ADD "B" ELEMENTS TO "A" AND THEN THE "B" SET IS UPDATED

#DIFFERENCE
#REMOVES COMMON ELEMENTS
a={4,5,6,7,8,9,10,11}
b={3,4,5,6,7,11,12,13}
a.difference(b)
{8, 9, 10}
b.difference(a)
{3, 12, 13}
#SYMMETRIC DIFFERENCE-->REMOVES COMMON VALUES AND PRINTS OPPOSITE VALUES
a={3,4,5,6,7,8,9}
b={1,3,5,7,8,11,13}
a.symmetric_difference(b)
{1, 4, 6, 9, 11, 13}
b.symmetric_difference(a)
{1, 4, 6, 9, 11, 13}
c={9,7,6,5,4}
d={6,9,5}
c.symmetric_difference(d)
{4, 7}
d.symmetric_difference(c)
{4, 7}

#INTERSECTION_UPDATE-->COMMANON ELEMENTS WILL BE STRORED IN VARIABLE "a"
a={1,3,5,7,9,11,13}
b={2,3,4,6,7,9,11,12}
a.intersection_update(b)
a
{11, 9, 3, 7}
b
{2, 3, 4, 6, 7, 9, 11, 12}
b.intersection_update(a)
b
{3, 9, 11, 7}
a
{11, 9, 3, 7}
#difference_update()-->
a={2,3,4,5,6,7}
b={9,8,7,5,6,4,2}
a.difference_update(b)
a
{3}
b.difference_update(a)
b
{2, 4, 5, 6, 7, 8, 9}
#SYMMETRIC_DIFFERENCE_UPDATE
a={11,12,13,14,15,16,17}
b={13,14,151,6,17,18}
a.symmetric_difference_update(b)
a
{6, 11, 12, 15, 16, 18, 151}
>>> b.symmetric_difference_update(a)
>>> b
{11, 12, 13, 14, 15, 16, 17}
>>> #POP-->IT WILL DELELTE FIRST ELEMEMT
>>> a={4,5,6,7,8,9,10}
>>> a.pop()
4
>>> a.pop(5)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.pop(5)
TypeError: set.pop() takes no arguments (1 given)
>>> a
{5, 6, 7, 8, 9, 10}
>>> #REMOVE--->DELETES PARTICULAR VALUE
>>> a.remove(5)
>>> a
{6, 7, 8, 9, 10}
>>> a.remove(10)
>>> a
{6, 7, 8, 9}
>>> #DISCARD-->delete particular element
>>> a={3,4,5,6,7,8,9}
>>> a.discord(5)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.discord(5)
AttributeError: 'set' object has no attribute 'discord'. Did you mean: 'discard'?
>>> a.discard(5)
>>> a.discard(9)
>>> a
{3, 4, 6, 7, 8}
>>> b=a.copy()
>>> b
{3, 4, 6, 7, 8}
>>> #CLEAR()-->clear all tha values
>>> a.clear()
>>> a
set()
>>> b=set()
#ADD-->ADD 1 ELEMENT AT A TIME
a.add(5)
a
{5}
a.add(8)
a
{8, 5}
#LENGTH
a.len()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a.len()
AttributeError: 'set' object has no attribute 'len'
len(a)
2
#count and index methods are not there because it a non duplicate and unordered
#ISDISJOINT-->IT SHOULD HAVE DIFFERENT ELEMENTS IN THE BOTH SETS THE IT WILL GIVE "True" or "False"
a={2,3,4,5}
b={9,8,7,6}
a.isdisjoint(b)
True
b.isdisjoint(a)
True
a={2,3,4,5}
b={9,8,7,6,5}
a.isdisjoint(b)
False
b.isdisjoint(a)
False
