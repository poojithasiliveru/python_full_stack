#Built-in functions

#print(dir()) -->dir->collection of files

#print(dir("__builtins__"))  #prints all builtin functions


a="codegnan"
'''
print(a)

print(list(a))
print(tuple(a))
print(set(a))
'''
#print(dict(a)) #error because it acceps key and value pairs

#fromkeys()->using fromkeys it is possible
'''
b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"poojitha")  #for all the keys the "poojitha" value will be assigned
print(c)

c["d"]="python"  #replace  for key "d" with value "python"
print(c)'''


#eval--->it accepts any data type/all datatypes

'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''


'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''
while True:
    a=(input("a value"))
    b=(input("b value"))
    print(a+b)''' #it accepts all datatypes but it will concatinate them not do the addition

'''
while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''      #it accepts all datatypes & it does addition



#zip->we can combime multiple collections into one collections in both collectons the no. of value shold be equal

'''a=[10,20,30,40,50,60]
names=["poojitha","varshita","sita","tara","ram","maya"]
print(a+names)  #it will combine both collections but not 1 from collection1 to 1 from collection2

'''
'''b=zip(a,names)
print(b)'''

#for combining two collectins we should use any one of collection datatype
'''
c=list(zip(a,names))
print(c)

d=tuple(zip(a,names))
print(d)

e=set(zip(a,names))
print(e)

f=dict(zip(a,names))
print(f)
'''

#enumerate()->we can give counter to the collection

'''names=["nikitha","taruni","siri","kalyani","prameela"]
for i in range(len(names)):
   print(i,names[i])
   '''

'''
names=["nikitha","taruni","siri","kalyani","prameela"]
b=list(enumerate(names))
print(b)


names=["nikitha","taruni","siri","kalyani","prameela"]
b=list(enumerate(names,10)) #it start assigan value from 10 onwards
print(b)

names=["nikitha","taruni","siri","kalyani","prameela"]
b=list(enumerate(names,100)) #it start assigan value from 100 onwards
print(b)
'''

'''
names=["nikitha","taruni","siri","kalyani","prameela"]
b=tuple(enumerate(names))
print(b)

names=["nikitha","taruni","siri","kalyani","prameela"]
b=set(enumerate(names))
print(b)

names=["nikitha","taruni","siri","kalyani","prameela"]
b=dict(enumerate(names))
print(b)
'''


#ASCII

#chr()-->finds the character for the given number
'''
print(chr(65))
print(chr(90))
print(chr(93))
'''

#ord()-->finds the number for the given character
'''
print(ord("a"))
print(ord("z"))
print(ord("y"))
'''

#print A-Z & a-z
'''
for i in range(65,91):
    print(chr(i),end=" ")


for i in range(97,123):
    print(chr(i),end=" ")
    
'''

#ascii for given runtime input
'''
n=input("Enter name:")
for i in n:
    print(i,"-",ord(i))

'''


#Task
'''
while True:
    weight=float(input("Enter weight in kg:"))
    height=float(input("Enter heigth in meters:"))
    bmi=weight/height**2

    if bmi<=18.5:
        print("Under Weight")
    elif bmi>18.5 and bmi<=24.5:
        print("Healthy Weight")
    elif bmi>24.5 and bmi<=29.5:
        print("Over weight")
    elif bmi>=30.5:
        print("Obesity")
'''  


    
