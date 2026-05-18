brac=input()
l_price=int(input()) #price of one '('
r_price=int(input()) #price of one ')'
l_count=0
r_count=0
for i in brac:
    if i=='(':
        l_count+=1
    elif i==')' and l_count>=1:
        l_count-=1
    elif i==')' and l_count<1:
        r_count+=1
sum=0
sum+=l_count*r_price
sum+=r_count*l_price
print(sum)


