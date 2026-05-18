n=56789
res=0
def sum(num):
    temp=num%10
    num//=10
    num+=temp
    return num
while n>9:
    n=sum(n)
print(n)


s="Na3ya5b6"
l=0
r=len(s)-1
n=r
res=""
while r!=0 and l<n+1:
    if s[l].isdigit() and s[r].isdigit():
        res+=s[r]
        l+=1
        r-=1
    elif s[l].isdigit():
        res+=s[l]
        r-=1
    elif s[r].isdigit():
        res+=s[l]
        l+=1
    else:
        res+=s[l]
        l+=1
        r-=1
print(res)


s="silent"
l="listen"
length=len(s)
for i in range(length):
    for j in range(length):
        if s[i]==l[j]:
            s=s[:i]+'_'+s[i+1:]
            l=l[:j]+'_'+l[j+1:]
            break
print(s, l)
print(length*'_')
if s==l and l==(length*'_'):
    print("it is anagram")
else:
    print("it is not anagram")



n=[1,2,3,4,5,6,7,8]
mid=(len(n)//2)
# print(mid)
print(n[:mid]+n[:mid-1:-1])



s="111"
p=1
res=0
for i in s[::-1]:
    if i=="1":
        res+=p
    p*=2
print(res)


