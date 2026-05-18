"""
1) Higher Order Function
2) Callback FUnction
3) lambda Function
4) Closure
"""
# 1) Higher Order Function
#function take another function as an argument
def greet(name) :  ## call back function where send as a argument to other function
    print( 'Hello' , name)
def show(func): ## higher order function
    func("ramesh")
show(greet)

#function return another function
def inner ():
    print("it is the inner")
def outer():
    return inner
x=outer()
x() #inner()


##lambda function :called as anonyms function most used for simple tasks
# Syntax: lambda (parameter or argument): expression
add=lambda x,y: x+y
print(add(1,1)) #2

even_or_odd=lambda x: "even" if x%2==0 else "odd"
print(even_or_odd(5)) #odd


#closure
def outer():
    x=10
    def inner():
        print(x)
    return inner
x=outer()
x()#10

def prime(num):
    n=num//2
    count=2
    for i in range(2,n+1):
        if num%i==0:
            count+=1
    return count
lst=[5, 9,8, 16, 10]
res=[]
for i in lst:
    x=prime(i)
    if prime(x)==2:
        res.append(i)
print(res)