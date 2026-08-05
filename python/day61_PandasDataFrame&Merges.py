import numpy as np
import pandas as pd


# DataFrame basic methods
data = {
    'name': ['sai', 'lalith', 'syam', 'ram', 'anand', 'priya', 'kiran', 'arjun', 'divya', 'vijay'],
    'Ages' : [27, 37, 47, 23, 31, 29, 35, 42, 26, 33],
    'Places' : ['Hyd', 'Bng', 'Chn', 'Mum', 'Del', 'Kol', 'Chn', 'Hyd', 'Bng', 'Mum'],
    'Status': ['Married', 'Married', 'Single', 'Single', 'Married', 'Single', 'Married', 'Single', 'Married', 'Single']
}
df=pd.DataFrame(data)


print(df.shape)
# (10, 4)
print(df.columns)
# Index(['name', 'Ages', 'Places', 'Status'], dtype='object')
print(df.keys())
# Index(['name', 'Ages', 'Places', 'Status'], dtype='object')
print(df.isnull())
#     name   Ages  Places  Status
# 0  False  False   False   False
# 1  False  False   False   False
# 2  False  False   False   False
# 3  False  False   False   False
# 4  False  False   False   False
# 5  False  False   False   False
# 6  False  False   False   False
# 7  False  False   False   False
# 8  False  False   False   False
# 9  False  False   False   False
print(df.sum()) #it can be used on complete df but it was mostly used on columns with int
# name         sailalithsyamramanandpriyakiranarjundivyavijay
# Ages                                                    330
# Places                       HydBngChnMumDelKolChnHydBngMum
# Status    MarriedMarriedSingleSingleMarriedSingleMarried...
# dtype: object
print(df['Ages'].mean()) #it gives an error bcz we can't find mean non numbers op:33.0 
print(df.min())
# name        anand
# Ages           23
# Places        Bng
# Status    Married
# dtype: object
print(df.count())
# name      10
# Ages      10
# Places    10
# Status    10
# dtype: int64
print(df['Places'].value_counts()) #it can directly take the complete df it will compare rows 
# Places
# Hyd    2
# Bng    2
# Chn    2
# Mum    2
# Del    1
# Kol    1
# Name: count, dtype: int64
print(df['Places'].unique())
# ['Hyd' 'Bng' 'Chn' 'Mum' 'Del' 'Kol']
print(df['Places'].nunique()) #it will no of unique words op:6
print(df['Ages'].sort_values()) #it can only be used on the int column
# 3    23
# 8    26
# 0    27
# 5    29
# 4    31
# 9    33
# 6    35
# 1    37
# 7    42
# 2    47
# Name: Ages, dtype: int64
print(df.sort_index())#here we can give a complete data frame bcz we are already specified int index column
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

df.loc[10]=["ram", 23, "Mum", "Single"]
print(df.drop_duplicates()) #if we use inplace we can edit the original dataframe
    #  name  Ages Places   Status
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
print(df['Ages'].astype(float))
# 0     27.0
# 1     37.0
# 2     47.0
# 3     23.0
# 4     31.0
# 5     29.0
# 6     35.0
# 7     42.0
# 8     26.0
# 9     33.0
# 10    23.0
# Name: Ages, dtype: float64

data = {
    'name': ['sai', 'lalith', 'syam', 'ram', np.nan, 'priya', 'kiran', 'arjun', 'divya', 'vijay'],
    'Ages' : [27, 37, 47, 23, np.nan, 29, 35, 42, 26, 33],
    'Places' : ['Hyd', 'Bng', 'Chn', np.nan, 'Del', 'Kol', np.nan, 'Hyd', 'Bng', 'Mum'],
    'Status': ['Married', 'Married', np.nan, 'Single', 'Married', 'Single', 'Married', 'Single', 'Married', 'Single']
}
df=pd.DataFrame(data)

print(df.dropna()) #if we use inplace it deletes from original df
#      name  Ages Places   Status
# 0     sai  27.0    Hyd  Married
# 1  lalith  37.0    Bng  Married
# 5   priya  29.0    Kol   Single
# 7   arjun  42.0    Hyd   Single
# 8   divya  26.0    Bng  Married
# 9   vijay  33.0    Mum   Single
df['Ages'].fillna(df['Ages'].mean(), inplace=True)
print(df)
#   df['Ages'].fillna(df['Ages'].mean(), inplace=True)
#      name       Ages Places   Status
# 0     sai  27.000000    Hyd  Married
# 1  lalith  37.000000    Bng  Married
# 2    syam  47.000000    Chn      NaN
# 3     ram  23.000000    NaN   Single
# 4     NaN  33.222222    Del  Married
# 5   priya  29.000000    Kol   Single
# 6   kiran  35.000000    NaN  Married
# 7   arjun  42.000000    Hyd   Single
# 8   divya  26.000000    Bng  Married
# 9   vijay  33.000000    Mum   Single

print(df['Ages'].agg(['max', 'min', sum, 'count', 'std', 'mean'])) #mostly give them in Strings to stop getting an error
df1 =pd.DataFrame({
    'id':[1,2,3],
    'Name' : [ 'Suresh', 'Ramesh', 'Mahesh']
})
df2=pd.DataFrame({
    'id':[1,2,3],
    'marks':[50,30,75]
})
print(pd.merge(df1,df2))  #it was mostly used for the column joining
#    id    Name  marks
# 0   1  Suresh     50
# 1   2  Ramesh     30
# 2   3  Mahesh     75

# Concat example: combine two DataFrames vertically
concat_df1 = pd.DataFrame({
    'id':[1,2,3],
    'Name':['Suresh', 'Ramesh', 'Mahesh']
})
concat_df2 = pd.DataFrame({
    'id':[4,5,6],
    'Name':['Kiran', 'Anita', 'Naveen']
})
print(pd.concat([concat_df1, concat_df2], ignore_index=True))
#    id    Name
# 0   1  Suresh
# 1   2  Ramesh
# 2   3  Mahesh
# 3   4   Kiran
# 4   5   Anita
# 5   6  Naveen

