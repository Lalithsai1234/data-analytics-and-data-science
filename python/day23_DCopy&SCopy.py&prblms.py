"""1. if we copy one thing-->
a.orignal
b.copied piece
"""
"""
shallow copy-- copies the objects with reference of the object if it was nested 
                so i we change nested object value it reflects the original it  (copy.copy())
                ex: here it have list inside a list so does not copy the nested list it copies its reference
deep copy--> the deep copy copies the nested data too instead of coping the references
"""
import copy
original=[[1,2], [3, 4]]
copied=copy.copy(original)
print("before shallow copy:")
print(original)
print(copied)
copied[1][1]="hello"
print("after shallow copy:")
print(original)
print(copied)

original=[[1,2], [3, 4]]
copied=copy.deepcopy(original)
print("before deep copy:")
print(original)
print(copied)
copied[1][1]="hello"
print("after deep copy:")
print(original)
print(copied)




"""             problems            """

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
for i in range(1,6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for i in range(1,6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()


"""
A
A B
A B C
A B C D
A B C D E
"""

for i in range(1,6):
    for j in range(0, i):
        print(chr(j+65), end=" ")
    print()
x=64
for i in range(1,6):
    for j in range(1, i+1):
        print(chr(i+64), end=" ")
    print()
print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))
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