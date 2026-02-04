##instagram -->if acc is private ---> both are the friends --> you can send the message
## if acc is public --> you send the message
## if acc is private --> both are not friends --> you can't send msg

acc_private=False
friends=False
allow_everyone=False
if friends:
    print("you can send the message")
else:
    if acc_private:
        print("you can send the message")
    else:
        if allow_everyone:
            print("send the message no need to follow")
        else:
            print("you can't send the message until the second person follows you")

##if purchase amount was below 500rs add the50rs deliver charge
##purchase amount should be calculated based on item price
##if distance is more than 3km add extra 10rs 

price= 150 #int(input("enter the item price:")) ##150
quantity=4 #int(input("enter the quantity:")) ##4
purchase=quantity*price
distance= 3 #int(input("enter the distance:")) ##3
if purchase>=500:
    print("no extra fee and delivery charges added and amount is:", purchase)
else:
    if distance<=3:
        print("only delivery 50rs added and the total is:", purchase+50)
    else:
        print(f"the total with all the charges is: {50+purchase+(10*(distance-3))}")

#too add the tab spaces for a select and tab to remove use shift tab
limit_available=100000
due_amount=0
# while True:
spending_amount= 50000#int(input("enter how much do you want to spend: "))   
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