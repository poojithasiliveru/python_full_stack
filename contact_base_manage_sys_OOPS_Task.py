'''
contact base management system
1.add contact
2.update contact
3.list of contacts
4.delete contact
5.exit

option1->name>poojitha,mobileno->23456,mailid->p@gmail.com
option3->to dispaly contact details
option2->old mobie to ->23456 new mobile->89765
option3->to display updated contact details
option4->name->poojitha,->it will remove entire contact information
option5->exit
'''



class contact():
    def __init__(self,name,mobile,mailid):
        self.name=name
        self.mobile=mobile
        self.mailid=mailid
    def display(self):
        print(f"Name:{self.name}")
        print(f"Mobile:{self.mobile}")
        print(f"Mailid:{self.mailid}")
        print("-"*30)

class contactmanager():
    def __init__(self):
        self.contacts=[]

    
    #adding the contat
    def add_contact(self):
        name=input("Enter Name:")
        mobile=input("Enter mobile number")
        mailid=input("Enter mailid:")

        con=contact(name,mobile,mailid)
        self.contacts.append(con)
        print("Contact added successfully...")

    #update the contact
    def update_contact(self):
        old_mobile=input("Enter old mobile number")
        for contact in self.contacts:
            if contact.mobile==old_mobile:
                new_mobile=input("Enter new mobile number:")
                contact.mobile=new_mobile
                print("Mobile number updated successfully")

        print("Contact not found")

    #List of contacts
    def list_contacts(self):
        if len(self.contacts)==0:
            print("No contacts available")
        else:
            print("List of Contacts")
            print("-"*30)
            for contact in self.contacts:
                contact.display()
                
    #Delete contact
    def delete_contact(self):
        name = input("Enter Name to Delete: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact Deleted Successfully!")
                return
        print("Contact Not Found!")
manager = contactmanager()

while True:
    print("\n===== Contact Base Management System =====")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. List of Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        manager.add_contact()

    elif choice == "2":
        manager.update_contact()

    elif choice == "3":
        manager.list_contacts()

    elif choice == "4":
        manager.delete_contact()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

















        
    
        
