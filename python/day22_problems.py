
"""
*
*
*
*
*
"""
for x in range(1,6):
    print('*')


""" ***** """

for x in range(1,6):
    print('*',end=' ')


"""
*****
*****
*****
*****
*****
"""
for i in range(1,6):
    for x in range(1,6):
        print('*',end=' ')
    print()


"""
11111
11111
11111
11111
11111
"""
for i in range(1,6):
    for x in range(1,6):
        print(1,end=' ')
    print()


"""
12345

"""
for x in range(1,6):
    print(x,end=' ')



"""
12345
12345
12345
12345
12345

"""
for y in range(1,6):
    for x in range(1,6):
        print(x,end=' ')
    print()


"""
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
"""

for y in range(1,6):
    for x in range(1,6):
        print(y,end=' ')
    print()


# print(chr(97))

"""
ABCDE
ABCDE
ABCDE
ABCDE
ABCDE
"""

for y in range(1,6):
    for x in range(65,70):
        print(chr(x),end=' ')
    print()



"""
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE
"""
for y in range(65,70):
    for x in range(65,70):
        print(chr(y),end=' ')
    print()


"""
A B C
D E F
G H I

"""
alphabet=65
for y in range(5):
    for x in range(5):
        print(chr(alphabet),end=' ')
        alphabet+=1
    print()

"""

1 2 3
4 5 6
7 8 9

"""

num=1
for y in range(3):
    for x in range(3):
        print(num,end=' ')
        num+=1
    print()

# y=0-->x=0,1,2
# y=1-->x=0,1,2
# y=2-->x=0,1,2


"""
0 1 0
1 0 1
0 1 0
"""
for x in range(3):
    for y in range(3):
        print((x+y)%2,end=' ')
    print()

# x=0-->y=0,1,2
# x=1--->y=0,1,2
# x=2-->y=0,1,2

# print((0+0)%2)
# print((0+1)%2)
# print((0+2)%2)

# print((1+0)%2)
# print((1+1)%2)
# print((1+2)%2)

# print((2+0)%2)
# print((2+1)%2)
# print((2+2)%2)



#Tasks
"""
1 2 3
2 3 4
3 4 5
"""
for i in range(1,4):
    for j in range(i, i+3):
        print(j, end=" ")
    print()

for i in range(3):
    for j in range(1,4):
        print(i+j, end="")
    print()

"""
a b c
b c d
d e f
"""
x=96
for i in range(3):
    for j in range(1,4):
        print(chr(x+i+j), end=" ")
    print() 
for i in range(1,4):
    for j in range(i,i+3):
        print(chr(x+j), end=" ")
    print()
