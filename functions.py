d#FUNCTIONS

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
'''def add():
    print("The Sum is:",a+b)
def sub():
    print("The Diff is:",a-b)   
def mul():   
    print("The Mul is:",a*b)
while True:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    opts=int(input("1.add 2.sub 3.mul"))
    if opts==1:
        add()
    elif opts==2:
        sub()
    elif opts==3:
        mul()'''


#----------------------------------------------------------------------
#keyword and positional arguments

'''def Details(id,name,mailid):
    id=10
    name="poojitha"
    mailid="poojitha@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid") #givig keywords same as arguments'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id="20",name="varshi",mailid="v@gmail.com")  #givig values same as arguments with keywords
Details(30,"tara","t@gmail.com")        #givig values same as arguments
Details("s@gmail.com",40,"sai")         #givig values not same as arguments & it will not print same as arguments
Details(mailid="c@gmail.com",id=50,name="chaitra")''' #givig values not same as arguments but with keywords & in different postions &it will print correct order

#-------------------------------------------------------------------------

#default arguments

'''def Grocery(item,price):
    print("Item is: %s" %item)
    print("Price is: %.2f" %price)
Grocery("sugar",100)'''  #giving values in the calling function


'''def Grocery(item="rice",price=1500):  #giving values at the function
    print("Item is: %s" %item)
    print("Price is: %.2f" %price)
Grocery()'''      



'''def Grocery(item,price=200):   #for first arg value is not giving in the function
    print("Item is: %s" %item)
    print("Price is: %.2f" %price)
Grocery("ghee")'''



'''def Grocery(item="dhal",price):
    #non def arg follows def args
    print("Item is: %s" %item)
    print("Price is: %.2f" %price)
Grocery(100)''' #it will raise error because for the first arg we given the value but for the second arg not given the value

#------------------------------------------------------

#Task

'''def Cake(name,price,qty):
    print("Cake name is:%s" %name)
    print("Price is:%d" %price)
    print("Quantity is:%dKg" %qty)
Cake("venela",500,1)'''


'''def Cake(name="chocolate",price=700,qty=2):
    print("Cake name is:%s" %name)
    print("Price is:%d" %price)
    print("Quantity is:%dKg" %qty)
Cake()'''

'''def Cake(name,price,qty=1):
    print("Cake name is:%s" %name)
    print("Price is:%d" %price)
    print("Quantity is:%dKg" %qty)
Cake("redvlvet",600)'''#without giving the value for first,second args & for giving remaining agrs it will accept


'''def Cake(name,price=1000,qty=2):
    print("Cake name is:%s" %name)
    print("Price is:%d" %price)
    print("Quantity is:%dKg" %qty)
Cake("pineapple")''' #without giving the value for first arg & for giving remaining agrs it will accept


'''def Cake(name="mango",price,qty):
    print("Cake name is:%s" %name)
    print("Price is:%d" %price)
    print("Quantity is:%dKg" %qty)
Cake(900,2) '''   #Error because if we give value to first arg the we need to give the values for remaining args also, otherwise it will raise error.

#----------------------------------------------------------

#(*)argument--->it is used to unpack the data

#list
'''a=[2,3,4,5,6,7]
print(a)
print(*a)'''

#tuple
'''a=(2,3,4,5,6,7)
print(a)
print(*a)'''

#set
'''a={2,3,4,5,6,7}
print(a)
print(*a)'''

#dict
'''a={"name":"poojitha","city":"vij"}
print(a)
print(*a)''' #it will return only keys



'''a,b,c=3,4,5
print(a)
print(b)
print(c)'''


'''a,b,c=2,3,4,5,6,8
print(a)
print(b)
print(c)'''#Error



#by using (*)arg it is possible
'''*a,b,c=2,3,4,5,6,8
print(*a)     #a=2 to 5
print(b)      #b=6
print(c)      #c=8


a,*b,c=2,3,4,5,6,8
print(a)
print(*b)
print(c)   #it will give first value to 'a' and last value to 'c' &ramaining all values to 'b'

a,b,*c=2,3,4,5,6,8
print(a)
print(b)
print(*c)'''

#two starts(*) not possible

#strings

'''b="python"
print(b)
print(*b)'''


'''a,b,c="codegnan"
print(a)
print(b)
print(c) '''#error


'''a,b,c="cod"
print(a)
print(b)
print(c)'''

#using (*)arg for strings


'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)

a,*b,c="codegnan"
print(a)
print(*b)
print(c)

a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''

#---------------------------------



















