#if we use a block multiple times--->block using 
#if we use a block multiple times with different inputs--->reusable block
#block means  set of tasks/ instructions.
#to reduce the length of the code

"""A function is a reusable block of code/ statements that performs specific task.
it helps organize code and avoid repetitions unnecessarily.
by default function will returns None if it is not returning anything specifically."""

"""
a function being called by itself on a particular condition is called recursion process.
and that function can be called as recursive function
1. default params
2. positional args
3. arbitrary args
4. keyword-arbitrary
5. keyword args
6. higher order
7. callback
8. anonymous using lambda
9. recursive function
"""





#static function: function which gives always same output without taking any inpu€
def Sample():
    print("hello iam sample function")
Sample()
Sample()
Sample()



#dynamic functions : functions which gives different outputs based on given inputs.
"""
while building dynamic functions, we should take inputs.
inputs should take in the form of parameters/ arguments while using function
eg: def sample(name, city): name and city--->parameters
        print(name, city)
    sample( 'kiran',' hyd ' )   kiran and hyd are arguments
    sample( 'harish', 'nlr')
count of parameters and arguments should be equal always
always positions of params and args should be match

in dynamic functions we have few types based on how we are passing arguments
1. positional arguments
2. default parameters--->whenever we have default values which should not be changed 
    inside the function then we can use these default parameters
"""

## note: Greetings("tharish", "inlr") it gives the error because their is no function to above it 
#it saves the function with name when we call it checks into functions table and run when we call it before it was stored it gives error

def Greetings (name, city) :
    print(f"{name} is from {city}" )
Greetings('kiran', 'guntur')
Greetings('hyd' , 'Akhil')



#default parameters
#here the default always should be last bcz here if we give x=20 
# first the we 4 will assign to x and gives error because of no argument for z
def function2(y,z,x=25): 
    print(x,y,z)
function2(4, 5)

def student(name, city, institute="10kcoders"):
    print(f"{name} is from {city} and joined in {institute}" )
student( 'lalith' , 'bnglr' )
student( 'kiran ' , 'gnt' )

def billing(item, price, quantity, gst=0.05):
    total_bill=price*quantity+gst*(price*quantity)
    print(f"total bill for {item} is {total_bill}" )
billing('dosa', 20, 3)
billing('poori', 30, 4)


"""
3. arbitrary arguments (*arg)-->
whenever we dont know the count of arguments to be pass then we should use this arbitrary arguments
all the arguments can be assign to single param in the tuple format
we should add * before the param name
"""
def students(*p):
    print(p)
students('hari' , 'krishna' , 'lalith', 'madhav')
students('harish')
students('kiran', 'akhil')

"""
4. keyword arbitrary arguments(**args)--->
whenever we dont the specific order of arguments to be follow, then we will pass arguments with variable names
then those arguments can be assign to single param in the form of a dictionary.
"""
def employees(**args):
    print(args)
employees(name="sai", age=11, city="jpt")#you can't give another name

def ramayana(first, second, third):
    print(f"first one is {first}, second one is {second}, third one is {third}" )
ramayana(third= "bharath" , first= 'ram' , second= "lakshman" )

def ramayana1(**brothers):
    print(f"first one is {brothers["first"]}, second one is {brothers["second"]}, third one is {brothers["third"]}" )
ramayana1(third= "bharath" , first= 'ram' , second= "lakshman" )


# #whenever we dont know count of args--->*params/args
# #whenever we dont know count/order--->**args/params


def demo():
    print( "hello")
    return 'function ends'
d1=demo()
print(d1)
# print (demo())