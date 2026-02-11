
for x in range(2,5,2):
    print (x)

"""to print numbers from 10 to 40"""
for x in range(10,41):
    print (x)


"""#step value is considering +1 by default.
to print from 40 to 10 we need to use -1 as step value"""
for x in range(10,40-1):
    print (x)

"""#sum of all numbers from 1 to 10"""
sum=0
for x in range(1,11):
    sum+=x
    print(x)
print(sum)


""""##sum of squares of all numbers"""
squares=0
for x in range(1,11):
    squares+=x**2
    print(x)
print(squares)


##square of a limited numbers
starting_value=1 #int(input("enter the start value"))
ending_value=2 #int(input("enter the end value"))
for i in range(starting_value, ending_value+1):
    print(f"square of {i} is {i**2}")

str1="seven"
for char in range(len(str1)-1, -1, -1):
    print(str1[char])


#reverse a string and print

rev=""
for char in range(len(str1)-1, -1, -1):
    print (char)
    rev+=str1[char]
print (rev)

if(str1==rev) :
    print ("it is palindrome")
else:
    print ("it is not a palindrome")



set2={'hello' , 'hii', 2,5,6,7,10}
for x in set2:
    print (x)
#we can't access the values in the set through indexing
for x in range(len( set2)-1,-1,-1):
    # print(set2[x])
    print(x)

"""when we need to execute statements in a loop until condition becomes true,
when count of iteration is not known then we can go for while loop.
syntax:
while condition:
set of statements
then we can go for while loop.
this will executes the statement in a loop or infinite loop until condition becomes fail.
#with in the syntax of for loop we have where we start and where we stop.
#if in while loop--->starting and updating rules we need to write seperately.which are not part of the syntax
"""
str3="welcome"
while x<=len(str3)-1:
    print(str3[x])
    x+=1

rev=""
x=len(str3)-1
while x>=0:
    print(str3[x])
    rev+=str3[x]
    x-=1
print(rev)


nums=1254
while nums!=0:
    print(nums%10)
    nums=nums//10


"""
strong number
perfect no
perfect square
buzz number

"""