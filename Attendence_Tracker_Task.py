#Attendence Tracker

n=int(input("Enter Total Students:"))
p=0
a=0
for i in range(1,n+1):
    stu=input(f"Student {i} present/absent:")
    if stu=="p":
        p+=1
    elif stu=="a":
        a+=1

print("............Attendence Report..........")
print("total students",n)
print("Total Presenties",p)
print("Total Absenties",a)
