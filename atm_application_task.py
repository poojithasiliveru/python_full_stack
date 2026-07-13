#ATM application

account=100000
card="c"
pwd=1234
while True:
    card_type=input("Insert the card:")
    if card_type=="c":
        print("Welcome Poojitha")    
        password=int(input("enter the Password:"))
        if pwd==password:
            opt=int(input('''Choose the option:
                            1.Balance enquiry
                            2.withdraw\n'''))
            if opt==1:
                print("your balance is",account)
        
            elif opt==2:
                w=int(input("withdraw some amount:"))
                r=account-w
                if w<100000:
                    print("Withdraw amount is",w)
                    print("Remaining Amount is",r)
                else:
                    print("Insufficient Balance")              
            else:
                print("Invalid Option")
        else:
            print("Incorrect password")
    else:
        print("Invalid card")
