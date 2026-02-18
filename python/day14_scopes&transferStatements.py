# local-->
    # variables which defined inside the function
    # will having local scope.
# enclosed-->
    # for suppose if we have a function inside a
    # function is a nested function.
    # if we declare a variable inside a outer function
    # then that variable will have enclosed scope.

z=5 #z is having global scope
def fun1():
    x=10 #x is having enclosed scope
    def fun2():
        y=10 ##y is having local scope
        print(x)

x=10
def func1():
    # print(x)
    x=15
func1()
print(x,"the global var prints")  #10 the global var prints
# 1. if i try to access x variable
# a. function first will check inside the function

def outer():
    x=10
    def inner():
        print(x)
outer()


def outer1():
    x=10
    def inner2():
        x=5
        print(x+2, 'from inner function' )#7 from inner function
    inner2()
    print(x*3, 'from outer function')#30 from outer function
outer1()


"""         scope modifiers:
these are the keywords which will change scope of the variable 
1. global--->change local to global
2. nonlocal-->it will change enclosed to local.
"""

#                  #global 
# to access local variable from outside
# to update global variable from inside of the function..
# global keyword will be useful
def func3():
    global x
    x='hello'
func3()
print(x)#hello

ipl='data'
def func4():
    global ipl
    ipl='science'
    print(ipl, 'from the fun')#science from the fun
func4()
print(ipl, 'out of the fun')#science out of the fun


                # non local
# to update outer function variable from inner function which is
# having enclosed scope we can use nonlocal scope-modifier
def outer2():
    x=125
    def inner2():
        nonlocal x #if we don't give it will print 5 and 125
        x=5 
        print(x) #5
    inner2()
    print(x) #5
outer2()


x=12
def func1():
    global x
    x=5         #here the x was updated in global
    print(x, 'from func1') #5 from func1
    def func2():
        x=6     #bcz it was local and not globalized it creates new x
        print (x, 'from func2')# 6 from func2
    func2()
func1()
print(x, "bcz it was global var")#5 bcz it was global var



"""                    #transfer statements
in python we have 3 transfer statements
1. break:
to stop the iterations completely/exits from the loop based on condition
2. continue:
to skip the specific iteration based on the condition
3. pass:
just act as a placeholder which do nothing.
we will use this for future development
we will just give name for the function and we can keep it on hold and implement in future.
to keep it in hold we need to use pass keyword
"""

#break will exits the loop whenever condition is satisfied
list1=['madhav', 'mani' , 'harish' ,'deepthi', 'aishwarya']
for name in list1:
    if name=='harish':
        print (name) #harish and after it breaks
        break

#the continue statement skips the iteration
for name in list1:
    if name=='harsih':
        continue
    print(name) #prints every name except harish

def fun2():
    pass


##          end statement
print("hello", end=" ")
print("world", end="\n") #default one was end="\n"


