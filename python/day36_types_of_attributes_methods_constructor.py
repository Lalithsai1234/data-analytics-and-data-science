"""
Types of attributes
class attributes -->without self in (class, self , instance)
instance attributes -->with self in class(self, instance)
local attributes or variable --without self and in function (in function)
"""
class student:
    clg='10k_clg' #it was class attribute
    def __init__(self, id, name, marks, ):
        self.name=name #these are the instance attribute which are unique for each object
        self.id=id
        self.marks=marks
        # self.clg=clg #here we are using same clg for both students so to reduce the redundancy i will make it a class attribute
    def show(self):
        print(student.clg)
        print(self.clg)
    def details(self, age):
        age=age
        print(age) #local can accessed  by this method only and we can't print with s1.age too
        # print(self.name, self.age)
#class and instance variable
s1=student(1, 'sai', 88)
print(s1.id, s1.name, s1.marks, s1.clg)
print('='*32)
s2=student(2, 'sai', 77)
print(s2.id, s2.name, s2.marks, student.clg)
print('='*32)
s1.show()
# student.name #we can't access the instance variable with the class name
print('='*32)
s1.details(22)
# print(s1.age)#it gives error bcz it does store with instance
print('='*32)


"""
types of methods
class method --> should be with @classmethod and instead self we use cls
instance method -->normal method with self with scope only within the instance can't change other instance
static method --> we don't self in the class but it gives error so we use decoreitor @staticmethod
"""
class student:
    clg_name="10k coders"
    def __init__(self, id, name, marks, ):
        self.id=id
        self.name=name
        self.marks=marks
    @classmethod #this is important only after this it will consider this as a class method
    def change_clg_name(cls, new_clg_name): #here we use cls bcz we are using the data in class level not in instance level
        cls.clg_name=new_clg_name
    def change_details(self, name, marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def greet():
        print("welcome to 10k coders")

s1=student(1, 'sai', 88)
print(s1.id, s1.name, s1.marks)
s1.clg_name='100kcoders' #it doesn't change the class variable it only changes for it
print(s1.clg_name)

print('='*32)
s2=student(2, 'sai', 77)
print(s2.id, s2.name, s2.marks)
print(s2.clg_name)

print('='*32)
#to change the class attribute we use with class method
s1.change_clg_name("100k_coders") #or student.change_clg_name is the correct way
print(s1.clg_name) #100kcoders it doesn't work bcz when we try to change the clg_name it creates a instance variable so cls var over ridded by instance var
print(s2.clg_name) #100k_coders here it will changing in the class level

print('='*32)
#we use instance which will have scope in instance level
s1.change_details('lalith', 66) #here we can't use it with student.change_details('lalith', 66)
print(s1.name, s1.marks) # lalith 66 here it was changing in same instance
print(s2.name, s2.marks) #sai 77 but can't change in the other instances

print('='*32)
#the static methods are helping methods
student.greet()
s1.greet()
s2.greet()

"""
types of constructor
default : __init__ we don't call it it called it self 
non-parameterized : greet(self) which doesn't take any arguments
parameterized : show (self, name) which take arguments
"""