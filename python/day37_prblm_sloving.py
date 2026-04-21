#if sum of the digits in a number is even it should show in output 
ip=[12,4,33, 57, 88, 221, 222, 12345]
op=[]
for i in ip:
    sum=0
    temp=i
    while temp!=0:
        sum+=temp%10
        temp//=10
    if sum%2==0:
        op.append(i)
print(op)

#if the sum of the digits in the number is prime number it should be displayed in the outputs
ip=[22, 34, 77, 122,890]
op=[]
for i in ip:
    sum=0
    temp=i
    while temp!=0:
        sum+=temp%10
        temp//=10
    for j in range(2,(sum//2)+1):
        if sum%j==0:
            break
    else:
        op.append(i)
print(op)

# search the key if it exists  input in the list given then print(exists) or else print(not exists)
ip=[5,3,2,8,10,14,3]
key=22
for i in ip:
    if key==i:
        print("key exists")
        break
else:
    print("key doesn't exists")

ip= [1,2,3,4,5]
op= ip[1:]+ip[:1]
print(op)