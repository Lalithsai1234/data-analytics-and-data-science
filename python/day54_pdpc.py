import mysql.connector
# try:
#     con=None
#     csr=None
#     con=mysql.connector.connect(
#         user='root',
#         password='R76s85l04u13@',
#         database='pdpc',
#         host='localhost',
#         port='30000'
#     )

#     csr=con.cursor()
#     Query="""Insert into Employee values(1, "sai"),(2,"Lalith"); """
#     csr.execute(Query)
#     con.commit()
# except Exception as e:
#     print(e)
# finally:
#     if con!=None and csr!=None:
#         csr.close()
#         con.close()

# try:
#     con=None
#     csr=None
#     con=mysql.connector.connect(
#         user='root',
#         password='R76s85l04u13@',
#         database='pdpc',
#         host='localhost',
#         port='30000'
#     )

#     csr=con.cursor()
#     Query="""Insert into Employee values(%s, %s); """ #we can also write {id},{name} but we need to assign id and name above 
#     id=int(input("Enter the Id:"))
#     name=input("Enter the Name:")
#     csr.execute(Query,(id,name)) #their should be a comma in between Query and Brackets
#     con.commit()
# except Exception as e:
#     print(e)
# finally:
#     if con!=None and csr!=None:
#         csr.close()
#         con.close()


# try:
#     con=None
#     csr=None
#     con=mysql.connector.connect(
#         user='root',
#         password='R76s85l04u13@',
#         database='pdpc',
#         host='localhost',
#         port='30000'
#     )

#     csr=con.cursor()
#     Query="""Insert into Employee values(%s, %s); """ #we can also write {id},{name} but we need to assign id and name above 
#     data=[(4,'syam'), (5,'loki')]
#     csr.executemany(Query,data) #their should be a comma in between Query and Brackets
#     con.commit()
# except Exception as e:
#     print(e)
# finally:
#     if con!=None and csr!=None:
#         csr.close()
#         con.close()

try:
    con=None
    csr=None
    con=mysql.connector.connect(
        user='root',
        password='R76s85l04u13@',
        database='pdpc',
        host='localhost',
        port='30000'
    )

    csr=con.cursor()
    Query="""select * from employee """ #Query="""select * from employee where emp_id=%s """
    csr.execute(Query)                  #csr.execute(Query,(4,)) if need to be a tuple we should add , after that
    row=csr.fetchone() #to fetch only one row from the list of tuples
    print(row)
    row=csr.fetchmany(2) #we can specify how many rows we want  
    print(row)  
    row=csr.fetchall() #either we need to do the fetch all are limit bcz if we close csr before fetching all the data it have it gives the error
    print(row)
    con.commit()
except Exception as e:
    con.rollback() #if any Query will not give an exception the whole transaction should be roll-backed
    print(e)
finally:
    if con!=None and csr!=None:
        csr.close()
        con.close()

