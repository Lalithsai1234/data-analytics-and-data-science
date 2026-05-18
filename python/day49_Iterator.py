"""
Iterators
Generators
Decorators
"""


# Iterators     ---> can work with str, list, tuple, dict(keys), set
#iterator is an object which use values or elements one by one from collections
print("="*32)
print("Iterator")
print("="*32)

lst=[1,2,3,4]
it=iter(lst)
print(it)       #<list_iterator object at 0x000001BD3CB2BF40>
# print(len(it)) #it gives an error because it doesn't storing in a single file 


print(next(it), end=" ") #1
print(next(it), end=" ") #2
##or
for i in it: #here continues from 3 because it was already passed the 1 and 2
    print(i, end=" ")
# print(next(it)) #it gives error if we using after completing the length of it


##Internal working of the for loop
while True:
    try:
        print(next(it))
    except StopIteration:
        print("\nIteration was completed")
        break


#why should we use iter in real life
from sys import getsizeof
lst=[i for i in range(1,1001)]
itr=iter(range(1,1001))
print(getsizeof(lst))   #8856
print(getsizeof(itr))   #32 #it will only take 32 bytes because only do the the goes and store the next element after calling
res=[next(itr)**2 for _ in range(1,11)]
print(res)

##Custom Iterators

class MyIterator:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self): # Iterable
        return self # -> Iterator
    
    def __next__(self):
        if self.start <= self.end: # 6 <= 5
            val = self.start # val = 4
            self.start += 1 # 2
            return val # 2
        else:
            raise StopIteration
        
obj = MyIterator(1,5) # -> Iterable
itr = iter(obj) #it was optional bcz even without that it was working
print(obj) #both address are same 
print(itr) #both address are same
print(next(itr), end=" ") #but if we don't use iter we use obj in next
print(next(itr), end=" ")
print(next(itr), end=" ")
print(next(itr), end=" ")
print(next(itr))
obj2 = MyIterator(2,5)
print(next(obj2))
# Generator
print("="*32)
print("Generator")
print("="*32)
lst=[i for i in range(1,1001)]
gen=(i for i in range(1,1001))
print(getsizeof(lst))   #8856 bytes
print(getsizeof(gen))   #192 bytes
