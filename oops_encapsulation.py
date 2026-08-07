#ENCAPSULATION
#pubilc data,protected data,private data

#public data

'''
class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj=child()
obj.method1()
obj.method2()
print(obj.publicdata)
'''

#protected data

'''
class parent():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj=child()
obj.method1() #call with the method_name
obj.method2()
print(obj._protecteddata)   #call with the variable name
'''


#private data
#examples->security purpose

'''
class parent():     #parent class
    __privatedata="poojitha"
    def method1(self):
        print(self.__privatedata)
class child(parent):  #child class
    def method2(self):
        print(self._parent__privatedata)   #to access the private data in child class we have to use parent class name
obj=child()
obj.method1() #calling with the method_name
obj.method2()
print(obj._parent__privatedata)   #calling with the variable_name
'''








