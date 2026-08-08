#FILE HANDLING-->accessing the data

#write()
'''
a=open("pooji.txt","w")
a.write("codegnan")
a.close()
'''

'''
a=open("pooji.txt","w")
a.write("python full stack")
a.close()
'''


#append
'''
a=open("pooji.txt","a")
a.write("\nData Science")
a.close()
'''

#rutime input
'''
a=open("pooji.txt","w") #file_name,mode
a.write(input("Enter Data:"))
a.close()
'''

'''
a=open("pooji.txt","w")
b=input("Enter data:")
a.write(b)
a.close()
'''


#read()
'''
a=open("pooji.txt")
#print(a.read())         #it will display entire content
#print(a.readline())     #it will display first line
#print(a.readlines())    #it will display in list with \n for new line
#print(a.read(10))       #it will display number of character
'''

#writelines()-->it makes every objectc side by side

'''
a=open("tara.txt","w")
b=["poojitha","varshitha","tara","chaitra","maya","mihira"]
a.writelines("\n".join(b))
a.close()
'''

#open file with the file name
'''
a=open("sample.py")
print(a.read())
'''

#open file with the path
'''
a=open("C:\\Users\\poojitha\\Downloads\\python_full_stack\\variables1.py")
print(a.read())

'''
             














