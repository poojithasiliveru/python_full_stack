#conditions
#if condition by using comparision operators
#<,>,<=,>=,!=,==

'''a=10
b=20
if a<b:
    print("true")'''

'''a=10
b=20
if a>b:
    print("true")''' #it will not display anything

'''a=5
b=7
if a<b:
    print("true")'''

'''a=5
b=7
if a>b:
    print("less") '''#it will not display anything


'''a=5
b=7
if a<=b:
    print("less")'''

'''a=5
b=7
if a>=b:
    print("less")'''#it will not display anything


'''a=5
b=7
if a!=b:
    print("true")'''

'''a=5
b=5
if a==b:
    print("match")'''

'''a=int(input("Eneter a:"))
b=int(input("Eneter b:"))
if a<b:
    print("true")'''

'''a="Python"
if a=="Python":
    print("true")'''

'''a="Java"
if a=="Python":
    print("match")'''   #it will not display anything

#if - condition by using logical operators
#and,or,not
'''a=3
b=7
if a<b and b>a:
    print("true")'''

'''a=4
b=7
if a<=b and b>=a:
    print("true")'''

'''a=3
b=7
if a!=b and a==b:
    print("true")'''

'''a=9
b=12
if a<b or b>a:
    print("true")'''

'''a=5
b=9
if a<=b or b>=a:
    print("true")'''

'''a=3
b=7
if a!=b and a==b:
    print("true")'''


'''a=4
b=9
if not a<b and b>a:
    print("true")'''

'''a=4
b=7
if not a<b or b>a:
    print("true")'''

'''a=3
b=7
if not a!=b and a==b:
    print("true")'''

#if - condition by using identify operator
#is,is not

'''a=9
if type(a) is int:
    print("true")'''

'''a=9
if type(a) is not  int:
    print("true")'''

'''a=9.8
if type(a) is float:
    print("true")'''

'''a=9.8
if type(a) is not float:
    print("true")'''

'''a="Codegnan"
if type(a) is str:
    print("true")'''

'''a="Codegnan"
if type(a) is not str:
    print("true")'''
    

'''a=8+7j
if type(a) is complex:
    print("true")'''
    
'''a=8+7j
if type(a) is not complex:
    print("true")'''

'''a=True
if type(a) is bool:
    print("true")'''


'''a=True
if type(a) is not bool:
    print("true")'''

'''a=False
if type(a) is bool:
    print("true")'''


'''a=False
if type(a) is not bool:
    print("true")'''

'''a=int(input("Enter a:"))
if type(a) is int:
      print("true")'''


#conditions by using membership operators
#in,not in

'''a=2,3,4,5,6,7
if 4 in a:
    print("true")'''

'''a=4,7,9,3,7,6
if 9 not in a:
    print("true")'''

#runtime input

'''a=int(input("Enter a:"))
if 30 in a:
    print("true")''' #it will throw error because we are only checking 30 in a ,it will contain other than 30 also

'''a=2,3,4,5,6,7,8,9
b=int(input("value:"))
if b in a:
    print("true")'''
#------------------------------------------------------

#if-else--> condition using comparision operators
#<,>,<=,>=,!=,==
'''a=10
b=20
if a<b:
    print("true")
else:
    print("false")'''

'''a=10
b=20
if a>b:
    print("true")
else:
    print("false")'''


'''a=10
b=20
if a<=b:
    print("true")
else:
    print("false")    

a=10
b=20
if a>=b:
    print("true")
else:
    print("false")'''

'''a=10
b=20
if a!=b:
    print("true")
else:
    print("false")
    
a=10
b=20
if a==b:
    print("true")
else:
    print("false")'''
#if-else-->by using logical operators
#and or not

'''a=20
b=40
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=20
b=40
if a>b and b<a:
    print("true")
else:
    print("false")'''

'''a=20
b=40
if a<b or b>a:
    print("true")
else:
    print("false")

a=20
b=40
if a>b or b<a:
    print("true")
else:
    print("false")'''

'''a=20
b=40
if not a<b:
    print("true")
else:
    print("false")

a=20
b=40
if not a>b:
    print("true")
else:
    print("false")'''


#if-else --> condition by using identity operators
#is,is not
'''a=13
if type(a) is int:
    print("true")
else:
    print("false")

a=13
if type(a) is not int:
    print("true")
else:
    print("false")'''

'''a=8.6
if type(a) is float:
    print("true")
else:
    print("false")

a=8.6
if type(a) is not float:
    print("true")
else:
    print("false")'''

'''a="Vijayawada"
if type(a) is str:
    print("true")
else:
    print("false")


a="Vijayawada"
if type(a) is not str:
    print("true")
else:
    print("false")'''

'''a=6+3j
if type(a) is complex:
    print("true")
else:
    print("false")


a=6+3j
if type(a) is not complex:
    print("true")
else:
    print("false")'''


'''a=True
if type(a) is bool:
    print("true")
else:
    print("false")

a=True
if type(a) is not bool:
    print("true")
else:
    print("false")'''

#if-else-->condition by using membership operator
#in,not in
'''a=1,2,8,4,9,6
if 4 in a:
    print("true")
else:
    print("false")

a=1,2,8,4,9,6
if 4 not in a:
    print("true")
else:
    print("false")'''

'''a=int(input("Enter a:"))
if 40 in a:
    print("true")
else:
    print("false")  '''       #it will throw error because we are only checking 40 in a ,it will contain other than 40 also


#run time input
'''a=5,8,4,3,9,6
n=int(input("Enter n:"))
if n in a:
    print("true")
else:
    print("false")'''


'''a=5,8,4,3,9,6
n=int(input("Enter n:"))
if n not in a:
    print("true")
else:
    print("false")'''


    
    


    







    
    

    
    





    
