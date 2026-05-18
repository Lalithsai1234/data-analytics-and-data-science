class Employee():
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def display_details(self):
        print(self.name, self.salary)
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size=team_size
    def display_role(self):
        print("manager with a team of ",self.team_size)
class Engineer(Employee):
    def __init__(self, name, salary, specialization):
        super().__init__(name, salary)
        self.specialization=specialization
    def display_role(self):
        print("engineer with a specialization of ", self.specialization)
m=Manager("sai", 100000, 10)
m.display_details()
m.display_role()

e=Engineer("lalith", 50000, "pyhton")
e.display_details()
e.display_role()



class Payment():
    def process_payment(amount):
        print(f"your amount was processing {amount}")
class CreditCardPayment(Payment):
    def process_payment(self,amount):
        print(f"your credit card payment was under process with  {amount}")
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"your upi payment was under process with {amount}")
class NetBankingPayment(Payment):
    def process_payment(self, amount):
        print(f"your net banking payment was under process with {amount}")

def make_payment(payment_method, money):
    payment_method().process_payment(money)

make_payment(CreditCardPayment, 5000)
make_payment(UPIPayment, 4000)
make_payment(NetBankingPayment, 5000)



class BankAccount():
    def __init__(self, acc_num, balance):
        self.__account_number=acc_num
        self.__balance=balance
    def deposit(self, amount):
        if amount>0:
            self.__balance+=amount
            print(f"your {amount} is credited")
    def withdraw(self, amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"your {amount} is withdrawn")
    def get_balance(self):
        print("your balance is",self.__balance)
b=BankAccount(123, 5000)
b.deposit(100)
b.get_balance()
b.withdraw(500)
b.get_balance()

from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    # def __init__(self,hourly_wage):
    #     self.hourly_wage=hourly_wage
    def calculate_salary(self,hourly_wage):
        print(f"your salary per month is {(hourly_wage*8)*31} as Full time employee")
class PartTimeEmployee(Employee):
    # def __init__(self,hourly_wage):
    #     self.hourly_wage=hourly_wage
    def calculate_salary(self,hourly_wage):
        print(f"your salary per month is {(hourly_wage*4)*31} as part time employee")
FullTimeEmployee().calculate_salary(1000)
PartTimeEmployee().calculate_salary(500)



class Vehicle(ABC):
    def __init__(self,brand):
        self.__brand=brand
    @abstractmethod
    def start(self):
        pass
    def brand_name(self):
        print("the brand is", self.__brand)
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")
    def find_brand(self):
        super().brand_name()
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self start button")
    def find_brand(self):
        super().brand_name()
c=Car("ford")
c.start()
c.find_brand()
b=Bike("bmw")
b.start()
b.find_brand()


n=3
l='('
r=')'
res=[]
temp=""
def reoccur(temp, n,m): 
    if n==0:
        res.append(temp)
        return
    if temp.count('(')>=m:
        temp+=r*(temp.count('(')-temp.count(')'))
        reoccur(temp, n-1, m)
        return
    else:
        reoccur(temp+l,n-1,m)
    if temp.count('(')>temp.count(')'):
        reoccur(temp+r,n-1,m)
reoccur(temp, n*2,n)
print(res)