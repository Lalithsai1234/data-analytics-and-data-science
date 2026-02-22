"""
- Block of code that is reusable
Function Definition
Function Call
def solution():
    print("My solution")
solution()

Type-   Pre defined and User defined
parameter and arguments
parameter was defined when we create the function ex: def add(num1, num2):  // num1 and num2 are parameters
arguments are the values we are passing when we call function ex:add(5, 3) // 5 and 3 are arguments
 
two types of arguments 
1.positional arguments we  simply pass the values it stores according to the order add(2,5)
2.keyword argument we can pass bu using add(num1=5, num2=2)
3.arbitrary arguments we can pass n number of arguments but we use arbitrary parameter (*args)
4.keyword arguments we can pass the arguments like (name="sai", id=1) and stores like dict using (**kwargs) 

"""
            ##recursion
def fact(num, res=1):
    if num<=1:
        return res
    res*=num
    return fact(num-1, res)
f=fact(5)
print(f)
