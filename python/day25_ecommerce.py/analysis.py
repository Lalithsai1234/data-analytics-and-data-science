def total_revenue(data):
   
    total_revenue=0
    for order in data:
        if order["status"]=='Delivered':
            total_revenue+=order['price']*order['quantity']
    print(total_revenue)

def most_sold_product(data):
    print('most sold product')
    products={}
    for order in data:
        if order['status']=='Delivered':
            if order['product'] in products:
                products[order['product']]+=order['quantity']
            else:
                products[order['product']]=order['quantity']
    print(products)
    most_sold=max(products,key=products.get) 
    print(most_sold)


def top_customer(data):
    customers={}
    for order in data:
        if order['status']=='Delivered':
            customers[order['customer']]=customers.get(order['customer'],0)+(order['quantity']*order['price'])
    print(customers)
    top_customer=max(customers,key=customers.get) 
    print(top_customer)            

def Cancelled_orders(data):
    for order in data:
        if order['status']=='Cancelled':
            print(order)
def product_revenue(data):
    products={}
    for order in data:
        if order['status']=='Delivered':
            if order['product'] in products:
                products[order['product']]+=order['quantity']*order['price']
            else:
                products[order['product']]=order['quantity']*order['price']
    print(products)
    most_product_revenue=max(products,key=products.get) 
    print(most_product_revenue)