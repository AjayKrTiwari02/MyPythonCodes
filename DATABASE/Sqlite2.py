import sqlite3

conn=sqlite3.connect("sq1.db")
# # data=conn.execute("select* from student")
# # data=conn.execute("select* from student limit 0,2")     #position,number of column
# for n in data:
#     # print(n)
#     print(n[0],"   ",n[1],"   ",n[2],"   ",n[3])
# print("------------------------------------------------")

# data=conn.execute("select * from student where st_id=5")
# for n in data:
#     print(n[0],"   ",n[1],"   ",n[2],"   ",n[3])

# print("------------------------------------------------")

# st_name=input("Enter the name:-")
# st_class=input("Enter the class:-")

# # data=conn.execute("select * from student where st_name like '%"+st_name+"%'")
# data=conn.execute("select * from student where st_name like '%"+st_name+"%'or st_class='"+st_class+"'  ")
# for n in data:
#     print(n[0],"   ",n[1],"   ",n[2],"   ",n[3])