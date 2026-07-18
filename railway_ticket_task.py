#Railway Ticket
#using functions

'''while True:
    def Ticket():
        ticket=1000
        gender=input("choose the gender:")
        age=int(input("Enter age:"))
        if gender=="male" : 
            if age>60:
                discount=(30/100)*ticket
                print("Ticket Price for male greater than 60:",discount)
            elif age<60:            
                print("Ticket Price for male less than 60:",ticket) 
        elif gender=="female":
            if age>60:
                discount=(50/100)*ticket
                print("Ticket Price for female greater than 60:",discount)
            elif age<60:
                discount=(30/100)*ticket
                print("Ticket Price for female less than 60:",discount)
    Ticket()'''



while True:
    def Ticket():
        ticket=1000      
        if gender=="male":
            if age>=60:
                discount=ticket-((30/100)*ticket)
                print("Ticket Price for male greater than 60:",discount)
            elif age<60:
                 print("Ticket Price for male less than 60:",ticket)
        elif gender=="female":
            if age>=60:
                discount=ticket-((50/100)*ticket)
                print("Ticket Price for female greater than 60:",discount)    
            elif age<60:
                discount=ticket-((30/100)*ticket)
                print("Ticket Price for female less than 60:",discount)       
    gender=input("choose the gender:")  
    age=int(input("Enter age:"))
    Ticket()











