#OOPS
#syntax
'''
class class_name():
    #attributes
    name="poojita"
    age=22
    place="vij"
    def function_name(method_name):
        print("statements......")
object_name=class_name()
object_name.function_name'''


#Class Declaration
'''
class Details():
    name="Poojitha"
    age=22
    place="Vij"
    def Display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.Display()
'''

#Object Instantiation-->creating objects instantly
#we can add multiple user Details
'''
class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
a.data("Poojitha",22,"Vij")
a.display()
b=Details()
b.data("Priya",21,"Hyd")
b.display()
'''

#Object Initialization
#Constructor-->__init__-->we can give this as class name
#directly pass the values in the class at the creation of the object
'''
class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("Poojitha",22,"vij")
a.display()
'''


#user input
'''
class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)

name=input()
age=int(input())
place=input()
a=Details(name,age,place)
a.display()
'''


'''
class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)

a=Details(input("name"),int(input("age")),input("place"))
print(dir(a))               
a.display()
'''


'''
class Details():
    #creating a constructor
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()
'''

#Difference b/w "_"  and  "__"
#when user wants to create a variable with "__" our python interpreter treats as a special variable to avoid name conflicts with methods and inner classes 

'''
class employee():
    def __init__(self):
        self.name="poojitha"
        self._mailid="poojitha@gmaul.com"
        self.__salary=30000   #private variable
a=employee()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._employee__salary)
'''


#3 employee datails
'''
class employee1():
    def __init__(self):
        self.name="poojitha"
        self._mailid="poojitha@gmaul.com"
        self.__salary=30000   #private variable
class employee2():
    def __init__(self):
        self.name="varshitha"
        self._mailid="varshi@gmail.com"
        self.__salary=50000   #private variable
class employee3():
    def __init__(self):
        self.name="priya"
        self._mailid="priya@gmail.com"
        self.__salary=20000  #private variable
        
e1=employee1()
print(dir(e1))
print(e1.name)
print(e1._mailid)
print(e1._employee1__salary)  #print using "_classname__attributename"

e2=employee2()
print(dir(e2))
print(e2.name)
print(e2._mailid)
print(e2._employee2__salary)

e3=employee3()
print(dir(e3))
print(e3.name)
print(e3._mailid)
print(e3._employee3__salary)
'''


#POLYMORPHISM
#OPERATOR OVERLOADING-->performing same operator differently based on datatypes.

#'+' operator for integers->it performs addition of two values
'''
a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(5))
print(a.__sub__(1))
print(a.__mul__(10))
#print(a.__div__(2))   #ther is no div method
print(a.__pow__(b))
print(a.__ge__(7))
print(a.__le__(10))
print(a.__eq__(2))
'''

#'+' opertaor for list->it merges two lists
'''
a=[2,3,4,5,6];b=[6,7,8,9,10]
print(a+b)
print(a.__add__(b))

print(a.__getitem__(2))     #prints that index value
print(a.__getitem__(4))     #prints that index value
'''

#'+' operator for string->it concatinate both the strings
'''
a="code";b="gnan"
print(a+b)
print(a.__add__(b))

print(a.__add__(" "+b))
      
a="python";b="counse"
print(a+b)
print(a.__add__(" "+b).title())

print("poojitha".__add__(" "+"siliveru").title())
'''


#OPERATOR OVERRIDING-->
'''
class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):    # inside add method operation will be performed
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(5)
y=B(6)
print(x+y)  #addition operator

x=5   #without class name
y=4   #without class name
print(x+y)  #additon of x and y will be performed

'''

#METHOD OVERLOADING-->
'''
class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum is:",a+b+c)
        elif a!=None and b!=None:
            print("The product is:",a*b)
        else:
            print("Program Ends...")
x=new()
x.sum()
x.sum(2,3,4)
x.sum(2,3)
'''

#METHOD OVERRIDING
#same method name
'''
class Animal():
    def speak(self):
        print("Animal can make sounds")
class Dog():
    def speak(self):
        print("Dog Barks")
a=Animal()
d=Dog()
a.speak()   #same method overrides based on objects
d.speak()
'''

'''
class Vehicle():
    def speed(self):
        print("Vehicle speed is 20km/h")
class Car():
    def speed(self):
        print("Car Speed is 25km/h")
v=Vehicle()
c=Car()
v.speed()
c.speed()
'''


class car():
    def vehicle(self):
        print("Thar")
class bike():
    def vehicle(self):
        print("vespa")
a=car()
b=bike()
a.vehicle()
b.vehicle()










