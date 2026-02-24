
import random
import math
from collections import Counter

print(pow(2,5)) # 2 Parameters or a list of values
a=[1,2,3]
print((a))
print(sum([1,23]))
print(sum(a))
print(max(a))
print(min(a))
print(math.factorial(3))
print(math.pi)
print(math.sqrt(144))
print(math.ceil(7.2))
print(math.floor(7.2))
print(math.trunc(7.2))
print(round(1234.56,2))
print(round(1234.56,1))
print(round(1234.56,0))
print(round(1234.56,-1))
print(round(1234.56,-2))


angle =math .pi/2 #we need give the values through where pi is 180 but when we give 90 it will take it as degrees
print(math.sin(angle))
print(math.fabs(-9)) #it gives the absolute value which remove - negative
print(math.log(5))   #it gives how much power of e will give the 5
print(pow(math.e, 1.6094379124341003)) 
print(math.log10(100)) #it gives how much power of 10 will give the 100


print (random. random())
print (random. randint(1, 10))# a range of integers
print (random. uniform (1,10))# a range of floats
print(random . choice( [ " apple" , "banana" , "grapes"]))
print(random .sample(["apple", "banana" ,"grapes"],2))


fruits =["apple" , "banana" , "grapes " ]
print(random . shuffle(["peaches " , "Tangerine" , "Orange" ]))
print(random.shuffle(fruits))
print(fruits)

#from coll library import counter module
# A count of all unique values that you have in an iterator
i=[1,2,3,5,6,5,1,2,2,3]
print (Counter(i))