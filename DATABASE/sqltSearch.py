import sqlite3

conn=sqlite3.connect("sqlite.db")

data=conn.execute("truncate table student")
conn.commit()
conn.close()
print("Data Truncate Successfully...!")