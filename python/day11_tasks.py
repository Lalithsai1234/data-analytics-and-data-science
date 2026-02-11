
##build the logic to check the number is armstrong or not
num=153
num1=num
num2=num
count=0
res=0
while num1!=0:
    num1//=10
    count+=1
print(count)
while num!=0:
    res+=(num%10)**count
    num//=10
print(res)
print(f" it was {"a" if res==num2 else "not a"} armstrong number")