#generators

#list comprehension->[exp for var in collection/range]
'''a=[i for i in range(16)]
print(a)
print(type(a))
'''

#Generator syntax->(exp for var in collection/range)
a=(i for i in range(16))
'''print(a)
print(*a)
print(type(a))


b=list(a)
print(b)'''

'''
print(tuple(a))
print(set(a))'''

#yield keyword with (*)->it will increase the value because of 'yield'
'''a,b=[int(x) for x in input("Enter the values").split(",")]
def check(a,b):
    while(a<b):
        yield a  #it will not terminate
        a=a+1
        yield a
print(*check(a,b))
'''

#return keyword without (*)-> it will terminate the value
'''
a,b=[int(x) for x in input("Enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        #return a --->increment by one value and terminate the function
    return a   #-->iterate and print last iterated value
print(check(a,b))

'''



#yield v/s return

'''
def mygen():
    #return "vij"  #it will terminate at the first return only
    #return "hyd"
    #return "vzg"
    return "vij","hyd","vzg"   #it will print in a packed form
print(*mygen())  #->it will unpack the data
'''

'''
def mygen():
    yield "python"
    yield "java"
    yield "DSA"   #prints all valus at a time

print(*mygen())'''



def mygen():
    yield "python"
    yield "java"
    yield "DSA"

print(*mygen())
#next-->print one value at a time
d=mygen()
print(next(d)) #prints "python"
print(next(d)) #prints "java"
print(next(d)) #prints "DSA"

























