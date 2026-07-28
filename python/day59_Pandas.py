import numpy as np
import pandas as pd

"""
Pandas 
-------------------------
used for to store a specific person details we use dictionary but if we need to store in real storage like rom
we need to use the pandas 
1. To store the data in tabular format
2. to visualize the data in tabular format
3. to clean the data
4. to analyze the data
"""
stu_details = {
    'stu1': {'name': 'Suresh', 'marks': 78, 'place': 'Hyd'},
    'stu2': {'name': 'Mahesh', 'marks': 88, 'place': 'Bng'},
    'stu3': {'name': 'Rakesh', 'marks': 66, 'place': 'Chn'}
}
print(stu_details)
""" the op will be understand to hard
{'stu1': {'name': 'Suresh', 'marks': 78, 'place': 'Hyd'}, 'stu2': {'name': 'Mahesh', 'marks': 88, 'place': 'Bng'}, 'stu3': 
{'name': 'Rakesh', 'marks': 66, 'place': 'Chn'}}
"""

"""
panda provides two types of data structure
1. series -->1 array (it can have single column)
2. data frames --> 2d array (it can have multiple column)
"""
lst=[1,2,3,4]
series=pd.Series(lst) #syntax is main series should be with capital 'Series'
print(series)
"""
0    1
1    2
2    3
3    4
dtype: int64
"""

print(series[0])#those give are work as keys not index op:1
# print(series[-1])#it gives the error because their is no key like that op: keyError


"""Basic Information
s. head() we can pass no of head values too default was 5
s. tail() same goes for tail
astype()
s. shape
s. size
s. dtype
s. index
name
value
index
"""
print(series.index) #RangeIndex(start=0, stop=4, step=1)
print(series.values) #[1 2 3 4]
print(series.name) #we need to assign a name first op:None 
series.name="sai"
print(series.name) #it give the name which states kind of data it stored op:sai
print(series.shape) #the op will be a tuple most used for data frame to find no of columns op:(4,) 
print(series.size) #it will gives the no of rows in int op:4
print(series.dtype) #it will gives data type stored data op: int64
series[0]=1.1 #it doesn't gives the error it will just give a futurewarning
print(series.dtype) #here every datatype was changed into float 64
print(series.head()) #it will first 5 rows 
print(series.head(2)) #it will give only 2 rows
s=series.astype(int)#it doesn't change the original series it will return the updated series
print(s.dtype) #op:int64


##indexes
series.index=['A', 'B', 'C', 'D']
print(series)
"""
A    1.1
B    2.0
C    3.0
D    4.0
Name: sai, dtype: float64
"""
s=pd.Series([1,3,5,7,9], index=['mango', 'banana', 'orange', 'grapes', 'apple'])
s.name="calories"
print(s)
"""
mango     1
banana    3
orange    5
grapes    7
apple     9
Name: calories, dtype: int64
"""

"""
Statistical Methods
s. sum()
s. mean()
s. median()
s.min()
s.max()
s.std()
s.var()
s. count()
"""
dic={'a':1, 'b': 2, 'c':3, 'd':4}
series=pd.Series(dic)
print(series)
"""
a    1
b    2
c    3
d    4
dtype: int64
"""
print(series.sum())      # total of all values
print(series.mean())     # average of values
print(series.median())   # middle value
print(series.min())      # smallest value
print(series.max())      # largest value
print(series.std())      # standard deviation
print(series.var())      # variance
print(series.count())    # count of non-null values


"""
Value-related Methods
s.unique()
s.nunique()
s.value_counts( )
duplicated
"""
s=pd.Series([1,2,3,2,3,5,4,5])
print(s.unique()) #don't show any duplicates op:[1 2 3 5 4]
print(s.nunique()) #it no of unique values #5
print(s.value_counts()) #gives the value and it' count
# 2    2
# 5    2
# 3    2
# 1    1
# 4    1
# Name: count, dtype: int64
print(s.duplicated()) #it gives the index and index value have duplicate or not in t/f
# 0    False
# 1    False
# 2    False
# 3     True
# 4     True
# 5    False
# 6    False
# 7     True
# dtype: bool


"""
Sorting
s.sort_values()
s.sort_index()
"""
s=pd.Series([1,2,3,2,3,5,4,5])
print(s.sort_values()) #it will sort based on the value
# 0    1
# 1    2
# 3    2
# 2    3
# 4    3
# 6    4
# 5    5
# 7    5
# dtype: int64
print(s.sort_index()) #it will  sort based on the index value
# 0    1
# 1    2
# 2    3
# 3    2
# 4    3
# 5    5
# 6    4
# 7    5
# dtype: int64


"""
Missing Values
s.isnull()
s.notnull()
s.dropna()
s.fillna(0)
"""
s=pd.Series([1, 2, np.nan, 5,None, 0])
print(s.isnull()) #it doesn't take 0 as null, it gives the false to no null values
# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
# 5    False
# dtype: bool
print(s.notnull()) #opposite of isnull here it will true for not null values
# 0     True
# 1     True
# 2    False
# 3     True
# 4    False
# 5     True
# dtype: bool
print(s.dropna()) #it will delete the rows of null values
# dtype: bool
# 0    1.0
# 1    2.0
# 3    5.0
# 4    0.0
# dtype: float64
print(s.fillna(0)) #it will fill the null value with given value
# 0    1.0
# 1    2.0
# 2    0.0
# 3    5.0
# 4    0.0
# 5    0.0
# dtype: float64



