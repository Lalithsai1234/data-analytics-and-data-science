# "abcd"--->print all the substrings of given string 
# a 
# ab 
# abc 
# abcd 
# b 
# bc 
# bcd 
# c 
# cd 
# d 
#count number of substrings can be done for given string

s1='abcd'
count=0
for i in range(len(s1)):
    res=""
    for j in range(i, len(s1)):
        res+=s1[j]
        print(res)
        count+=1
print(count)
