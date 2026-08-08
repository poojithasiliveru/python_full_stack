#yvic gqpk ivok pxdb

#Email Automation
import random
import math
import smtplib  #simple mail transfer library

digits="0123456789"
OTP=""    #empty string
for i in range(5):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is your OTP"
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()       #for encryption
s.login("poojithasiliveru2003@gmail.com","yvic gqpk ivok pxdb")
user="poojithasiliveru2003@gmail.com"
mailid=input("Enter the mail which you want to send:")
s.sendmail(user,mailid,msg)

while True:
    a=input("Enter the otp:")
    if a==OTP:
        print("OTP is correct")
    else:
        print("OTP is incorrect")
