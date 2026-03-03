"""
set-methods

1.intersection_update() -->#it will modify the original set with common elements from the given set
2.difference_update() --> #it will removes the original set with values which are same by comparing with second set
3.symmetric_difference() --> the new set with uncommon values from 2 sets we can use ^ A performs the symmetric difference operation
5.symmetric_difference_update()--> it will modify the original set with un common values


note:when we are suing the symbols the two object should be the set but when we are using the method name the objects can be list or tuple

"""
set1={'kumar','vijay', 'ajay'}

set2={'kumari', 'krishna', 'sushma', 'vijay', 'meghana'}

print(set1.intersection(set2)) #it return the intersected value -- {'vijay'}
print(set1.intersection_update(set2)) #it will modify the original set with intersected elements -- None
print(set1) #{'vijay'}

set1={1,2,3}
set2={3,4,5}
op=set1.difference(set2)
print(op) #{1,2}

set1.difference_update(set2)
print(set1)#{1,2} it was updating the original  set1


set1={'apple', 'banana','orange'}
set2={'kiwi','grapes', 'banana' , 'orange'}
op=set1.symmetric_difference(set2) #it will returns the uncommon values in the both sets
print(op)
set1.symmetric_difference_update(set2)
print(set1)#it will assign the uncommon values in both sets to the original set

"""
5.issubset()-->check if one set is completely inside of another set.
6.<=check the issubset or not
7.issuperset()-->check if set contains all elements of another set
8.>= checks superset or not
9.isdisjoint()-->check if two sets have no common elements it doesn't have symbol
10.clear()-->removes all the elements from the set
"""
x={'read','write','edit','share'}
y={'read','write'}
op=y.issubset(x)
op=y<=x
print(op)

x1={1,2,3,4,5,6}
x2={4,5,2,3,'hello'}
op=x1.issuperset(x2)
op1=x2.issubset(x1)
print(op)
print(op1)

xx1={1,2,3}
xx2={5,6,4}
op=xx1.isdisjoint(xx2)
print(op)

xx2.clear()
print(xx2)






"""                                                    Dict
get()--->to access the values from the dictinary using key_names
keys()-->returns keys from the dictinary in the form of a list
values()-->returns the values from the dictionary in the form of a list
items()--<returns the keys and values in tuple in form of list
pop()--->removes the specified key-named value
update()-->add the property if it is not available or updates with new value if 
it is available already.
popitem()--->removes last property from dictionary
clear()--->clears all the key-value pairs from the dict
"""
dict1={'name':'kiran','city':'hyd','age':25}

x=dict1.get('name',0) #it will zero if no key exists as name
print(x)


for key in dict1.keys(): #it will return the list of key name
    print(key)

op=dict1.values() #it will return the list values in the dict
print(op)

op=dict1.items() #it will returns the list of tuples with key value pairs
print(op)

for item in dict1.items(): #here the item was the tuple which contain key value pairs
    print(item)

for x,y in dict1.items(): #here we un packing the key value pairs x as key and y as value
    print(f"{x}:{y}")

dict1.popitem() #it will pop the last item from the dict
print(dict1)

dict1.pop('city') #it will remove the specified item from the dict
print(dict1)

dict1.update({'city1':'gtr'}) #it will update the existing value if the key exists or else it will add a key value pair
print(dict1)

dict1.clear() #it will clear the dict






