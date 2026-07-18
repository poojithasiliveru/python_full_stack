#Variable length arguments-->variable length arguments are autimatically stores in tuple and we use "*" arguments

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=(2,3,4,5,6,7)
check(*b)
c={5,6,7,8,9}
check(*c)
d={"name":"poojitha","age":22,"place":"vij"}
check(*d)'''



'''def check1(*a):
    d=1
    print(a)
    print(type(a))
    for i in a:
        if type(i)in (int,float):         #we write like this also-> if type(i)== int or type(i)==float
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(1,3,4,5,1.3,4.3)
check1(4,3,6,2,3.4,2.3,"python")'''

#-------------------------------------
#(**kwargs)-->keyword  arguments-->it gives output in dict format

'''def check2(**a):
    print(a)
    print(type(a))
check2()
details={"names":["sweety","cuty","hearty"],
         "marks":[60,70,80],
         "satus":["p","a","p"]}
check2(**details)'''


'''
def check2(**a):
    print(a)
    print(type(a))
    for i in a:            
        print(i)            #print keys withoutmethod
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])         #print values withoutmethod
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])       #print keys,values withoutmethod
    for i in a.items():
        print(i)
check2()
details={"names":["sweety","cuty","hearty"],
         "marks":[60,70,80],
         "satus":["p","a","p"]}
check2(**details)
'''

#both (*) and (**) usage

'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("The key is:",i)
        print("The value are:",j)
final()
data=(2,3,4,5,6,2.3,4.5)
final(*data)
details={"year":[2024,2025,2025],"month":["june","july","aug"]}
final(**details)
final(*data,**details)'''


































