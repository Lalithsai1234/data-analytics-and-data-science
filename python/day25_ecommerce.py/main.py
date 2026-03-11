from data import orders
from analysis import *

def menu():
    print("""
    choose 1 for total revenue
    choose 2 for most sold product
    choose 3 for top_customer
    choose 4 for cancelled orders
    choose 5 for product revenue
    """)
    choice=int(input("enter ur choice : "))
    if choice==1:
        total_revenue(orders)
    elif choice==2:
        most_sold_product(orders)
    elif choice==3:
        top_customer(orders)
    elif choice==4:
        Cancelled_orders(orders)
    elif choice==5:
        product_revenue(orders)
menu()