#LIST COMPREHENSION

a=["codegnan","python","course"]
#o/p->['CODEGNAN','PYTHON','COURSE']

#print(a.upper()) #it will give error because upper is a string methon not list method

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=",")'''


'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''


#syntax
#a=[expression for var in collection/range]

'''a=[i.upper() for i in a]
print(a)'''

#---------------------------------------------
#tasks

'''a=["vij","hyd","viz"]
#o/p->['Vij','Hyd','Viz']

b=[i.capitalize() for i in a]
print(b)'''



'''a=[1,2,3,5,6,8,12,13]
#o/p->[1,4,9,25,36,64,144,169]

b=[i**i for i in a] #methon1 
b=[i**2 for i in a] #method2
b=[pow(i,2) for i in a] #method3
print(b)'''


#if-usage in list comprehension


'''a=[i for i in range(16)]
print(a)'''    #prints from 0 to 15

'''a=[i for i in range(16) if i%2==0]
print(a)   ''' #prints 0,2,4,6,8,10,12,14

'''a=[i for i in range(16) if i%2!=0]
print(a)'''    #prints 1,3,5,7,9,11,13,15



'''a=[i*i for i in range(21) if i%2==0]   #method1
a=[i**2 for i in range(21) if i%2==0]   #method2
a=[pow(i,2) for i in range(21) if i%2==0] #method2

print(a)''' #prints even num squares



'''
fru=["apple","banana","grapes","mango","kiwi","dragon","berry"]
b=[i for i in fru if "a" in i]     #using membership operator--> in
print(b)   #prints  "apple","banana","grapes","mango","dragon"]



fru=["apple","banana","grapes","mango","kiwi","dragon","berry"]
b=[i for i in fru if "a" not in i]     #using membership operator -->not in
print(b)    #prints  ["kiwi""berry"]'''


#no elif usage in list comprehension

#if-else usage
'''
a=[i*i if i%2==0 else i*5 for i in range(31)]
print(a) #if there are more than 1 condition uses the for loop after the conditions
'''


'''
a=[1,2,3,4,5]
b=[5,4,3,2,1]
#o/p->[6,6,6,6,6]

c=[a[i]+b[i] for i in range(len(a))] #method1
c=[a[i]+b[i] for i in range(5)]   #method2
print(c)
'''











