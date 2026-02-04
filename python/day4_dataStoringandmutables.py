
##  Primitive data types -- int, float, complex, boolean, String   --  stored in Stack Memory
x=5
print(id(x))        # here the int is immutable but we are reassigning the value which changes the location of the value in memory 
x=10                # that's why it was immutable to change the value in the same location
print(id(x))        #the id of the x object was changed    (these was immutable at the same place)


##  Non Primitive data types -- list, tuple, set, dict, functions, regex, None, datetime   -- stored in heap Memory
users=["lalith", "sai"]
print(id(users))
users.append("ishwaq") #these are mutable at the same place
print(id(users))


"""   Primitive data types
    1.int--->it is a pure numeric data which have whole numbers only.
    eg:user mobile, user age,pincode,quantity(count),
    2. float--->it is also a pure numeric value which contains decimal values
    eg : quantity(weights) , ratings, price.
    3. str-->group of characters which enclosed in b/w '', "", """""".
    eg: username, usergender, userpassword, labels, citynames, productnames ...
    4. bool--->which contains truth values true/ false.
   eg:while checking conditions., is available?, is active....like questioning.   
"""

students=["umamahesh", "harish", "deva", "divya", "neelima", "srinivas","neelima"]
print(len(students))
print (students[-4])
print(students[len( students)-4])

##update
students[2]="deva raj"
print(students) #updating with positive indexing.

##append
students.append("sai")
print(students)

""" methodname(list_variable name)
    here we are passing entire list as a input
    list_variable_name . method ( )
    here we are passing a new values as a inputs to be apply for the list"""

##remove
students.remove("neelima") #removes the first match only
print(students)

##extend
students.extend(["lalith", "ishwaq"]) #we can add more elements that should be pass as a list.
print(students)

##using pop method
students.pop() #this will removes last element by default.
print(students)
students.pop(5)#this will removes the indexed(+ve or -ve) value
print(students)

##extend with input
movies=[]
movies.extend(input("enter the names with the ,").split(","))
print(movies)