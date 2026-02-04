            ##operator
"""An operator is a symbol which tells python to perform the operator values .
1.ARITHMETIC OPERATOR:
+,-,*,/,//,%,**
2. ASSIGNMENT OPERATOR:
=,+=,-=,/=,*=,**=,//=,%=
3.comparision and relational operator
==,!=,<,>,<=,>=
4. logical operator
and, or, not
5. MEMBERSHIP operator
in, not in
--->returns boolen values. used to check presense of value in
string, list, tuple, dictionary .
6.identity Operator
is is not -- python uses same memory from a range of -5 to 256
to compare two values based on value and their memory address
7.Bitwise Operator
and --> &
or --> |
not --> ~  # ~ (not) it will inverts the given binary value by followint 2's complement, where python will understand and writes the formula like -(x+1)
xor --> ^ if both are diff it gives the 1
leftshift --> <<
rightshift --> >>

8.Ternary Operator

"""
            ##Arithmetic Operator
print (2+2) #4
print(2.5+3.6) #6.1
print((4+5j)+(3+8j)) #7+13j 
print("hello"+"world") #helloworld
#print(3+"hi") #unsupported operand- typeerror
print([1,2,3]+[4,5,6]) #[1,2,3,4,5,6]
print((1,2,3)+(4,5,6))#(1,2,3,4,5,6)
# print({1,4}+{2,6}) #unsupported
# print( {"name" :1}+ {"city": "hyd"}) #unsupported
print(True+12) #13
print(False+False) #0
print(True+True) #1
# print(None+None)#unsupported
# print(True+"helloworld") #unsupported
# print(True+None) #unsupported

##it works for the int , float and complex
# print("hello"-"world")#unsupported 
# print([1,2,3]-[4,5,6])#unsupported same goes for the sets, dicts and tuples


##works for the int and float 
print((2+3j)*2) #4+6j
print((2+5j)*(3+2j)) #-4+19j  #(a+b)(c+d)=(a*c)+(a*d)+(b*c)+(b*d)
# print("hello"*"hello") #unsupported
print("hello"*3) #"hellohellohello"
print([1,2,3]*2) #[1, 2, 3, 1, 2, 3] same for the tuple
print((1,2,3)*2) #(1, 2, 3, 1, 2, 3)
# print([1,2,3]*[1,2,3])#unsupported same for the tuple 
# print({1,2}*2)#unsupported same for the dict


#works for the int and float
print((4+5j)/2) #(2+2.5j)  
print((4+6j)/(4+8j)) #(0.8-0.1j)  #((a+bj)/(c+dj))*((c-dj)/(c-dj))
# print([1,2,3]/[1,2,3]) #unsupported  same goes for the tuple, set and dict
# print([1,2,3]/2)#unsupported same for all


print(10//3) #3
# print((4+6j)//(4+8j))  #unsupported same for dividing with 2
# print([1,2,3]//2) #unsupported
print(10%3) #1
print(3**3) #27
# print("hello"**3)#unsupported
# print([1,2,3]**2)#unsupported


            ##ASSIGNEMENT OPERATOR
# X+=5
# print(x) #not defined
strl=" hello "
strl+= "hi "
print(strl)
li=[1,2,3]
li+=[3,4]
print(li)

set1={1,2}
set1|={3}
print(set1)

            ##reational or comparision 
print([1,2,3]<=[1,4,6]) #comapring each value with every value in other list
print({1,2,3}<={1,2,3,6,10}) #it's comaparing does it a subset or not



            ##logical operator
print(True and "") #it gives the empty string
print(False and "") #it gives the false
print(True and 2) #it gives the 2 bcz if both are then it goes for the true value
print(3 and 2) #if both are then it goes to the 2nd value not first value
print(False and 5) #if the false it goes to the false 
print(5 and False) #false


            ##Membership Operator
student_name= 'omkar'
students=[ 'mineesh' , 'madhu' , 'omkar' , 'divya ' , 'mani']
print(student_name not in students)  #false
student_name1= 'omkar'
students1={ 'mineesh' , 'madhu' , 'omkar' , 'divya ' , 'mani'} 
print(student_name1 not in students1)  #false


dict1={"name" : "mineesh " , "city" : "hyd " , "age" : 20, " gender" : "male " }
print("minesh" in dict1) #false bcz it only sees key names
print( "name" in dict1) #true bcz it was in keys 


            ##Identity Operator
# #for the short int shares the same memory when the integer if from -5 to +256 only
## when we add above that it make a new memory so in identity we have is and is not which was based on the memory location of the variable
a=10000
b=10000
print(a is b)


                                                        #day7 starting
        ##Bitwise Operator
##to print bin value we have bin method  --works only for the integer
print(bin(10))  #0b1010 Ignore the 0b 
print(2&2) # answer was the 2
print(5&7) #answer was the 5

print(5|7) #answer was the 7

print(5^6) #answer is 3 if both are same it gives the 0 if both are diff it gives the 1


# ~ (not) it will just add the one and give the negative to the result
#where python will understand and writes the formula like |x|=-(x+1)

print(~10) #-(10+1) 11
print(~6)  #here -7 instead 5  bcz it will take the |x| = -(x+1)==> -(6+1)
print(~255) #256

#1eft shift--
print(10<<2)
#right shift
print(10>>2)


            #ternary Operator
x=5 if True else 6
print(x) #5

login=False
login_status="logged in" if login else "logged out"
print (login_status) #logged out



##finding the number was even and odd through the bitwise operator,arithmetic and membership
num=5
print("even" if num%2==0 else "odd") #odd
print("even" if num&1==0 else "odd") #odd  here whenever we have the rightmost digit is 1 it always be the even if not it was odd
print("even" if str(num)[-1] in "02468" else "odd") #odd here we are converting the num into str and taking the final value to find it in the sequence


