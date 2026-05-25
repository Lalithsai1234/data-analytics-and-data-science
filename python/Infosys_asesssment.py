brac="(())))"#input()
l_price=5#int(input()) #price of one '('
r_price=3#int(input()) #price of one ')'
l_count=0
r_count=0
for i in brac:
    if i=='(':
        l_count+=1
    elif i==')' and l_count>=1:
        l_count-=1
    elif i==')' and l_count<1:
        r_count+=1
sum=0
sum+=l_count*r_price
sum+=r_count*l_price
print(sum)


def get_permutations(numbers, path=[], used=[]):
    # If our path is the same length as the numbers, we found a full combination!
    if len(path) == len(numbers):
        print(path)
        return

    # Try adding each number
    for i in range(len(numbers)):
        if i not in used:
            # 1. Choose a number
            used.append(i)
            path.append(numbers[i])
            
            # 2. Explore further
            get_permutations(numbers, path, used)
            
            # 3. Step back (Backtrack) to try the next option
            path.pop()
            used.pop()

get_permutations([1, 2, 3, 4])