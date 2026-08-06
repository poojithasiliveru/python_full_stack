#INHERITANCE

#single inheritace
'''
class RBI():#parent class
    cash=100000
    def available_cash(cls):
        print("available cash is:",cls.cash)
        print("available cash is:",RBI.cash)
class SBI(RBI):  #child-1
    pass
class HDFC(RBI):  #child-2
    cash=50000
    def new_cash(cls):
        print("new cash is:",cls.cash+cls.cash)
        print("new cash is:",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()
'''

#MULTIPLE INHERITANCE->Acquring properties from one class to another class

#without inheritance we have to create the objects for parent classes also
'''
class father(): #parent class
    def height(cls):
        print("Father height is 5.5 inches")
class mother(): #parent class
    def weight(cls):
        print("Mother weight is 55 kgs")
class child():  #child class 
    def dob(cls):
        print("DOB of child is 4/02/2004")
        
a=child()
b=father()
c=mother()
a.dob()
b.height()
c.weight()
'''

#with inheritance-> object creation for only child class, we can also access the parent class methods
'''
class father(): #parent class
    def height(cls):
        print("Father height is 5.5 inches")
class mother(): #parent class
    def weight(cls):
        print("Mother weight is 55 kgs")
class child(father,mother):  #child class inherits from parent class
    def dob(cls):
        print("DOB of child is 4/02/2004")
        
a=child()
a.dob()
a.height()       #with the child class object only, we can call the parent class methods
a.weight()       #with the child class object only, we can call the parent class methods
'''


#TASK
'''
class father(): #parent class
    h=5.8
    def height(cls):
        print(f"Father height is {cls.h} inches")
        print(f"Father height is {father.h} inches")
class mother(): #parent class
    w=55
    def weight(cls):
        print(f"Mother weight is {cls.w} kgs")
        print(f"Mother weihgt is {mother.w} kgs")
class child(father,mother):  #child class inherits from parent class
    def dob(cls):
        print(f"DOB of child is 4/02/2004")
        print(f"Father height is {cls.h} inches")
        print(f"Mother weight is {cls.w} kgs")
a=child() 
a.dob()
a.height()       #with the child class object only, we can call the parent class methods
a.weight()       #with the child class object only, we can call the parent class methods
'''


#MULTILEVE INHERITANCE->Acquring properties from grandparent to parent and parent to child

'''
class GrandParent():
    def land(cls):
        print("Grand Parent has 10 acres land")
class Parent(GrandParent):  #inherit form grandparent
    def house(cls):
        print("Parent has a 100 sqrt house")
class child(Parent):       #inherit from parent   
    def car(cls):
        print("Child has a BMW car")
a=child()
a.car()
a.land()     #with the child class object only, we can call the grandparent class methods
a.house()    #with the child class object only, we can call the parent class methods
'''

#HIERARCHICAL INHERITANCE->it is where one parent class is inherited by multiple child classes

'''
class Employee():  #parent class
    def company_name(self):
        print("Cognizent")
class Trainer(Employee):   #child class-1
    def teach(self):
        print("Trainer teachs the code")
class Developer(Employee):   #child class-2
    def code(self):
        print("Develops the code")
a=Trainer()         #object for trainer class
b=Developer()       #object for developer class
a.teach()
a.company_name()    #access parent class method with the trainer class object
b.code()
b.company_name()    #access parent class method with the developer class object

'''


#HYBRID INHERITANCE-->it means combining more than one type of inheritance->for example (hierarchial+multiple)
'''
class Person():
    def details(self):
        print("Poojitha")
class Trainer(Person):    #child-1 for person class
    def teach(self):
        print("Trainer will teach the code")
class Student(Person):   #child-2 for person class
    def study(self):
        print("Student should learn the code")
class Program_Manager(Trainer,Student):   #child class for trainer & student classes
    def manager(self):
        print("Assign the classes")
p=Program_Manager()
p.manager()
p.details()
p.teach()
p.study()
'''
    

#SUPER --> super()->

'''
class parent(): #super class
    def __init__(self,name):
        self.name=name
        print("parent constrctor")
class child(parent): #sub class
    def __init__(self,name,age):
        self.age=age
        self.name=name
        print("child constructor")
a=child("poojitha",22)
print(dir(a))
print(a.name)
print(a.age)
'''

#To display the parent constructor

'''
class parent(): #super class
    def __init__(self,name):
        self.name=name
        print("parent constrctor")
class child(parent): #sub class
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("poojitha",22)
print(dir(a))
print(a.name)
print(a.age)
'''














