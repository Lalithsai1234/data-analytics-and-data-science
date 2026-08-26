import pandas as pd
import numpy as np
"""
CSV 
SQLwith engine.begin() as conn:
    conn.execute(text("DROP TABLE IF EXISTS Student"))

JSON
EXCEL
"""

data = {
    'name': ['sai', 'lalith', 'syam', 'ram', np.nan, 'priya', 'kiran', 'arjun', 'divya', 'vijay'],
    'Ages' : [27, 37, 47, 23, np.nan, 29, 35, 42, 26, 33],
    'Places' : ['Hyd', 'Bng', 'Chn', np.nan, 'Del', 'Kol', np.nan, 'Hyd', 'Bng', 'Mum'],
    'Status': ['Married', 'Married', np.nan, 'Single', 'Married', 'Single', 'Married', 'Single', 'Married', 'Single']
}
df=pd.DataFrame(data)
# Export from program to csv (use forward slashes or raw strings to avoid escape issues)
df.to_csv('python/day62_new.csv') #if we use index is false it don't take index as a column
# Import
df = pd.read_csv('python/day62_new.csv')
print(df)
#   df=pd.read_csv('python\day62_new.csv')
#      name  Ages Places   Status
# 0     sai  27.0    Hyd  Married
# 1  lalith  37.0    Bng  Married
# 2    syam  47.0    Chn      NaN
# 3     ram  23.0    NaN   Single
# 4     NaN   NaN    Del  Married
# 5   priya  29.0    Kol   Single
# 6   kiran  35.0    NaN  Married
# 7   arjun  42.0    Hyd   Single
# 8   divya  26.0    Bng  Married
# 9   vijay  33.0    Mum   Single

##SQL
from sqlalchemy import create_engine, text
df=pd.DataFrame(data)
# 'databse_name+driver_name//user/pass@host:port/schema_name'
engine = create_engine(
    # Password contained an extra '@' which caused the connection string to have two '@' signs.
    # Remove the extra '@' so there is only one separator before the host.
    'mysql+pymysql://root:R76s85l04u13%40@localhost:30000/alchemy'
)
with engine.begin() as conn:
    conn.execute(text("DROP TABLE IF EXISTS Student"))

df.to_sql(
    name='Student',
    con=engine,
    index=False,
    if_exists='append'
)

query="SELECT * FROM STUDENT"
sql_data=pd.read_sql(query, engine)
print(sql_data)
#      name  Ages Places   Status
# 0     sai  27.0    Hyd  Married
# 1  lalith  37.0    Bng  Married
# 2    syam  47.0    Chn     None
# 3     ram  23.0   None   Single
# 4    None   NaN    Del  Married
# 5   priya  29.0    Kol   Single
# 6   kiran  35.0   None  Married
# 7   arjun  42.0    Hyd   Single
# 8   divya  26.0    Bng  Married
# 9   vijay  33.0    Mum   Single

## JSON --> javascript object notation
df.to_json('python/day62_new.json', orient='records',indent=4)
json_data=pd.read_json('python/day62_new.json')
print(json_data)
#      name  Ages Places   Status
# 0     sai  27.0    Hyd  Married
# 1  lalith  37.0    Bng  Married
# 2    syam  47.0    Chn     None
# 3     ram  23.0   None   Single
# 4    None   NaN    Del  Married
# 5   priya  29.0    Kol   Single
# 6   kiran  35.0   None  Married
# 7   arjun  42.0    Hyd   Single
# 8   divya  26.0    Bng  Married
# 9   vijay  33.0    Mum   Single

