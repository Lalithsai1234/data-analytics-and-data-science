import pandas as pd
import numpy as np
"""
DataFrame 
"""


data = {
    'name': ['sai', 'lalith', 'syam', 'ram', 'anand', 'priya', 'kiran', 'arjun', 'divya', 'vijay'],
    'Ages' : [27, 37, 47, 23, 31, 29, 35, 42, 26, 33],
    'Places' : ['Hyd', 'Bng', 'Chn', 'Mum', 'Del', 'Kol', 'Chn', 'Hyd', 'Bng', 'Mum'],
    'Status': ['Married', 'Married', 'Single', 'Single', 'Married', 'Single', 'Married', 'Single', 'Married', 'Single']
}

df=pd.DataFrame(data)
print(df)
#      name  Ages Places   Status
# 0     sai    27    Hyd  Married
# 1  lalith    37    Bng  Married
# 2    syam    47    Chn   Single
# PS D:\10k coders> & C:\Python313\python.exe "d:/10k coders/python/day60_Pandas.py"
#      name  Ages Places   Status
# 0     sai    27    Hyd  Married
# 1  lalith    37    Bng  Married
# 2    syam    47    Chn   Single
# 3     ram    23    Mum   Single
# 4   anand    31    Del  Married
# 5   priya    29    Kol   Single
# 6   kiran    35    Chn  Married
# 7   arjun    42    Hyd   Single
# 8   divya    26    Bng  Married
# 9   vijay    33    Mum   Single


"""
indexing in dataframe
"""
# print(df[1]) it will gives the error bcz in data we can access column directly
print(df.loc[1])
# name       lalith
# Ages           37
# Places        Bng
# Status    Married
# Name: 1, dtype: object
print(df.loc[1]['name']) #here when we use loc it gives a series where col names are the index so op:lalith
print(df.loc[1, 'name']) #works same op:lalith
print(df.loc[[1,3,4], ['name', 'Ages']])
#      name  Ages
# 1  lalith    37
# 3     ram    23
# 4   anand    31
print(df.loc[1:4,['name', 'Ages']])
#      name  Ages
# 1  lalith    37
# 2    syam    47
# 3     ram    23
# 4   anand    31
print(df.iloc[2])#it will works same loc until the index are different

"""
other methods
info()
"""
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   name    10 non-null     object
#  1   Ages    10 non-null     int64 
#  2   Places  10 non-null     object
#  3   Status  10 non-null     object
# dtypes: int64(1), object(3)
# memory usage: 452.0+ bytes
# None
print(df.describe())
#             Ages
# count  10.000000
# mean   33.000000
# std     7.468452
# min    23.000000
# 25%    27.500000
# 50%    32.000000
# 75%    36.500000
# max    47.000000


"""
adding a new row and column
"""
df.loc[10]=["ish", 25, 'hyd', 'single']
print(df.loc[10])
# name         ish
# Ages          25
# Places       hyd
# Status    single
# Name: 10, dtype: object 

df['Gender']=np.random.choice(["Male", "Female"],11)
# print(df["Gender"])
# 0     Female
# 1     Female
# 2       Male
# 3       Male
# 4       Male
# 5       Male
# 6     Female
# 7       Male
# 8       Male
# 9     Female
# 10    Female
# Name: Gender, dtype: object


"""
drop a row
drop a column
"""

print(df.drop(10)) #it doesn't delete the original dataframe
df.drop(10, inplace=True) #with inplace we can change the original dataframe

df.drop(columns='Gender', inplace=True) #it will delete a column from dataframe #note if you print it op:None
print(df.drop(columns=["name","Ages"]) ) #it will returns thee data frame with deleted columns doesn't change anything

