x=10
print(x)
def add():
    # x=x+10 if give we can redefine the outer var
    # print(x) it doesn't work bcz we are redefined
    # y=x+10 #it will bcz we are just using the var
    # print(y) #it will work bcz we used it 
    # x+=10 
    # print(x) #even it doesn't work bcz we are changing the value
    global x
    x=x+10 #it will work we telling the it was global var so their can only be one
    print(x) #we can the access variable outside func but can't redefine 
add()

#another approach
def add():
    a= 10
    return a
x += add()
print(x)
"""
Deposit
Withdraw
Check balance
"""
def deposit():
    amount=int(input("enter the amount you want to deposit:"))
    if amount>0:
        print("your amount is credited")
        return amount
    else:
        print("enter the valid number")
        #if return nothing it will return when we try add the none to the int it gives the error so
        return 0
def draw():
    amount=int(input("enter the amount you want to withdraw:"))
    if 0<amount<=balance:
        print("your amount was withdraw was done")
        return amount
    else:
        print("enter the valid amount")
        return 0
def enquiry():
    print(f"your current balance is:{balance}")
print("welcome the 10k coders bank")
balance=10000
db_pin=1234
correct_pin=False
chances=3
for i in range(chances):
    a=int(input("enter your pin: "))
    if a==db_pin:
        correct_pin=True
        break
    else:
        chances-=1
        print(f"entered pin is wrong you have extra {chances} chances")
    
if correct_pin:
    while True:
        print("""select the option:
            to deposit enter 1
            to withdraw enter 2
            to check balance enter 3
            to exit enter 4""")
        option=int(input("enter your option number: "))
        # if option==1:
        #     balance+=deposit()
        # elif option==2:
        #     balance-=draw()
        # elif option==3:
        #     enquiry()
        # else:
        #     break
        match option:
            case 1: balance += deposit()
            case 2:balance-=deposit()
            case 3:enquiry()
            case 4:
                print("thank you welcome again..")
                break
            case _: print("invalid option")