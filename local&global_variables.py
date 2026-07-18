#Global and Local Variables
#-----------------------------
#variables in side and outside the function is called global and local variables.
#A variable is define the above the function and is accessible to the entire global space is called global varibale.
#A variable is inside the function is called local varible.


#first case of global variable

'''a=4
def check1():
    print("inside value is",a)
check1()
print("outside value is",a)'''



#second case of global variable
'''a=12
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)'''



#third case->both local and global variables

'''a=10
def check3():
    a=8
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=13  #local variable
    b=b+a
    print("value of b is",b)
check3()
print("outside value of a",a)
print("outside value of b",b) ''' #error because b is local varuable



#usage of global keyword
#when user wants to access the global var inside the function directly and carry forward the updated value even the outside the funtion the we need to use global keyword.


a=4
def final():
    global a,b
    print("inside value is",a)
    a=15
    print("updated value",a)
    b=20
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)





















    
