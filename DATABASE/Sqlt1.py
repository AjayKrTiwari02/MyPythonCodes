import sqlite3

# con=sqlite3.connect("sq1.db")
# con.execute(''' create table student(
#             st_id INTEGER AUTO_INCREMENT PRIMARY KEY,
#             st_name varchar(50),
#             st_class varchar(10),
#             st_email varchar(30)
# ) 
# ''')
# con.close()

# INSERT DATA:

# con=sqlite3.connect("sq1.db")
# ins=  """insert into student1 
#         (st_id,st_name,st_class,st_email)values 
#        (7,'Avijit kumar','12th','Avi@gmail.com')
#                     """
# con.execute(ins)
# con.commit()
# con.close()
# print("Data inserted successfully")

# FETCHING DATA
# conn=sqlite3.connect("sq1.db")
# # data=conn.execute("select* from student1")
# data=conn.execute("select* from student limit 0,2")     #position,number of column
# for n in data:
# #     print(n)
#     print(n[0],"   ",n[1],"   ",n[2],"   ",n[3])



# con=sqlite3.connect("sq1.db")
# con.execute(''' create table fees(
#             fees_id  int not null,
#             st_id int Not null ,
#             st_fees int,
#             foreign key (st_id)
#             references student1 (st_id)
          
# ) 
# ''')

# con=sqlite3.connect("sq1.db")
# ins=  """insert into fees 
#         (fees_id,st_id,st_fees)values 
#        (105,5,3200)
#                     """
# con.execute(ins)
# con.commit()
# con.close()
# print("Data inserted successfully")
# con.close()