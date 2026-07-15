#FUNCTIONS

#without using functions

'''a=10
b=20
print("The sum is:",a+b)
print("The diff is:",a-b)
print("The product is:",a*b)
a=100
b=200
print("The sum is:",a+b)
print("The diff is:",a-b)
print("The product is:",a*b)
a=1000
b=2000
print("The sum is:",a+b)
print("the diff is:",a-b)
print("The product is:",a*b)'''


#Using functions concept

'''def calculate(a,b):
    print("The sum is:",a+b)
    print("The diff is:",a-b)
    print("The product is:",a*b)
    print("The div is:",a/b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''


'''def calculate(a,b):
    print("The integer division is:",a//b)
    print("The power is:",a**b)
    print("The modulo is:",a%b)
   
calculate(1,2)
calculate(3,4)
calculate(5,6)'''


#Taking runtime input
#we should not pass arguments

'''def cal():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(a+b)
cal()'''
    

#using while loop->it will iteratate the loop untile condition false
'''while True:
    def cal():
        a=int(input("Enter a:"))
        b=int(input("Enter b:"))
        print(a+b)
    cal()'''


#using recursion-->A function which is call by itself

'''def cal():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(a+b)
    cal()  #calling function by itself
cal()'''


'''def fullname():
    fname=input("First name:")
    lname=input("Last name:")
    print((fname+" "+lname).title())
fullname()'''


#Diff B/w Print and Return

'''def mul(a,b):
    print(a*b)
mul(5,6)'''

'''def mul(a,b):
    return a*b
print(mul(2,3))'''   #by using only return it will not print the result


#Print v/s Return

'''def program(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
program(6,5)'''


'''def program(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
print(program(6,5))''' #it will return only first return value and the terminate


'''def program(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e     #by using single return we will get the o/p
print(program(6,5))'''

#------------------------------------------------------------------

#Tasks
#splitbill()

'''def splitbill():
    persons=int(input("No of persons:"))
    bill=int(input("Total Bill:"))
    split=bill/persons
    print("Bill Per Person:",split)
splitbill()'''
    

'''def splitbill():
    persons=int(input("No of persons:"))
    bill=int(input("Total Bill:"))
    split=bill//persons
    print("Bill Per Person:",split)
    print("Bill Per Person:{}".format(split))  #.format method
    print(f"Bill per person:{split}")    #fstring 
splitbill()'''


#without storing in a variable for (.format,fstring)
'''def splitbill():
    persons=int(input("No of persons:"))
    bill=int(input("Total Bill:"))
    print("Bill Per Person:",bill//persons)
    print("Bill Per Person:{}".format(bill//persons))  #.format method
    print(f"Bill per person:{bill//persons}")    #fstring 
splitbill()'''


#Task-2
#perform the operation based on provided option
'''while True:
    def all():
        a=int(input("Enter a:"))
        b=int(input("Enter b:"))
        opts=int(input("1.add,2.sub,3.mul"))
        if opts==1:
            print("The Sum is:",a+b)
        elif opts==2:
            print("The Diff is:",a-b)
        else:
            print("The Mul is:",a*b)
    all()'''


#using multiple def keywords
def add():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    
    opts=int(input("1.add,2.sub,3.mul"))
    if opts==1:
        print("The Sum is:",a+b)
    elif opts==2:
        print("The Diff is:",a-b)
    else:
        print("The Mul is:",a*b)
def sub():
    a=int(input("Enter a:"))
    
    opts=int(input("1.add,2.sub,3.mul"))
    if opts==1:
        print("The Sum is:",a+b)
    elif opts==2:
        print("The Diff is:",a-b)
    else:
        print("The Mul is:",a*b)
    b=int(input("Enter b:"))
def mul():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    
    opts=int(input("1.add,2.sub,3.mul"))
    if opts==1:
        print("The Sum is:",a+b)
    elif opts==2:
        print("The Diff is:",a-b)
    else:
        print("The Mul is:",a*b)
add()
sub()
mul()






