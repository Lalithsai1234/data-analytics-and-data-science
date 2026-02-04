"""
CRUD= create, Read, Update, Delete
"""
 
l=[1,2,3,4,5] #Creating
print(l) #reading
l[1]="sai" #updating
del l[2]  #deleting the value rather using the pop and remove
print(l)
# l1=list(1,2,3,4) #it gives the error because list only take single argument
# ip=1ist([1,2,3,4]) #it was right


"""                 ##Tuples##          
immutable
to store the final data , we will use tuple
tuples executes faster than lists
tuples can accepts duplicates and heterogeneous data.
we can access the values from tuple using indexing because it will store values in ordered collection
"""

t=(1, "string", [1,2])  #Creating the tuple
print(t[0])             #reading the tuple
print(t)
t[2][1]="sai"           #updating the tuple only when the element is mutable
print(t)
t[2].pop(0)             #deleting the tuple only when the element is mutable
print(t)
del t[2][0]             #we can only delete the element from the list we can't delete the entire list like del t[2]
print(t)


"""                 ##Sets##    
sets are used to store the unique values as a unordered collection.
whenever we try to execute the set or print the set values, it always gives random order
only especially for string values.
in set every value has the hashing values. for numbers-->number itself be the hashing value.
but for string hashing value will be generates randomly

we can't access elements in the set with indexing. so, we cant add values with indexing
in sets like lists how we do.
we will use union approach for adding two sets
so for removing values from the set we can use - 
"""

set1={1,2,3, 'hello' ,4,3,2, 'hello', 'hi'} #creating was possible 
print(set1)
# print(set1[2]) #you can't access the value through index

# num1=1
# value1='hello'
# print(hash(num1)) #it will give the same value
# print(hash(value1)) #it will give a random number every time like 65184813213488964

new_set=set1|{108} # | it was the union symbol
print(new_set)
new_set1=set1-{4}  #it was the - symbol to remove element from a set
print(new_set1)




"""                 ##dictionary##
lists/ tuples/ sets are used to store like multiple persons, products, colors, books, students.
dictionary is used to store a full information of a particular person. , product, color, book, student.
dictionaries will store these information/data in the form of a key-value pair.
so, that key-value pair can be said to be as a property
should not allows duplicate keys
key always in the string format only
"""

Student_info={"name":"sai", "age":22, "gender":"male", "degree":"bTech","mobile":12345789, 501:"school", "name":"lalith"  } #we can pass the number as key but it was no use
print(Student_info[501])
print(Student_info.get("name"))  #here it does give a error it over rides it
Student_info["role"]="student"
del Student_info[501] #removes 501 property
print(Student_info)
Student_info.update(skills= ["pyhton", "sql", "html"]) #the update method updates if it is their and it will create if their is no key with that
print(Student_info)
print(f"i am {Student_info["name"]} and i am studying in {Student_info["degree"]}")
