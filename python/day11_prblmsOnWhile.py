
##how to print the count of the number 
count=0
num=12345
while num!=0:
    num//=10
    count+=1
print(count)


## add the sum of the digits in the integer
num=123456789
sum=0
while num!=0:
    sum+=(num%10)
    num//=10
print(sum)


## adding the squares of the each digit
num=123
sum=0
while num!=0:
    sum+=(num%10)**2
    num//=10
print(sum)


##strong number ---> sum of factorial of each digits is equal to the number 
fact=1
num=5
while num>0:
    fact*=num
    num-=1
print(fact)



# #125 -->1fact+2fact+5fact--123
str_num=145
copy_num=str_num
res=0
while str_num!=0:
    fact=1
    x=str_num%10
    while x>=1:
        fact*=x
        x-=1
    res+=fact
    str_num//=10

print(res)
print(f"{res} is the strong number is {res==copy_num} aligation")



##palindrome number 

## 3, 5 = 3x10+5=35
##35, 2 =35x10+2=352

## rev= (rev=0) 0x10+3
## rev= (rev=3) 3x10+5

num=-121
##instead of checking for every interation you can change the number to +ve
## if num<0:
##    num*=-1
num1=num
rev=0
while num!=0:
    ld=num%10
    if num>0:
        rev=(rev*10)+ld #instead giving the ld we can directly write it
    else:
        rev=(rev*10)-ld 
    num//=10
print(rev)
if rev==num1:
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")



#n,d=divmod(n,10)