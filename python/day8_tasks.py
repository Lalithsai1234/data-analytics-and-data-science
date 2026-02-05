limit_available=100000
due_amount=0
while True:
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