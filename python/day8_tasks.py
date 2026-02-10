limit_available=0 #100000 change it any number when you want to run this block of code
due_amount=0
while limit_available>0: # i stopped by changing the limit_available to zero
    spending_amount= int(input("enter how much do you want to spend: "))   #30000
    if limit_available>=spending_amount:
        limit_available-=spending_amount
        due_amount+=spending_amount
        print(f"take the amount: {spending_amount} and you can still use {limit_available}")
        print("your due amount is : ", due_amount )
    else:
        if due_amount>spending_amount:
            print("clear the due amount")
        else:
            print("exceed the limit of the card")


due=0
limit=int(input("enter the limit: "))
while True:
    print("""choose 1 for spending card,
    choose 2 for paying the bill,""")
    choice=int(input("enter choice: "))
    if choice== 1:
        spending_amount=int(input("enter the amount to be spend: "))
        if spending_amount<=limit:
            limit-=spending_amount
            due+=spending_amount
            print(f"after spending of {spending_amount} rupees and the limit is {limit} and due amount is {due}")
        else:
            print( "insufficient limit ")
    elif choice==2:
        payable_amount=int(input("enter the amount to be pay: "))
        if payable_amount<=due:
            due-=payable_amount
            limit+=payable_amount
            print(f"after payment of {payable_amount} rupees, updated limit is {limit} and due is {due}" )
        else:
            print("no dues for now, go and use ur card first")