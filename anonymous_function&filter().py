#anonymous functions(nameless/unknown functions)->these are nameless functions and we use a keyword called "lambda" to create anonymous functions.

#write a function to calculate 2*x+5 where x=5

'''def cal(x):
    return 2*x+5
print(cal(5))
'''

#runtime input
'''
def cal(x):
    return 2*x+5
x=int(input("Enter value"))
print(cal(x))
'''


#syntax for anynomous function

#var=lambda argument:expression

'''
a=lambda x:2*x+5
print(a(5))
'''

'''
a=int(input("Enter value"))
b=lambda x:2*x+5
print(b(a))
'''


#mutiply 2 arguments
'''
a=lambda x,y:x*y
print(a(5,6))'''


#runtime input
'''
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=lambda a,b:a*b
print(c(a,b))'''


#codegnan
#o/p->CODEGNAN
'''
a=lambda a:a.upper()
print(a("codegnan"))


x="codegnan"
a=lambda x:x.upper()
print(a(x))


#using runtime input
x=input("Enetr x:")
a=lambda x:x.upper()
print(a(x))
'''

#a="python course"
#o/p->Python course
'''
b=lambda b:b.title()
print(b("python course"))

a="python course"
b=lambda a:a.title()
print(b(a))

#runtime input
a=input("Enter string:")
b=lambda a:a.title()
print(b(a))
'''

#firstname+lastname=fullname and it should be capital
'''
fname=input("Enter first name:")
lname=input("Enter last name:")
fullname=lambda fname,lanme:(fname+" "+lname).title()
print(fullname(fname,lname))
'''

#another method
'''
fname=input("Enter first name:")
lname=input("Enter last name:")
full=fname+" "+lname
a=lambda a:full.title()
print(a(full))
'''

#taking multiple inputs using genetators and split method 
'''
fname,lname=[x for x in input("Enter fname and lname:").split(",")]
a=lambda fname,lname:(fname+" "+lname).title()
print(a(fname,lname))
'''


#filter()
'''
a=[10,30,50,100,127,39,45,67,200]
for i in a:
    if i%2==0:
        print(i)
'''

#using filter()-->used to print the wanted data and removes unwanted data
#filter accepts only two arguments
'''
a=[10,30,50,100,127,39,45,67,200]
b=list(filter(lambda x:x%2==0,a))
print(b)
'''

#removes none values and prints original data
'''
a=[[],(),{},"",4,6.8,"python",5+9j,True,False]
b=list(filter(None,a))    #by using 'None' it will remove all the empty datatypes
print(b)
'''

#max()->prints maximum value fron the collection
#print(max(5,6,7,8,9,2,3))

#min()->prints the minimum value from the collection
#print(min(45,67,23,90,32))

#sum->prints the sum of all values
'''a=7,6,5,9,3,4
print(sum(a))'''

#using list
#print(sum([3,5,6,7]))

#map()-->each object from a collection and forms a new collection

'''
a=[2,3,4,5,10,12,16,18,20,25]
b=[1,2,3,4,11,13,15,17,19,22]
c=list(map(max,a,b))
print(c)


a=[2,3,4,5,10,12,16,18,20,25]
b=[1,2,3,4,11,13,15,17,19,22]
c=list(map(min,a,b))
print(c)
'''

#taking multiple inputs
'''
a=input("data1:")
b=input("data2:")
print(a+b)
'''

#taking multiple inputs at a time
'''
a,b=input("Enter the names:").split(",")
print(a+b)
'''

#taking multiple runtime inputs using generators
'''
a,b=[x for x in input("Enter names:").split(",")]
print(a+b)
'''
#usind map()
'''
a,b=map(str,input("Enter names:").split(","))
print(a+b)
'''

#taking mutiple integer runtime inputs
'''
a=int(input())
b=int(input())
print(a+b)
'''

#taking mutiple runtime integet inputs using generators
'''
a,b=[int(x) for x in input("Enter a and b values:").split(",")]
print(a+b)
'''
'''
a,b=int(input()).split(",")
print(a+b)'''  #error

#taking mutiple runtime integer iputs using map
'''
a,b=map(int,input("enter values:").split(","))
print(a+b)
'''

#list using map()
'''
a=list(map(int,input("enter values:").split(",")))
print(a)
print(type(a))
'''

#tuple using map()
'''
a=tuple(map(int,input("enter values:").split(",")))
print(a)
print(type(a))
'''

#set using map()
'''
a=set(map(int,input("enter values:").split(",")))
print(a)
print(type(a))
'''

#eval it taks any type of data and prints in a list
'''
a=list(map(eval,input("enter values:").split(",")))
print(a)
print(type(a))
'''

#taking runtime dictionary values
'''
a=input("Enter key and value pairs:")
b=dict(i.split(":") for i in a.split(","))
print(b)
'''


#Task-Marks analysis report

n=int(input("Enter number of students:"))
a=[]
for i in range(1,n+1):
    marks=int(input(f"Enter Student{i} Marks:"))
    a.append(marks)
print("...........Marks Analysis Report.............")
print("Total Number of Students:",n)
print("Highest Marks:",max(a))
print("Lowest Marks:",min(a))
print("Total Marks:",sum(a))
print("Average Marks:",sum(a)/n)


















