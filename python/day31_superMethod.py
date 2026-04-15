class Parent():
    def eating(self):
        print("parent is eating")
class Child(Parent):
    def eating(self):
        super().eating() #parent is eating   child is eating
        print("child is eating")
c=Child()
c.eating()


class Parent:
    def __init__ (self, name) :
        self.name= name
class Child(Parent):
    def __init__ (self, name, age) :
        super().__init__ (name)
        self. age = age 
    def info(self):
        print(self.name)
        print(self.age)   
c=Child("Sai",21)
c.info()

class A():
    def method(self):
        print("A")
class B(A):
    def method(self):
        super().method()
        print("B")
class C(B):
    def method(self):
        super().method()
        print("c")
class D(C):
    def method(self):
        super().method()
        print("D")
d=D()
d.method()
"""
A
B
D
"""
class A1():
    def method(self):
        print("A1")
class A2():
    def method(self):
        print("A2")
class B(A1):
    def method(self):
        super().method()
        print("B")
class C(A2):
    def method(self):
        super().method()
        print("C")
class D(C,B):
    def method(self):
        super().method()
        print("D")
d=D()
d.method()
"""
A2
C
D
"""