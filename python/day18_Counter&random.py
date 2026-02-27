from collections import Counter

l1=['a','b','a','b','c','e','c','a']
freq=Counter(l1)
print(freq) #Counter({'a': 3, 'b': 2, 'c': 2, 'e': 1})
print(freq['a'])  #we can use it as a normal dictionary

print(freq.most_common())  #if we won't give how many you it will give a tuple of lists with every character [('a', 3), ('b', 2), ('c', 2), ('e', 1)]
print(freq.most_common(1)) #it will give the top most common element [('a', 3)]
print(freq.most_common(2)) #[('a', 3), ('b', 2)]

freq.update(['e', 'e'])
print(freq)  #Counter({'a': 3, 'e': 3, 'b': 2, 'c': 2})
freq.subtract(['a'])
print(freq)  #Counter({'e': 3, 'a': 2, 'b': 2, 'c': 2})

 #we need to convert it into list if not it will give <itertools.chain object at 0x0000014D908C0400>
print(list(freq.elements())) #['a', 'a', 'b', 'b', 'c', 'c', 'e', 'e', 'e']


#l1=['a','b','a','b','c','e','c','a']
l2=['a','b','a','c','a','e','d']
count1=Counter(l1)
count2=Counter(l2)
print("count1= ", count1)
print("count2= ",count2)
print(count1+count2) # gives the count values based on two counters
print(count1-count2) #one count value subtracts the another count value for the same element
print(count2-count1) #if it is zero or below zero it doesn't show anything
print(count1&count2)  #it takes the common values only but it will takes the least value
print(count1|count2) #it will takes the all values but it will take the highest value



# Square root
# factorial
# power
# sin - trigonometry
# log10() --> log - base 10


# Roll a dice 10000 times
# Storing all the outputs in a list
# What is the probablility of getting each side from those 10000 tr

import random
num=[1,2,3,4,5,6]
# count={}
rolls=[]
for i in range(1000):
    choice=random.choice(num)
    # count[choice]=count.get(choice,0)+1
    rolls.append(choice)
counts=Counter(rolls)
for i in counts:
    prob=counts[i]/10
    print(f"the probability of {i} is {prob}%")
print(counts)


# Compare 2 words to see if they are annagrams
# use counter module 

# take 2 stores sales data in 2 lists
# find out the total sales in both stores combined
# Find out the Common items in both stores
# Items in only store 1

# Generate a random password every time you run the file
# the password must be 10 characters
# Password must have an Upper case character, Lower case character And a numberb