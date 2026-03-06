

"""
A
B B
C C C
D D D D
E E E E E
"""
for i in range(1,6):
    for j in range(1, i+1):
        print(chr(i+64), end=" ")
    print()


ip=['Hii','hello','java']
op=[]
for char in ip:
    res=""
    if ord(char[0])<=90:    
        index=0
        for i in char:
            if index==0:
                res=chr(ord(i)+32)
                index=1
                continue
            res=i+res
    else:
        for i in char:
            res=i+res
    op+=[res]
print(op)# op=[ 'iih','Hello', 'avaj']



ip=['Hii','hello','java']
op=[]
for char in ip:
    res=""
    for i in char:
        if ord(i)<=90 and not res:    
            res=chr(ord(i)+32)
            continue
        res=i+res
    op+=[res]
print(op)# op=[ 'iih','Hello', 'avaj']