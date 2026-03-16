"""
1. procedural programming- ->pop
    characterstics :
    variables
    functions with sequential order programming
2. functional programming- ->fop
    charcterstics:
    pure functions
    immutable
3. object oriented programming-->oop
    for easy maitanance of large scale applications, we prefer to use oops.
    oops is a paradigm/ system/ approach of implementing a software system with well organized code.
    these paradigm can be prefer while building real time entities(objects).
Note: in
fop/pop-->variables and functions can be in implemented separately
oop-->both can be implemented together same place i.e.. class
4. logical based programming
5. event driven programming


1.oops are totally works with objects.
2.objects can be create with reference of class.
3.objects can contains-->properties and behaviour
4.to store properties we will use attributes
5.to add behaviour we will use/ implement methods
"""                                                

"""
to store properties we will use attributes or variables.
1. class variable-->
    this will contains constant values within the class and outside of methods.
2. instance variable-->
    contains values with instance of objects these will be implemented inside of methods in classes.
"""

class HumanBeing():
    from_place= 'brahmalokam'
    to_place= 'bhoolokam'
    def __init__ (self, name, age) :
        self.name=name
        self. age=age
obj1=HumanBeing( 'lalith' , '300' )
obj2=HumanBeing( 'krishna' , '300' )
obj3=HumanBeing( 'lalith' , '300' )

print (obj1. from_place, obj1 . name, obj1. age, obj2. to_place)
print (obj2. from_place, obj2 . name, obj2. age, obj2. to_place)
print(obj1.from_place is obj2.from_place)
print(obj1.age is obj3.age)
"""
self keyword refers to the object which we are going to create
I.obj1 is a object going to create with properties of name, gender
2. x and y are parameters which contains values that to be assigned to the properties of objects which we
are going to create.
3. __init__ is a method/ constructor which helps to constructs the objects.
4. __init__ will executes by default whenever we are creating objects, no need to call that method specially.
"""

class Student:
    institue= "10000 coders"
    def __init__(self, name, batch):
        self.name=name
        self.batch=batch

s3=Student('lalith', 'd9' )
s4=Student('madhav', 'd9')
print(s3.name)
print(s4.name)



class bankAccount:
    bank_name="bob"
    def __init__(self,x,y):
        self.holder_name=x
        self.acc_number=y
    def __str__(self):
        return f"{self.holder_name} and his acc no is {self.acc_number}"
print(bankAccount("sai", 741852963))
obj1=bankAccount("sai", 741852963)
print(obj1, obj1.bank_name)



"""
create ipl class with the team name with player info
create multiple player objects with reference of ipl class
"""