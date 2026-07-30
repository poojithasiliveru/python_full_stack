#EXCEPTION HANDLING->it will show the error in an information format

#try->Instructions from which we are expecting the exceptions(it handle all the errors if the all the instrictios that are raised errors)
#except->exceptions are raised in try block, it will be handle by this block.
#else->optional(no exceptions) it will execute only if 'try' block is executed
#finany->always it will display

'''
while True:
    try:                               #write the code that which we except the error
        a=int(input("Enter a:"))
        b=int(input("Enter b:"))
        c=a//b
        print(c)
    except:                            #it will handle the errors that are raised in try block
        print("Exception is raised")
    else:                              #it will execute only try block is executed
        print("No Exceptions")
    finally:                           #it will always execute
        print("Program ends...")
'''

#regex->regular expression are powerful tools(module) embedded in python which is mainly used to find a pattern within a given string or statements or files & we mainly use it for text manipulation.
#used for matching purpose

'''
a="Codegnan is in vijayawada"
print(a)
'''

'''
a="Codegnan\nis\tin nvijayawada"
print(a)
'''

#rstring->it will display same data that we provided
'''
a=r"Codegnan\nis\ninvijayawada"
print(a)
'''

#compile(),search(),findall(),split(),sub()

#sequence characters
'''
\w->it matches alphanumeric
\W->it matches non-alpha numeric
\d->it matches any digit
\D->it matches non-digit
\s->it represents white spaces
\S->it represents non-white spaces
'''


#compile()

import re
a="mat cat cap maths monkey cash code cup dog donkey mug money"

'''
b=re.compile(r"m\w\w")
print(b)


#search
c=b.search(a)
print(c)


b=re.search(r"m\w+",a)   #w+ print first word full
print(b)
'''

#findall()   ->it will print all words that are start with 'c'
'''
c=re.findall(r"c\w+",a)
print(c)


c=re.findall(r"c\w+",a)
print(*c)   #by using * it will unpack

'''

#split() ->it will split the given character
'''
d=re.split(r"m",a)
print(d)

e=re.split(r"\s",a)
print(e)
'''

#sub()->replace the old char with new
'''
f=re.sub("m","p",a)
print(f)
'''

#usage of \d
'''
x="year 2026 month 7 day 29"
g=re.findall("\d",x)
h=re.findall("\d+",x)  #it will merge
i=re.findall("\D+",x) 

print(g)
print(h)
print(i)
'''


b=re.findall(r"\bdo\w+",a)  #\b set the boundary to find particular pattern words
print(b)


b=re.findall(r"\bdo\w*",a)  #(we can use * also)\b set the boundary to find particular pattern words
print(b)




























