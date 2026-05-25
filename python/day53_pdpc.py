"""
1) install mysql driver(if oracle oracle driver)
2) create or establish the connection
3) create Cursor(Workspace)
4) Execute the Query
5) To save Changes we use Commit()
6) close()


pip --> package installer for python
ex: pip install mysql-connector-python
"""
#import mysql driver
import mysql.connector

#create the connection
con=mysql.connector.connect(
    user='root',
    password='R76s85l04u13@',
    database='pdpc',
    host='localhost',
    port='30000'
)

#create Cursor
csr=con.cursor()

#Execute the Query
Query=  """Create Table IF NOT EXISTS Employee(emp_id int, emp_name varchar(50));"""
csr.execute(Query) 

#commit the changes
con.commit()

#Close the files to prevent leakage
csr.close()
con.close()
 