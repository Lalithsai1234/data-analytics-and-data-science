"""
-----------------
Encapsulation
-----------------
Wrapping or binding the data and the behaviors into a
single unit(class).
Restricting the direct access
"""

class Bank:
    def __init__(self,name, pin, balance):
        self.name=name
        # self.pin=pin first it was public we can access it through b.pin
        self.__pin=pin
        self.__balance=balance
    #Getter
    def balance(self, pin): ##we call this getter because we only reading the private data (balance)
        if pin==self.__pin:
            print(self.name, self.__balance)
    #Setter
    def set_pin(self, pin, new_pin): ## we call this setter bcz we updating the private data (pin)
        if pin==self.__pin:
            self.__pin=new_pin
    #Getter
    def get_pin(self):
        print(self.__pin)
b=Bank("sai", 123, 654)
# print(b.pin) #it was printing the pin it should show the pin
b.balance(123)
b.set_pin(123,321)
b.get_pin()

"""
sai 654
321
"""

"""
-----------------
Access Modifiers
-----------------
1.public/default member --> self.variable   (anywhere)
2.protected member      --> self._variable  (within the class or sub class)
3.private member        --> self.__variable (only within the class)
"""

# 1.public/default member
class Parent:
    def __init__(self):
        self.name="Ramesh"
        print(self.name)
class child(Parent):
    def info(self):
        print(self.name)
p=Parent() #ramesh
c=child() #it will print ramesh two times bcz when we call sub class the main class also called itself
c.info() #ramesh
print(p.name) #ramesh
"""
Ramesh
Ramesh
Ramesh
Ramesh
"""
# 2.protected member 
class Parent:
    def __init__(self):
        self._balance=10000
    def show_money(self):
        print(self._balance)
class child(Parent):
    def info(self):
        print(self._balance)
Parent().show_money()
child().info()
# print(Parent().balance) it gives the error
print(Parent()._balance)#it was giving outside of the class when we write with one underscore when it was protected not private
"""
10000
10000
10000
"""
# 3.private member
class Parent():
    def __init__(self):
        self.__secret="secret"
    def show(self):
        print(self.__secret)
class child(Parent):
    def info(self):
        print(super().__secret) #even it was also not working
        print(self.__secret) #not this one too
Parent().show()
child().show() #we can get secret bcz we are using parent show fun so the secret was stored in parent show that's why we can see
# child().info() #it gives the error bcz it was private
"""
secret
secret
"""