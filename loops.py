#loops()-->for,while,range,break,continue,pass

#forloop()-->sequence iteration,one by one iteration

#list datatype
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)


a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")'''


'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

#tuple datatype
'''a=(5,6,7,8,9)
for i in a:
    print(i)
print(type(a))
print(type(i))'''

#set datatype
'''a={10,20,30,40,50}
for i in a:
    print(i)
print(type(a))
print(type(i))'''

#dict datatype
'''a={"year":2026,"month":"july","day":"thuresday"}
for i in a:
    print(i)'''


'''a={"year":2026,"month":"july","day":"thuresday"}
for i in a:
    print(i)
for i in a.keys():
    print(i)'''


'''a={"year":2026,"month":"july","day":"thuresday"}
for i in a:
    print(i)
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''

#float datatype
'''b=[5.6,8.9,4.5]
for i in b:
    print(i)
print(type(b))
print(type(i))'''


#str datatype
'''b=["python","java","c++"]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''

    
#complex datatype
'''c=[4+8j,3+7j,2+6j]
for i in c:
    print(i)
print(type(c))
print(type(i))'''


#bool datatype
'''d=[True,False]
for i in d:
    print(i)
print(type(d))
print(type(i))'''



#tasks
#o/p-->['APPLE','BANANA','MANGO']

'''fruits=["apple","banana","mango"]
b=[]
for i in fruits:
    b.append(i.upper())
print(b)'''



'''a=[1,3,5,7,9,"code"]
#o/p->[1,3,5,7,9,'c','o','d','e]
a.extend("code")
print(a)'''
#---------------------------------------------------------

#while loop-->continuous iteration until condition false

'''a=10
while a>1:
    print(a)'''

    
'''a=10
while a<1:
    print(a)'''


'''a=10
while a>1:
    print(a)
    a=a-1'''


'''a=10
while a>1:
    print(a)
    a+=1'''# it will go to infinite loop



'''a=1
while a<10:
    print(a)
    a+=1''' # it will print 1 to 9


'''a=20
while a>3:
    a-=1
    print(a)''' #print from 19 10 3


'''a=20
while a>3:
    a-=1
print(a)''' #print only 3 because after iteration we are printing last value


'''a=40
while a>5:
    a=a-1
print(a)'''


'''a=30
while a>1:
    print(a)
    a=a-1 '''   #print from 30 to 2


'''a=10
while a>2:
    print(a)
    a=a-1 '''  #print from 10 to 3



'''a=1
while a<25:
    print(a)
    a=a+1 '''  #print from 1to 24


#examples

'''while True:
    age=int(input("Enter age:"))
    if age>=18:
        print("eligible for vote:")
    else:
        print("not eligible for vote")'''


'''while True:
    year=int(input("Enter year:"))
    if year%4==0:
        print("leap year")
    else:
        print("not leap year")'''

#------------------------------------------------------

#Range()-->The range function returns a sequence of numbers,starting from 0 by default and increments by one by one and stops before a specified number.

#range(stop)--->range(9)--->prints--->0,1,2,3,4,5,6,7,8
#range(start,stop)-->range(1,5)-->prints  --> 1,2,3,4
#range(start,stop,step)--->range(2,11,2)-->prints --> 2,4,6,8,10


#start-stop-step

'''for i in range(20):
    print(i)'''  #prints from 0 to 19


'''for i in range(13,35):
    print(i)'''  #prints from 13 to 34



#o/p-->0,3,6,9,12,15,18,21,24,27
'''for i in range(0,30,3):
    print(i,end=" ")'''

#o/p-->5,10,15,20,25,30,35,40,45
'''for i in range(5,50,5):
    print(i,end=" ")'''

#o/p-->2,4,6,8,10,12,14,16,18
'''for i in range(2,20,2):
    print(i)'''



#Grades

#Method 1
'''while True:
    marks=int(input("Enter marks:"))
    if marks<=100 and marks>=90:
        print("Grade A")
    elif marks<=90 and marks>=80:
        print("Grade B")
    elif marks<=80 and marks>=70:
        print("Grade C")
    elif marks<=70 and marks>=50:
        print("Grade D")
    else:
        print("Fail")'''

#Method 2:
'''while True:
    marks=int(input("Enter marks:"))
    if marks in range(91,101):
        print("Grade A")
    elif marks in range(81,91):
        print("Grade B")
    elif marks in range(71,81):
        print("Grade C")
    elif marks in range(50,71):
        print("Grade D")
    else:
        print("Fail,study Well.....")'''

#-----------------------------------------

# difference among break, continue, pass

#Break->it is used to terminate the entire loop.
#contnue->it is used to skips the current iteration and rest of the code will continue.
#pass->it is a null statement it does nothing but syntatically we need.


#break
'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''


'''a=10
while a>1:
    a=a-1
    if a==6:
        break
    print(a)'''
    


'''for i in range(20):
    if i==13:
        break
    print(i)'''


'''a="python"
if a=="h":
   break
print(a)''' #error because to apply break we need for loop or while loop


'''a="python"
for i in a:
    if i=="h":
       break
    print(i)'''

#---------------------------------------------------------------------
#continue

'''a=20
while a>5:
    print(a)
    a=a-1'''


'''a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        continue'''  #it will not skip 10 because we written the print before the condition


'''a=20
while a>5:
    a=a-1
    if a==10:
        continue
    print(a) '''       #write the print after the condition the only it will skip



'''for i in range(15):
    if i==7:
        continue
    print(i)'''



'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''
#--------------------------------------------------

#pass

'''a=30
while a>10:
    print(a)
    a=a-1
    if a==20:
        pass'''


'''for i in range(40):
    if i==10:
        pass
    print(i)'''










