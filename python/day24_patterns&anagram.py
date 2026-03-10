ip=['some', 'happy', 'olive', 'theatre', 'show', 'zomato']
#odd--reverse
#even--upper
op=[]
for char in ip:
    if len(char)%2==0:
        op.append(char.upper())
    else:
        rev=""
        for i in char:
            rev=i+rev
        op.append(rev)
print(op)


##anagram e- listen==silent
count=0
s1="sieent"
s2="listnn"
if len(s1)!=len(s2):
    print('Not anagram')
else:
    for i in s1:
        for j in s2:
            if i==j:
                s2=s2.replace(j,'*')                
                count+=1 
                break   
    if count==len(s2):
        print('ANAGRAM')
    else:
        print('NOT ANAGRAM')

# s-->c=1 
# i-->c=2
# l--->c=3
# e-->c=3
# n-->c=4
# t-->c=6
# str1='happy'
# str2='hello'
# banana=b a n

