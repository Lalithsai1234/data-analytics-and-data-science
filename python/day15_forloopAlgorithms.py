#sum of the n numbers using recursion.
#ip=5 op=15
def rec1(n, sum):
    if n<=10:
        sum+=n
        return rec1(n+1, sum)
    else:
        print(sum)
rec1(1,0)


#write a program to print n number of fibonoci series without recursion
n= 5 #int(input( 'enter num of: '))
a=0
b=1
if n<=0:
    print('enter positive')
elif n==1:
    print(a)
else:
    print(a)
    print(b)
    for x in range(3,n+1):
        c=a+b
        print(c)
        a=b
        b=c


def freq(str1):
    dict1={}
    for char in str1:
        if char in dict1:
            dict1[char]+=1
        else:
            dict1[char]=1
    print(dict1)
freq("hello world")


def count1(str1):
    checked=""
    for i in str1:
        count=0
        if i in checked:
            continue
        for j in str1:
            if i==j:
                count+=1
        print ("\t",i,"\t", count)
        checked+=i
count1('BANANA')

def compare(str2, str3):
    checked=""
    for i in str2:
        if i in checked:
            continue
        for j in str3:
            if i==j:
                print(i)
                break
        checked+=i
compare("pooja", "apoorva")

# tasks
""""
abc"-->it should print all
pairs of chars
op-->
ab
ac
bb
bc
ca
cb
cc
ip=['apple' , 'banana' , 'orange' 'mango' , 'grapes ' ]
op=[ elppa' , 'ananab' , 'egnaro' , 'ognam' , 'separg' ]
"""