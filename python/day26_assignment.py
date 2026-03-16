# section 4
# 2 question
word=""
ls=[]
input  = "python is a very powerful programming language"
for wrd in input:
    if wrd==" ":
        ls.append(word)
        word=''
    else:
        word+=wrd
else:        
    ls.append(word)

print(ls)
longest=""
for i in ls:
    if len(longest)<len(i):
        longest=i
print(longest)

# 3 question
input= "aabbcdde"
freq={}
for i in input:
    freq[i]=freq.get(i,0)+1
for i in freq:
    if freq[i]==1:
        print(i)
        break


#4 question rotations
input= [1,2,3,4]
expected=[3,4,1,2]

for i in range(len(input)):
    # print(input[i:]+input[:i],end="  ")
    if (input[i:]+input[:i])==expected:
        print(True)
        break
else:
    print(False)


#5 question
input = "aaaabbcc"
count=0
op=""
for i in range(len(input)):
    count+=1
    if  i+1==len(input) or input[i]!=input[i+1]:
        op+=input[i]
        op+=str(count)
        count=0
        continue
print(op)
