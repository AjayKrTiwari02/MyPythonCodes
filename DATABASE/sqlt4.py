import sqlite3

conn=sqlite3.connect("sqlt4.db")
# st_id=input("Enter the student id you want to Delete")
data=conn.execute("update student set st_name='Somya Roy' where st_id=5")
conn.commit()
conn.close()
print("Data Updated Successfully...!")