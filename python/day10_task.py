#iterate a number in reverse order with the while loop
#note without converting it into string
nums=1234
while nums!=0:
    print(nums%10)
    nums//=10

#iterate the number in the left to right with while loop
#note without converting it into string

n=1234
p=1
while p<=n//10:
    p*=10

while p>0:
    print(int(n/p))
    n=n%p
    p=p//10     #p/10 here the problem is if do that after p=1 it doesn't stop it goes to 0.1 which was higher than 0 then in another iteration it goes to 0.001