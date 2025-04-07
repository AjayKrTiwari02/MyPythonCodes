
# pip install mysqlx-connector-python
import mysql.connector


connection=mysql.connector.connect( 
    host="localhost",
    user="root",
    passwd="password",
    database="pymysql1")


if connection.is_connected():
    db_Info=connection.get_server_info()
    print("My DB Sever Version",db_Info)
    cursor=connection.cursor()
    cursor.execute("select database();")
    record=cursor.fetchone()
    print("Connected to database:",record)

cursor.callproc('My_emp_Records') 

# for result in cursor.stored_results():
#     print(result.fetchall())

# for result in cursor.stored_results():
#     rlist=result.fetchall()
#     for row in rlist:
#         print(row)

# for result in cursor.stored_results():
#     rlist=result.fetchall()
#     for row in rlist:
#         cols=row
#         for c in cols:
#             print(c)
#         print("****************************************")



#arguments
# cursor.callproc('new_procedure',[1003,]) 
# for result in cursor.stored_results():
#     rlist=result.fetchall()
#     for row in rlist:
#         cols=row
#         for c in cols:
#             print(c)

