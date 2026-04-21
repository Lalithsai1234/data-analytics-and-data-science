"""
================================
dict comprehension
================================
"""
# Program 1: Create a dictionary from 1 to 10 where
# key = number and value =cube of the number.
d1={i:i**3 for i in range(1, 11)}
print(d1)


# Program 2: Given names - [ "a", "bb" ,"ccc"]
# create a dictionary where
# key = name and value is length of the name.
a=[ "a", "bb" ,"ccc"]
d2={i: len(i) for i in a}
print(d2)

# Program 3: Create a dictionary for numbers 1 to 10 where
# each number is mapped to "even" or "odd" .
d3={i:"even"if i%2==0 else "odd" for i in range(1,11)}
print(d3)

# Program 4: Given the string word ="mississippi"
# create a dictionary where
# key = character and value = frequency of that character.
a="mississippi"
d4={i:a.count(i) for i in a}
# d4={i:d4.get(i, 0)+1 for i in a} #it gives the error bcz you can't assign to itself
print(d4)

# Program 5: Given prices -- {"pen" :10, "book": 120 ,"bag": 700 ,"eraser":5}
# create a dictionary that keeps only items with value 100
a={"pen" :10, "book": 120 ,"bag": 700 ,"eraser":5}
d5={k: v for k,v in a.items() if v>=100}
print(d5)

# Program 6: Given nums -
# create a dictionary where key = number and value - square of the number,
a=[1,2,5,4,7,8,1,6]
d6= {i: i**2 for i in a if i%2!=0}
print(d6)

# Program 7:
# Given words -["apple" , "hi",  "banana", 'cat , "elephant"]
# create a dictionary that keeps only words with length greather than 3
# where key = word and value =length of the word.
a=["apple" , "hi",  "banana", 'cat' , "elephant"]
d7={i: len(i) for i in a if len(i)>3}
print(d7)

# Program 8: Given the dictionary 
# d = {"x": 1, "y": 2, "z": 3} 
# create a new dictionary by swapping keys and values.
a={"x": 1, "y": 2, "z": 3} 
d8={v:k for k,v in a.items()}
print(d8)

# Program 9: Given students ={"Ram": 28, "Sam" :45,"Tom" :90}
# create a dictionary where each student is mapped to PASS OR FAIL
a ={"Ram": 28, "Sam" :45,"Tom" :90}
d9={k: "pass" if v>=33  else "fail" for k,v in a.items() }
print(d9)

# Program 10: Given nums = [1, 1, 2, 2, 2, 3, 3] 
# create a dictionary where 
# key = number and value = count of that number. 
a=[1, 1, 2, 2, 2, 3, 3] 
d10={i:a.count(i) for i in set(a)}
print(d10)

# Program 11: Given the string s - "python makeS coding fun"
# create a dictionary where
# key = word and value length of the word,
# keeping only words with length greater than 5.
s="python makes coding fun"
d11={i:len(i) for i in s.split(' ') if len(i)>5}
print(d11)