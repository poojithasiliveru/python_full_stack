#ERROR HANDLING

#Syntax error->during complilation it will occure (compile error)
#run_time_error->during execution time it will happens
#logical_error->error in logic(it can't be visible)

#Syntsx error
'''
for i in range(10):
print(i)       #indentation error

'''

#run_time error
'''
a=int(input())
b=int(input())
print(a//b)   #(20//0)->ZeroDivisionError
'''

#logical error
'''
a=10
b=20
print(b-a)  #it is logically incorrect we can't substract 20 from 10.

'''

'''
a=10
b=20
if a>b:
    print("less") #it is a logical error because 10 not greater than 20(the error cannot be visibile)
    
'''
