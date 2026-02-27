units=200#int(input("enter the no of units: "))
if units<=100:
    print(units*2)
elif units<=200:
    print(((units-100)*3)+(2*100))
else:
    print(((units-200)*5)+(units*3)+(units*2))


                ##strings

str1="hello"
str2='do something great'
print(str1.upper())     #HELLO
print(str1 . lower())   #hello
print(str1.isupper())   #False
print(str1 .islower() ) #True
print(str1.capitalize())#Hello
print(str2.capitalize())#Do something great
print(str2.title())     #Do Something Great


#replace
print(str2.replace('e', 'a',1)) #the default everting


            ##lists

##slicing
list1=[4, 6, 7, 8, 12, 14, 16]
print(list1[2:4])   #[7, 8]
print(list1[1:6:2]) #[6, 8, 14]
print(list1[::2])   #[4, 7, 12, 16]
print(list1[::-1])  #[16, 14, 12, 8, 7, 6, 4]


"""
1. append()---> the single value at the end of the list
2. extend()-->  adds multiple elements at a time to the given list through iterable objects(list/tuple/sets)
3. insert()-->add the value at specific index in the existing list
4. remove()-->removes the first occurred of argument if found. if not throws the error. it doesn't return any values
5. pop()--> removes the last element from the list if not arg passes. if arg passes then removes the indexed value as per the arg.
            if index not found then throws an error pop method will returns the value which is removed
6. clear()-->clears all the elements in the list
7. index()--->returns the index num of first occurred of arg value
8. sort()-->sort the list in ascending order by default to sort in descending order we can use reverse=True inside sort meth()
9. reverse()-->will reverse the given list
10.sorted()-->sort method will change thc original list sorted method will not change the original list but returns
            the new list by sorting it out.
11. join()--->it will joins all the elements in the given iterable(list,tuple,set) with any string

"""
list1.append(5)     #[4, 6, 7, 8, 12, 14, 16, 5]
list1.extend((4,8)) #[4, 6, 7, 8, 12, 14, 16, 5, 4, 5]
list1.extend([7,9]) #[4, 6, 7, 8, 12, 14, 16, 5, 4, 7, 8, 9]
list1.extend({7,9}) #[4, 6, 7, 8, 12, 14, 16, 5, 4, 7, 8, 9, 9, 7]

list1=[4, 6, 7, 8, 12, 14, 16]
list1.insert(1, 8)      #[4, 8, 6, 7, 8, 12, 14, 16]
list1.insert(1, [1,8])  #[4, [1, 8], 6, 7, 8, 12, 14, 16]
list1.insert(-1, 0)     #[4, [1, 8], 6, 7, 8, 12, 14, 0, 16] it will add it from backwards
list1.insert(11, -1)    #if the index was more than the len it will add it in the end
print(list1)

list1=[4, 6, 7, 8, 12, 14, 16, 7]
list1.remove(7) #removes the only first match [4, 6, 8, 12, 14, 16, 7]
list1.pop()     #removes the last element if no argument passes  [4, 6, 8, 12, 14, 16]
# list1.pop(11)   #gives an error if the index is not their
list1.pop(-1) #[4, 6, 8, 12, 14]
print(list1)
list1.clear #clears the complete list and list will be like this []

list1=[4, 6, 7, 8, 12, 14, 16, 7]
print(list1.index(12,0,5)) #index(value, start, end) it will only search from start to end


li=[4, 6, 7, 8, 12, 14, 16, 7]
li.sort()
li.sort(reverse=True)
li.reverse
print(sorted(li))  #not modify the existing list


list1=['apple', 'banana' , 'orange', 'grapes']
op="-".join(list1)
print(op)   #apple-banana-orange-grapes