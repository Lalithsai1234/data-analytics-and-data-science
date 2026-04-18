class Bank:
    def __init__(self):
        self.__pin=1234 #it stores as self._Bank__pin -->Name mangling
    def get_pin(self):
        print(self.__pin)
    def show(self):
        print(self.__dict__) #bcz it gives output in dict format we can also get values by key which was variable name
b=Bank()
b.__pin=1111 #it will stores the value in class like self.__pin not as _Bank__pin ,and it was also not private
print(b.__pin) # 1111 we accessing the new variable not the private variable with 1234
b.get_pin() #1234
print(b._Bank__pin) # 1234 we can acquire private data by _classname__varname
b.show()
"""
1111
1234
1234
{'_Bank__pin': 1234, '__pin': 1111}
""" 
class parent:
    def __init__(self):
        self.__pin=9999
class child(parent):
    def __init__(self):
        super().__init__()
        self.__pin=999
    def show(self):
        print(self._parent__pin)
        # print(super().__pin) #it can't print
        print(self.__pin)
c=child()
c.show()
"""
9999
999
"""

"""
-----------------------------
Access Modifiers for methods
-----------------------------
"""
#Public Method
class Parent():
    def public_method(self):
        print("parent public method")
class Child(Parent):
    def parent_method(self):
        super().public_method()
Parent().public_method()
Child().parent_method()
"""
parent public method
parent public method
"""

#Protected Method
class Parent():
    def _protected_method(self):
        print("parent protected method")
class Child(Parent):
    def parent_method(self):
        super()._protected_method()
Parent()._protected_method() # parent protected methodyou can the method but it was not good practice
Child().parent_method()
"""
parent protected method
parent protected method
"""

#Private Method
class Parent():
    def __private_method(self):
        print("parent private method")
    def show(self):
        self.__private_method()
class Child(Parent):
    def parent_method(self):
        super().__private_method() #it gives the attribute error
    def calling_parent_method(self):
        super().show()
    def call_with_nameMangling(self):
        self._Parent__private_method()
# Parent().__private_method() #it gives attribute error
# Child().parent_method() #it gives error we can't access the private method not in sub class
c=Child()
c.calling_parent_method() # parent private method it gives the private method
c.show() #parent private method these was also works bcz if the method is not their it goes to the parent so parent can access it will gives output
c.call_with_nameMangling()  #parent private method it gives we are using name mangling
"""
parent private method
parent private method
parent private method
"""

s="aabbaaccd"
freq={}
for i in s:
    # freq[i]=freq.get(i,0)+1
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
print(freq)
# {'a': 4, 'b': 2, 'c': 2, 'd': 1}
res=""
for i,j in freq.items():
    res+=i+str(j)
print(res)
# a4b2c2d1