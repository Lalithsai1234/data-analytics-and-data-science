# s='a[3]b[2]c[1]'
# res=""
# for i in range(0,len(s),4):
#     res+= s[i]*int(s[i+2])
# print(res)

print(ord('0'),ord('9') )
s="ab[2],bc[2],d[1]"
s="a[10]b[1]"
# s='a[3]b[2]c[1]'

chr=""
res=""
dig=0
for i in s:
    if 97<=ord(i)<=122:
        chr+=i
    elif 48<=ord(i)<=57:
        dig=(dig*10)+int(i)
    elif i==']':
        res+=chr*dig
        chr=""
        dig=0
print(res)


s="fourthreeone"
dic={'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9 }
ch=""
res=0
for i in s:
    ch+=i
    if ch in dic:
        res= (res*10)+dic[ch]
        ch=""
print(res)
#431


#    *     
#   * *
#  * * *
# * * * *
n=5
for i in range(1,(n*2)+1, 2):
    print(((n*2-i-1))*" "+i*'* ')
for i in range(1,(n*2)+1, 2):
    print(((n-(i//2)-1))*" "+i*'*')
# for i in range(n*2-1,0, -2):
#     print(((n*2-i-1))*" "+i*'* ')

