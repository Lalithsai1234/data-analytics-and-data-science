from abc import ABC, abstractmethod

#Abstract class-- must contain atleast one abstract method if we stop creating the object for it 

#Concrete Method-->those which have a body or one instruction
#Abstract Method-->those which have the @abstractmethod decorator and don't have the body

class Teacher(ABC):
    @abstractmethod
    def teach(self):
        pass
    def take_Attendance(self):
        print("teacher is taking the attendance")
class Physics_teacher(Teacher):
    def teach(self):
        print("physics teacher is taking the attendance")
    def take_Attendance(self):
        print("phy teacher taking the attendance")
class Biology_teacher(Teacher):
    def teach(self):
        pass
    def take_Attendance(self):
        print("biology teacher is taking the attendance")
class Sql_teacher(Teacher):
    def take_Attendance(self):
        print("sql teacher is taking the attendance")
p=Physics_teacher()
p.teach()
p.take_Attendance()
print("="*22)

b=Biology_teacher()
b.teach()
b.take_Attendance()
print("="*22)

# s=Sql_teacher() #you can't create the object if the abstract method was not override
# Sql_teacher().take_Attendance() #we can't use other methods tpp

# t=Teacher() # you can't create the object for the abstract class