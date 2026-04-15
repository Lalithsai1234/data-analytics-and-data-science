#14)
s="HeLLo" #hEllO
res=""
for i in s:
    if i.isupper():
        res+=i.lower()
    else:
        res+=i.upper()
print(res)
print(ord("a")-ord("A")) #32
print(ord("a"),ord("z")) #97, 122
print(ord("A"),ord("Z")) #65 90
##or
res=""
for i in s:
    if 97<=ord(i)<=122:
        res+=chr(ord(i)-32)
    elif 65<=ord(i)<=90:
        res+=chr(ord(i)+32)
    else:
        res+=i
print(res)

#15)
s="abc123d4"
res=""
for i in s:
    if i.isdigit():
        res+=i
print(res)

print(ord("0"), ord("9")) #48 57
res=""
for i in s:
    if 48<=ord(i)<=57:
        res+=i
print(res)


#15)
s="Abc123@#"
upper=""
lower=""
num=""
special=""
for i in s:
    if i.isalpha():
        if i.isupper():
            upper+=i+" "
        else:
            lower+=i+" "
    elif i.isnumeric():
        num+=i+" "
    else:
        special+=i+" "
print(upper)
print(lower)
print(num)
print(special)
upper=""
lower=""
num=""
special=""
for i in s:
    if 65<=ord(i)<=90:
        upper+=i+" "
    elif 97<=ord(i)<=122:
        lower+=i+" "
    elif 48<=ord(i)<=57:
        num+=i+" "
    else:
        special+=i+" "
print(upper)
print(lower)
print(num)
print(special)


s="aaabbbccccd"
res="" 
for i in s:
    if i not in res:
        res+=i
print(res)
res=s[0]
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        res+=s[i+1]
print(res)

#two pointers
res=s[0]
i=0
j=1
while j<len(s):
    if s[i]==s[j]:
        j+=1
    else:
        res+=s[j]
        i, j=j, j+1
print(res)