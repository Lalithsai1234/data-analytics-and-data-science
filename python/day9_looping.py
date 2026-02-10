# "tankl" , "tank2" , "tank3" , "tank4"]
# for x in list:
# print (f "filling the water in {x}" )

students= [ "pooja" , " harigopal" , "aishwarya" , "sohail" , "dhakshayani" , "umamahesh" ]
count=0
for student in students:
    print(f"{student} index is {count}")
    count+=1
 
nums=[1,2,3,4,5,6,7,8,9,10]
for num in nums:
    print(f"2 x {num}= {num*2}")


student_info=[
{"name" : "pooja" ,"rollno": 501},
{"name" : "harigopal", "rollno" : 502},
{"name" : "aishwarya" , "rollno" : 503}
]
for student in student_info:
    print (student["name"],"and reg no: ", student["rollno"])


students = [
    {"id": 101, "name": "Aarav", "marks": 98},
    {"id": 102, "name": "Ishani", "marks": 95},
    {"id": 103, "name": "Aditya", "marks": 92},
    {"id": 104, "name": "Priya", "marks": 78},
    {"id": 105, "name": "Rohan", "marks": 72},
    {"id": 106, "name": "Ananya", "marks": 65},
    {"id": 107, "name": "Vikram", "marks": 48},
    {"id": 108, "name": "Siddharth", "marks": 42},
    {"id": 109, "name": "Meera", "marks": 38},
    {"id": 110, "name": "Arjun", "marks": 45}
]
for student in students:
    if student["marks"]>=90:
        student["status"]="topper"
    elif student["marks"]>=60:
        student["status"]="medium level"
    else: 
        student["status"]="low level"




#i want to iterate or perform some task based on my requirement then i can use range
# for x in range(start,end,step):
#print numbers from I to IO by skipping every 3 values

for x in range(1, 10):
    print(x, end="")

for x in range(1, 10, 3):
    print(x)

num=5
for x in range(1,11):
    print(f"{num} x {x} = {num*x}")


