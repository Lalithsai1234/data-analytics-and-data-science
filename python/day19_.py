"""
strings: group of characters enclosed in b/w "" or ''
to define multiline string---> """"""


"""

str1="something is fishy"
 #  -10.......-5-4-3-2-1

print(str1[3])
print(str1[5:15]) #starts at 5 and ends at 14
print(str1[:12]) #starts at 0 and ends at 11
print(str1[:]) #starts at 0 and ends at end of the string
print(str1[3:15:2]) #starts at 3 and ends at 14 by taking 2 steps at a time, skips every single character
print(str1[-10:-3]) #g is fi
print(str1[-3:-10:-1])#sif si 

print(str1[::-1]) #reverse the entire string -->yhsif si gnihtemos
print(str1[::-2])#reverse and skips 2 the entire string-->ysfs nheo
print(str1[::2]) #the string will start 0 and end the last but it skips the one element in middle

"""
operations on strings
+(concationation),*(repetetion)
"""
str1='hello'
# str2='world'
str2='3'
print(str1+str2) #hello3

str1='python'
x=3
# x='ok' it will gives the error because we can only use the number for multiple
print(str1*x) #pythonpythonpython

"""
removing space from the string
starting space(leading space) and ending space(trailing space) can be removed
to remove leading space-->lstrip()
to remove trailing space--->rstrip()
to remove both--->strip()

this method doesn't modify the existing string.
it will returns the new string by removing spaces
"""

username="harish  123   "
print(username)
print(len(username)) #14
x=username.strip() #it will strip the spaces in the corner
print(len(x)) #11


username1="###**harish***##  "
print(username1)
x=username1.strip('#')#it will only strip the specified element if it was in the corner
print(x) #"""**harish***##"""

username="harish  123   "
op=username.lstrip() #same like lstrip we have rstrip
print(username)


"""
finding substrings from the given string:
find()--->str.find(substring) or str.find(substring,start,end)
returns the index num of first occurance of substring, if not then returns -1

index()--->str.index(substring) or str.index(substring,start,end)
returns the index num of first occurance of substring, if not then returns valueerror


rfind()-->str.rfind(substring) or str.rfind(substring,start,end)
returns the index num of last occurance of substring by searching from right to left.
if not then returns -1

rindex()-->str.rindex(substring) or str.rindex(substring,start,end)
returns the index num of last occurance of substring by searching from right to left, 
if not then returns valueerror.
"""

str1="PYTHON IS EASY Easy"
op=str1.find('Eat')
print(op)

str1="AOKDNCDUECWDERTYSXCVESWDF"
op=str1.find('D',6,10)
print(op)



str1="PYTHON IS EASY Easy"

# op=str1.index('x')  it will gives the error because it was existed
# print(op)

op=str1.rfind('x') #it will return the -1 because their is no x and it searches from right to left
print(op)


# # op=str1.rindex('x') it will gives the error
# # print(op)


"""
counting substrings in given string
count()-->used to count the substrings from given string
str.count(substring)
    OR
str.count(substring,start,end)
"""

str1="PYTHON PYTHON JAVA JS PYTHON"
op=str1.count('ON',2) #3
print(op)

"""
splitting the string
to split the string into multiple partitions we can use split().
this will returns in the form of list.
splitting can be happened with help of seperator which should be avaialble in given string
by default it will consider space as a seperator if any space available in given string
first arg-->act as a seperator
second arg-->number of substrings to be splitted
"""

str1="DO*SOMETHING*GREAT*FROM*NOW" 
op=str1.split('*',3)#it will splits three time so the no of elements in list would be 4
print(op) #['DO', 'SOMETHING', 'GREAT', 'FROM*NOW']


"""
units-->1-100-->2rs/unit
units-->1-200--->1st 100-->2rs and >100-->3rs
units--->>200-->100x2+100x3+150x5
"""

units= 200 #int(input('enter the units : '))
if units<100:
    total_bill=units*2
    print(f"ur electricity bill is {total_bill}")
elif units<200:
    total_bill=(units-100)*3+100*2
    print(f"ur electricity bill is {total_bill}")
else:
    total_bill=(units-200)*5+100*3+100*2
    print(f"ur electricity bill is {total_bill}")



"""
upper()-->converts string to uppercase
lower()-->converts string to lowercase
isupper() --> to check the it was upper or not
islower() --> to check the it was lower or not
# """

str1="hello"
str2='do something great'
print(str1.upper())
print(str1.lower())
print(str1.isupper())
print(str1.islower())
print(str2.capitalize()) #only first letter in whole string will capitalize
print(str2.title()) #starting letter of each word will be capitalized
 
#replace(old_value, new_value, no of times the default was all)
x='hello everyone hello hello'
op=x.replace('hello','hi',1)
print(op) #hi everyone hello hello


str1='weLCOmE'
op=str1.swapcase()
print(op) #WElcoMe