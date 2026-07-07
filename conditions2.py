#if-elif-else-->
#condition by using comparision operators
'''a=10
b=20
if a<b:
    print("less")
elif b>a:
    print("greater")'''


'''a=10
b=20
if a==b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''


'''a=10
b=20
if a==b:
    print("less")
elif b<a:
    print("greater")
elif a!=b:
    print("not equal")'''


'''a=10
b=20
if a==b:
    print("less")
elif b<a:
    print("greater")
else:
    print("true")'''

'''a=int(input("Enter a:"))
b=int(input("Enetr b:"))
if a<b:
    print("a less than b")
elif b>a:
    print("b greater than a")
else:
    print("nothing")'''


#if-elif-else->conditon using logical operator

'''a=4
b=9
if a<b and b>a:
    print("small")
elif a>b and b<a:
    print("big")
else:
    print("both are equal")'''


'''a=4
b=9
if a>b and b<a:
    print("small")
elif a<b and b>a:
    print("big")
else:
    print("both are equal")'''


'''a=4
b=4
if a>b and b<a:
    print("small")
elif a<b and b>a:
    print("big")
else:
    print("both are equal")'''

'''a=4
b=9
if a<b or b>a:
    print("small")
elif a<b or b<a:
    print("big")
else:
    print("both are equal")


a=4
b=9
if a>b or b<a:
    print("small")
elif a<b or b>a:
    print("big")
else:
    print("both are equal")'''

'''a=50
b=60
if not a<b:
    print("less")
elif not a>b:
    print("greater")
else:
    print("nothing")'''


'''a=50
b=60
if not a>b:
    print("less")
elif not a>b:
    print("greater")
else:
    print("nothing")'''

'''a=int(input("Enter a:"))
b=int(input("Enter b:"))
if a<b and b<a:
    print("true1")
elif a>b or a<b:
    print("true2")
else:
    print("nothing")'''

#if-elif-else-->using identity operators
#is,is not

'''a=5
if type(a) is int:
    print("it is int")
elif type(a) is not int:
    print("not int")'''


'''a=9.4
if type(a) is float:
    print("it is float")
elif type(a) is not float:
    print("not float")'''


'''a="Python"
if type(a) is str:
    print("it is str")
elif type(a) is not float:
    print("not str")'''

'''a=7+3j
if type(a) is complex:
    print("it is complex")
elif type(a) is not complex:
    print("not complex")'''


'''a=False
if type(a) is bool:
    print("it is bool")
elif type(a) is not bool:
    print("not bool")'''

'''a=int(input("Enter value:"))
if type(a) is complex:
    print("it is complex")
elif type(a) is not complex:
    print("not complex")'''


#if-elif-else-->using membership operators  (executes only one condition)

'''a=8,5,4,3,9,0
if 5 in a:
    print("true 5")
elif 3 in a:
    print("true 3")'''


'''a=8,7,6,5,4
n=int(input("Enter a:"))
if n in a:
    print("true")
else:
    print("false")'''
#---------------------------------------------------------

#multiple-if conditions-->it executes all the if conditions, if all if conditons are satisfied along with the else condition

'''a=10
b=20
if a<b:
    print("less")
if b>a:
    print("graeter")
if a!=b:
    print("not equal")'''


'''a=20
b=40
if a==b:
    print("a equal to b")
if b>a:
    print("greater")
if a!=b:
    print(" a not equal to b")'''

'''a=20
b=40
if a==b:
    print("a equal to b")
if b>a:
    print("greater")
if a>=b:
    print(" a not equal to b")
else:
    print("true")'''

#Logical operators-->and,or.not

'''a=12
b=45
if a<b and b>a:
    print("true1")
if a>b or b>a:
    print("true2")
if a!=b:
    print("true3")
else:
    print("yes")'''

#identity-->
#is,is not
'''a=19
b=8
if type(a) is int:
    print("true1")
if type(b) is int:
    print("true2")'''

'''a=19
b=8
c=4.6
if type(a) is int:
    print("true1")
if type(b) is int:
    print("true2")
if type(c) is float:
    print("true3")
else:
    print("End")'''

'''a=19
b=8.9
c="Python"
if type(a) is int:
    print("true1")
if type(b) is float:
    print("true2")
if type(c) is not str:
    print("true3")
else:
    print("End")'''

'''a=19
b=8.9
c="Python"
d=5+8j
e=True
if type(a) is int:
    print("true1")
if type(b) is float:
    print("true2")
if type(c) is not str:
    print("true3")
if type(d) is complex:
    print("true4")
if type(e) is not bool:
    print("true5")
else:
    print("End")'''

    
#membership--->
#in,not in
'''a=6,7,8,3,5,0
if 7 in a:
    print("true1")
if 0 in a:
    print("true2")'''


'''a=56,67,87,34,58,80
if 34 in a:
    print("true1")
if 0 in a:
    print("true2")
if 56 in a:
    print("true3")
else:
    print("Final")'''

n=3,9,44,6,22,7
a=int(input("Enter value:"))
if a in n:
    print("yes")
else:
    print("No")


#----------------------------------------------------
#nested-if-->if outer if condition is true then only it will go to inner if condition

'''a=4
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=4
b=9
if a>b:
    print("less")
    if b>a:
        print("greater")'''

'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("b equal to a")'''

'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("b equal to a")
    else:
        print("b not equal to a")
else:
    print("false")'''

        

'''a=13
b=15
if a==b:
    print("true")
    if b>a:
        print("greater")
else:
    print("false")'''

'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")
    else:
        print("false")
else:
    ("not true")'''

'''a=int(input("Enter a:"))
b=int(input("Enter b:"))
if a!=b:
    print("true")
    if a==b:
        print("equal")
    elif b>a:
        print("greater")
    else:
        print("false")
else:
    print("Program ends!")'''

    
    





    
