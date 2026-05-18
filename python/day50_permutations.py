
# def back(num,temp):
#     if len(temp)==n:
#         res.append(temp)
#         return
#     if num<n and len(temp)<n:
#         temp+=str(num)
#         back(num+1,temp)
#         back(num-1, temp)
# back(1, "")
# print(res)
n=4
count=0
res=[]
def recur(fixed,vary):
    if len(fixed+vary) == n and len(set(fixed+vary)) == n:
        if fixed+vary not in res:
            res.append(fixed+vary)
            return
    if len(vary)>1:
        mid=(len(vary)//2)
        recur(fixed+vary[:mid], vary[mid:])
        recur(fixed+vary[mid:], vary[:mid])
temp=""
for i in range(1,n+1):
    temp+=str(i)
print(temp)
temp2=""
for i in range(n):
    temp2=temp[i]+temp[:i]+temp[i+1:]
    for i in range(n-1,-1,-1):
        recur(temp2[:i],temp2[i:])
print(sorted(res))
print(res)

# 1234
# 1243
# 1324
# 1342
# 1423
# 1432
# 2134
# 2143
# 2314