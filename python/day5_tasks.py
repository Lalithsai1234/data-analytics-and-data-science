            ##lists
list1= ["sai", "lalith", "ishwaq", "syam", "loki"]
print(f"the first element: {list[0]} \n the last element: {list[-1]}")
list1[2]="python_student"
del list1[1]
print(list1)


            ##tuples
tuple1=("telugu", "hindi", "english", "maths")
"""tuple1[0]="science"
Traceback (most recent call last):
  File "d:\10k coders\python\day5_tasks.py", line 8, in <module>
    tuple1[0]="science"
    ~~~~~~^^^
TypeError: 'tuple' object does not support item assignment"""
list2=list(tuple1)
list2.append("excel")
print(tuple(list2))


            ##sets
set1={1,2,3,4,1,3,8,9,"hello","Hello"}
print(set1)
set2=set1|{100}
print(set2)
set3=set1-{"Hello"}
print(set3)
print(list(set3))


            ##dictionary
student_details={"name":"sai", "age": 21, "skills":["python","java","html","css"]}
print(student_details)
student_details["role"]="data_scientist"
print(student_details)
student_details["age"]=20
# student_details.update(age=20)
print(student_details)
del student_details["role"]
print(student_details)
print(student_details["name"])
print(student_details.get("name"))


            ##Nested data access
students=[{"name":"lalith", "city":"jpt", "address":{"street":"depo", "pincode":"521175"}},
          {"name":"sai","city":"vjd","address":{"street":"1town", "pincode":"521745"}},
          {"name":"ishwaq","city":"hyd","address":{"street":"LBnagar", "pincode":"500001"}}]
print(f"the student {students[0]["name"]} lives in {students[0]["city"]}.")
print(students[0]["address"]["street"])
