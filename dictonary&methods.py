Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#DICTIONARY
#dict-->KEY VALUE PAIRS
a={"name":"Poojitha","city":"vij"}
a
{'name': 'Poojitha', 'city': 'vij'}
type(a)
<class 'dict'>
b={"Name":"Poojitha","Email_id":"poojitha@gmail.com","mobile_no":8967597494}
b
{'Name': 'Poojitha', 'Email_id': 'poojitha@gmail.com', 'mobile_no': 8967597494}
#KEYS-->PRINTS THE KEYS
b.keys()
dict_keys(['Name', 'Email_id', 'mobile_no'])
#VALUES-->PRINTS VALUES
b.values()
dict_values(['Poojitha', 'poojitha@gmail.com', 8967597494])
#ITEMS-->BOTH KEY AND VALUE PAIRS ARE PRINTD
b.items()
dict_items([('Name', 'Poojitha'), ('Email_id', 'poojitha@gmail.com'), ('mobile_no', 8967597494)])

a={"course":"Python","institute":"codegnan"}
a
{'course': 'Python', 'institute': 'codegnan'}
#UPDATE-->USED TO ADD KEY VALUE PAIRS ONE OR MORE
a.update{"name":"Poojitha"}
SyntaxError: invalid syntax
a.update({"name":"Poojitha"})
a
{'course': 'Python', 'institute': 'codegnan', 'name': 'Poojitha'}
3ADDING MUNTIBLE VALUE IN A SINGLE FLOWER BRACKET{}
SyntaxError: invalid decimal literal
#ADDING MUNTIBLE VALUE IN A SINGLE FLOWER BRACKET{}
a.update({"year":2026,"month":7,"date":2})
a
{'course': 'Python', 'institute': 'codegnan', 'name': 'Poojitha', 'year': 2026, 'month': 7, 'date': 2}
#SETDEFAULT-->DIRECTLY IT CONVERTS TO DICTIONARY FORMAT
b={"year":2026,"month":"july"}
b.setdefault("date",2)
2
b
{'year': 2026, 'month': 'july', 'date': 2}

#POP-->REMOVE THE LAST KEY VALUE PAIR OR SPECIFIC KEY
A={"hour":12,"min":4,"sec":56}
A.pop("sec")
56
#POPITEM-->DELETE LAST ITEM
A.popitem()
('min', 4)
A
{'hour': 12}

#GET-->ACCESSING THE VALUE
a={"college":"lbrce","branch":"cse"}
a
{'college': 'lbrce', 'branch': 'cse'}
a.get("college")
'lbrce'
a.get("branch")
'cse'
a
{'college': 'lbrce', 'branch': 'cse'}
a["college"]
'lbrce'
a["lbrce"]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a["lbrce"]
KeyError: 'lbrce'
#IT DOES NOT TAKE VALUES IT ONLY TAKES KEYS

#COPY-->COPIES THE DICTIONARY
a={"hour":4,"min":56,"sec":44}
a.copy()
{'hour': 4, 'min': 56, 'sec': 44}
a
{'hour': 4, 'min': 56, 'sec': 44}
#CLEAR-->CLEAR ALL THE DATA IN DICT
a.clear()
a
{}
>>> b={]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> b={}
>>> b.update({"name":"tara","college":"lbrce"})
>>> b
{'name': 'tara', 'college': 'lbrce'}
>>> 
>>> #LENGTH-->FIND THE LENGTH
>>> a={"name":"Poojitha","course":"python","year":2026}
>>> print(a)
{'name': 'Poojitha', 'course': 'python', 'year': 2026}
>>> len(a)
3
>>> 
>>> a={"name":"chaitra","city":"hyd","name":"chaitra"}
>>> print(a)
{'name': 'chaitra', 'city': 'hyd'}
>>> a={"name":"chaitra","city":"hyd","name":"tara"}
>>> print(a)
{'name': 'tara', 'city': 'hyd'}
>>> a={"name1":"chaitra","city":"hyd","name2":"chaitra"}
>>> print(a)
{'name1': 'chaitra', 'city': 'hyd', 'name2': 'chaitra'}
>>> #IT DOES NOT ALLOW DUPLICATE KEYS BUT IT WILL ALLOW DUPLICTE VALUES
>>> #IF WE TAKE SAME KEYS AND DIFFERENT VALUES IT WILL PRINT LATEST VALUE FOR THET KEY
>>> 
>>> #MULTIPLE VALUES FOR A SINGLE KEY
>>> a={"idnos":[10,20,30],"names":["maya","tara","chairta"],"marks":[60,70,80]}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['maya', 'tara', 'chairta'], 'marks': [60, 70, 80]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['maya', 'tara', 'chairta'], [60, 70, 80]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['maya', 'tara', 'chairta']), ('marks', [60, 70, 80])])
>>> 
