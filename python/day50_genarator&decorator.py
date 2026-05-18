
"""
1) give lazy evaluation
2) it is memory efficient
3) it is used to represent infinite stream of data
"""


def gen():
    yield 1
    yield 2
    yield 3
g=gen()
print(next(g), end=" ") #1
print(next(g), end=" ") #2          
print(next(g), end=" ") #3
# print(next(g)) #StopIteration
print()

def gen(start, end):
    while start<=end:
        yield start
        start+=1
    else:
        raise StopIteration
g=gen(1,5)
print(next(g), end=" ") #1
print(next(g), end=" ") #2          
print(next(g), end=" ") #3
print(next(g), end=" ") #4
print(next(g), end=" ") #5
# print(next(g)) #StopIteration
print()


"""
Decorator:
decorator is a function which is used to modify the behaviour of another function without changing the code of original function
"""
print("="*32)
print("Decorator")
print("="*32)
 
def outer(func): #higher order function
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper
@outer
def greet(): #callback function
    print("hello")

greet()
#how it works
# x=outer(greet) #here it outer func returning the wrapper fun
# x()     #calling the wrapper function
print("="*5+"or"+"="*5)
