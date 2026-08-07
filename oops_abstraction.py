#ABSTRACTION-->Hiding unnecessary infomation from user is called abstraction
#Abstract Class-->In abstract class we have one or more abstract methods
#Abstract Method-->The method is declared without implementation

#examples->ATM application,all apps,car

'''
class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()
'''

'''
from abc import ABC,abstractmethod
class A():
    def method1(self):
        print("python")
obj1=A()
obj1.method1()
'''

'''
from abc import ABC,abstractmethod
class A():
    def method1(self):
        print("data")
obj1=A()
obj1.method1()
'''

'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method(self):
        print("codegnan")
obj1=A()
obj1.method1()
'''  #error ,because abstract class should have one or more methods



#2 abstract methods are there in class A and those are implemented in class B which is inherited by the class A.
'''
from abc import ABC,abstractmethod
class A():
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("Python")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("Data Science")
    def method3(self):
        print("Machine Learning")
b=B()
b.method1()
b.method2()
b.method3()
'''




















