"""Write a program that takes these inputs
firstName
lastName
City
Age
Fav animal
fav number
Function-->Return initials

Function -->Return city code

function-->Check if age is eligible for voting or not

function--> Combine all inputs into a list
"""
f_name=input("enter the firstname: ")
l_name=input("enter the lastname: ")
city=input("enter your city name: ")
age=int(input("enter your age: "))
fav_animal=input("enter your fav animal: ")
fav_num=int(input("enter your fav number: "))

def initial(l_name):
    if len(l_name)<=1:
        return l_name
    for i in l_name:
        return i

def code(city):
    if len(city)<=3:
        return city
    res=""
    n=0
    for i in city:
        res+=i
        n+=1
        if n==3:
            return res

def eligible(age):
    return "eligible for voting" if age>=18 else "not eligible for voting"
def combine(f_name, l_name, age, city, fav_animal, fav_num):
    print(f"My name is {initial(l_name)}.{f_name}. \\\
          I am from {code(city)} and i am {eligible(age)}. \\\
          My favorite animal is {fav_animal} and number is {fav_num}.")

combine(f_name,l_name,age,city, fav_animal,fav_num)