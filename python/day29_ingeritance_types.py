"""
Single-level Inheritance
Multi-level Inheritance
Hierarchical Inheritance
Multiple Inheritance
Hybrid Inheritance
"""

# Single-level Inheritance
class father:
    pass
class son(father):
    pass

# Multi-level Inheritance
class grandfather:
    pass
class father(grandfather):
    pass
class son(father):
    pass

# Hierarchical -- Inheritance single parent multiple inheritance
class father:
    pass
class son(father):
    pass
class daughter(father):
    pass

# Multiple Inheritance -- multiple parents
class Father:
    x=10
    def eat(self):
        print("eating")
class Mother:
    y=5
    def sleep(self):
        print("sleeping")
class child(Father, Mother):
    print(Father.x, Mother.y)
    

c=child()
print(c.x)
print(c.y)
c.eat()
c.sleep()
#method resolution order --c3 linear algorithm
print(child.mro())
