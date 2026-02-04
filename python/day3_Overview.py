# topics:
# ----------
# python installation
# vscode intro
# variables
# type conversions
# type(),input()





student_name_1= input("enter the name: ")  #lalith sai
student_rollno_1= int(input("enter the student roll number: ")) #501
print(student_name_1,": ",student_rollno_1 )
print(f"type of the Student_name: {type(student_name_1)}, and student_rollno_1 is always: {type(student_rollno_1)}")

students_names=list(map(str, input("enter the student names: ").split( )))  # sai lalith ish loki syam
students_rollnumbers= list(map(int,input("enter the name of the students names with spaces: ").split( ))) # 1 2 3 4 5 6
print(students_names, students_rollnumbers)


#type conversions
a=15.5     
print(type(a), a)  #implict type converson their is no data loss and it's automatic

b=15.21
print(int(b)) #explict have the data loss and it's not automatic




# x=25      --->b001(x) gives True
# x= 25     --->bool(x) gives True
# x=0       --->b001(x) gives False
# x="hi"    -->bool(x) gives True
# x ""      --->bool(x) gives False
# x " "     -->bool(x) gives True


x,y,z=2,3,4
print(x)
print(y)
print(z)


# ipl=
"""Lorem Ipsum is simply dummy text
of the printing and typesetting industry.
Lorem Ipsum has been the industry's
standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and sc
to make a type specimen book. It has survived not on
popularised in the 1960s with the
release of Letraset sheets containing
Lorem Ipsum passages, and more recently
with desktop publishing software like
\A1dus PageMaker including versions
of Lorem Ipsum"""

user_name="akhil"
role= "trainer"
location="hyd"

print(f"{user_name} is working as a {role} in {location}")


# type conversion is happening internally-->implicit type conversion
# python is dynamically typed language