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

def repeat(str1):
    for i in str1:
        for j in str1:
            print(i,j)
repeat("abc")

def rev(list1):
    list2=[]
    for fruit in list1:
        rev=""
        for i in fruit:
            rev=i+rev
        list2+=[rev]
    print(list2)
            
rev(['apple' , 'banana' , 'orange' 'mango' , 'grapes' ])

