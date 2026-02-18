def sample():
    print( 'hello')
    return 'something'
    print( 'welcome') #ignored
print (sample())

def sample1():
    return 'hello'
x=sample1()
print(x)

def sample2():
    return 'iam sample2'
x=sample2 #iam assigning function name/definition to x
print(x())

def sample3():
    print( 'hello sample3' )
    return 'byeee'
y=sample3
print(y())
print(y)

# we can assign a function to a variable
# a function definition can be take as values inside the datastructures like list/ tuple
# a function which can pass as a argument into another function, then that can be called as call back function
# a function which will take another function as a argument or returns another function then it can be called as higher order function
#beacuse of being a value

def func1():
    print( 'iam function 1')
def func2():
    print("iam function 2")
    return 'i am func 2'
list1=[func1,func2]
list1[0]()
list1[1]()


def fun3():
    print(" iam func 3")
    return func2()
fun3()
f=fun3()
print(f)


def fun4():
    return 'iam function 4'
def fun5(cbf):
    print(cbf())
    return 'iam function 5'
print(fun5(fun4))


# we can also define a function without name
# a function without name can be called as anonymous function
# to define anonymous function in python we have to use lambda keyword

def sample():
    return "hello"
print(sample())
#lambda function without params

fun2=lambda: 'hello'
print(fun2())

#lambda function with param
fun6=lambda x:x
print(fun6(3))

#lambda function with multiple params
fun4=lambda x,y: x+y
print (fun4(4,5))
fun5=lambda x, y=5: x+y
print(fun5(8,2))
print(fun5(8))

fun6=lambda *x: x[0]+x[1]+x[2]
print(fun6(1,2,3))

fun8=lambda *x: sum(x)
print(fun8(1,2,3))

fun7=lambda **x: x
print (fun7(second=5, third=6) )

"""                 ##recursive functions
a function being called by itself on a particular condition is called recursion process.
and that function can be called as recursive function
due to recursion--->more memory will be wasted because of more times of calling same function
so we went to loops instead of recursion
"""
def recu(n):
    if n>=0:
        print(n)
        return recu(n-1)
recu(10)

# def recursion(count):
#     count+=1
#     print(count)
#     return recursion(count)
# recursion(0)

#printing numbers from 10 to e
def recu(n):
    if n>=0:
        print(n)
        return recu(n-1)
recu(10)
#print numbers from 1 to 10
def rec1(n):
    if n<=10:
        print(n)
        return rec1(n+1)
rec1(0)



#sum of the n numbers using recursion.
#ip=5 op=15
#write a program to print n number of fibonocci series without recursion

#write a function to print multiplication table of given input
def table(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}") 
table(5)

#write a function to print numbers for given range
def numbers(start, end):
    for i in range(start, end+1):
        print(i)
numbers(20,30)

"""
task:
pratice all types of functions with syntax and examples on a paper and also execute them
level 2--->implement all the previous problems using functions
1. userdefined
2. predefine
"""