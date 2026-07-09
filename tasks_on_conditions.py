#if-else tasks
#voting
'''age=int(input("Enter age:"))
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")'''

#even or odd
'''num=int(input("Enter num:"))
if num%2==0:
    print("it is Even")
else:
    print("it is odd")'''

#leap year
'''year=int(input("Enter year:"))
if year%4==0:
    print("leap year")
else:
    print("not leap year")'''


#guest code
#to convert to upeer case
'''name=str(input("Enter name:").upper())
if name=="POOJITHA":
    print("welcome",name)
else:
    print("welcome guest")'''

#to convert to lower case
'''name=str(input("Enter name:").lower())
if name=="poojitha":
    print("welcome",name)
else:
    print("welcome guest")'''


#multiple names
'''names=["poojitha","varshitha","ram","sita","tara"]
a=input("Enter name:")
if a in names:
    print("welcome",a)
else:
    print("welcome quest")'''


#vowels
'''vowels=["a","e","i","o","u"]
a=input("Enter vowel:").lower()
if a in vowels:
    print("it is vowel")
else:
    print("it is consonent")'''

#---------------------------------------------------
#nested if tasks

#social media login
#method-1
'''username=input("Enter username:")
password=input("Enter password:")
if username=="poojitha":
    if password=="123":
        print("Login Successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")'''


#by using variables
'''a="poojitha"
b="123"
username=input("Enter username:")
password=input("Enter password:")
if username==a:
    if password==b:
        print("Login Successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")'''

#method-2
#by using if-else condition
'''username=input("Enter username:")
password=input("Enter password:")
if username=="poojitha" and password=="123":
        print("Login Successful")
else:
    print("Invalid credentials")'''


#----------------------------------------
#multiple if tasks
'''age=int(input("Enter age:"))
marks=int(input("Enter marks:"))
attendence=int(input("Enter attendence:"))
if age>=18:
    print("eligible for vote")
if marks>=80:
    print("eligible for scholership")
if attendence>=70:
    print("Allow to exams")'''


#-----------------------------------------
#if-elif-else taskes
#Bakery

'''cakeprice=int(input("Enter cake price:"))
if cakeprice==1200:
    print("redvelvet cake")
elif cakeprice==1000:
    print("almond cake")
elif cakeprice==800:
    print("chocolate cake")
elif cakeprice==600:
    print("butter scotch cake")
else:
    print("cake is not available")'''

#pizza
'''pizza=input("Enter pizza name:")
if pizza=="bbq_pizza":
    print(800)        #without codes also it will accept because it is a integer
elif pizza=="crispy_chicken":
    print("600")
elif pizza=="panner_pizza":
    print("400")
elif pizza=="corn_pizza":
    print("200")
elif pizza=="french_fries&coke":
    print("150")'''

















