#Sqlite -join:-
# inner join:-returns all records that have matching values in both table .
# left(outer)join:-Returns all record from left table & the matched record from the right table.
# right(outer)join:-Returns all record from right table & the matched record from the left table.
# full(outer)join:Returns all the records when there is a match in either left or right table .

import sqlite3

# conn=sqlite3.connect("sqlt4.db")
# print("st_id ","st_name ","st_fees")

# data=conn.execute("select * from fees as f inner join student as s on f.st_id=s.st_id")
# for a in data:
#     print(a)
# conn.close()

#2nd:

# conn=sqlite3.connect("sqlt4.db")
# print("st_id ","st_name ","st_fees")

# data=conn.execute("select f.st_id ,s.st_name ,f.st_fees from fees as f inner join student as s on f.st_id=s.st_id")
# for a in data:
#     # print(a)
#     print(a[0],a[1],a[2])
# conn.close()

# left join:

# conn=sqlite3.connect("sqlt4.db")
# print("st_id ","st_name ","st_fees")

# data=conn.execute("select f.st_id ,s.st_name ,f.st_fees from fees as f left join student as s on f.st_id=s.st_id")
# for a in data:
#     # print(a)
#     print(a[0],a[1],a[2])
# conn.close()

# right join:

# conn=sqlite3.connect("sqlt4.db")
# print("st_id ","st_name ","st_fees")

# data=conn.execute("select f.st_id ,s.st_name ,f.st_fees from fees as f right join student as s on f.st_id=s.st_id")
# for a in data:
#     # print(a)
#     print(a[0],a[1],a[2])
# conn.close()

# full join

# conn=sqlite3.connect("sqlt4.db")
# print("full join:")
# print("st_id "," ","st_name "," ","st_fees")

# data=conn.execute("select f.st_id ,s.st_name ,f.st_fees from fees as f full join student as s on f.st_id=s.st_id")
# for a in data:
#     # print(a)
#     print(a[0]," ",a[1]," ",a[2])
# conn.close()