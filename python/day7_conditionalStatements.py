"""1. as per the salary need to categorize the employee
1.salary is greater than equal to 1lkh-->senior level
2. salary is less than 1kh and e greater than 20k --> medium level
3. salary is less than 60k and greater than 25k--->beginner level"""

salary=10000
level_of_job="senior" if salary>=100000 else "medium" if salary>60000 else "beginner" if salary>25000 else "no job"
print(level_of_job)
print("senior" if salary>=100000 else "medium" if salary>60000 else "beginner" if salary>25000 else "no job")


                        ##conditional statements
"""
normal statements-->statements which executes without depending on any condition are said to be normal statements
conditional statements-->statements which executes based on condition/conditions are said to be conditional statements
1.simple if
2. if-else
3. if-elif-else
4. nested if 
"""

print("iam a normal statement1")
##making condition true directly
if True:
    print("iam a conditional statement1")
##decision is depends on expression(hardcoded)
if 2==2:
    print("iam a conditional statement2")
if " ":
    print("hello world")
print( "welcome everyone")
if not True:
    print("hello 1")
print("hello 2")

##if subscription is available then watch Ott otherwise please to subscribe
is_subscribed=False
if is_subscribed:
    print("watch Ott ")
else:
    print("please subscribe")

is_selected=True
is_rejected=False
on_hold=False

if is_selected:
    print("send the offer letter")
elif on_hold:
    print("wait for update")
elif is_rejected:
    print("you are not selected")
else:
    print("go and look for a job")

sql=True
excel=True
powerBi=True
python=True
if sql and excel and powerBi and python:
    print("become a data analyst")
elif sql:
    print("become a sql developer")
elif excel:
    print("become a excel developer")
elif python:
    print("become a python developer")
else:
    print("go and join the 10k coders")

"""if conditional:
    if condition T 1.1:
        print( " statement Tl " )
    else:
        print( " statementF1 " )
elif condition2:
    if condition T 2.1:
        print( " statementT2 " )
    else:
        print( " statementF2)
else:
    print ("default statement")"""
