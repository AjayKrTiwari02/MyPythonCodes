#searching & filter:

import pymysql as mq

# mysql=mq.connect(
#     host="localhost",
#     user="root",
#     passwd="password",
#     database="PYSQL1"
# )
# mycursor=mysql.cursor()
# name=input("Enter the Student name:- ")
# print("{:<20} {:<30} {:<15} {:<30}".format("Student id",
#                                             "Student Name",
#                                             "Student email",
#                                             "Student class"))
# try:
#     sql="select * From student where st_name='"+name+"'" 
#     mycursor.execute(sql)                            
#     sdata=mycursor.fetchall()
#     for s in sdata:
#         print("{:<20} {:<30} {:<15} {:<30}".format(s[0],s[1],s[2],s[3]))
# except:
#     print("Error...!")

#### LIKE:
                        ##### single Input
# mysql=mq.connect(
#     host="localhost",
#     user="root",
#     passwd="password",
#     database="PYSQL1"
# )
# mycursor=mysql.cursor()
# name=input("Enter the Student name:- ")
# print("{:<20} {:<30} {:<15} {:<30}".format("Student id",
#                                             "Student Name",
#                                             "Student email",
#                                             "Student class"))
# try:
#     sql="select * From student where st_name like'%"+name+"%'" # surching from both side 
#     mycursor.execute(sql)                            
#     sdata=mycursor.fetchall()
#     for s in sdata:
#         print("{:<20} {:<30} {:<15} {:<30}".format(s[0],s[1],s[2],s[3]))
# except:
#     print("Error...!")

                            ###multiple input

# mysql=mq.connect(
#     host="localhost",
#     user="root",
#     passwd="password",
#     database="PYSQL1"
# )
# mycursor=mysql.cursor()
# name=input("Enter the Student name:- ")
# classname=input("Enter Your class")
# print("{:<20} {:<30} {:<15} {:<30}".format("Student id",
#                                             "Student Name",
#                                             "Student class",
#                                             "Student email"
#                                             ))   #and or 
# try:
#     sql="select * From student where st_name like'%"+name+"%' and st_class like '%"+classname+"%'" 
#     mycursor.execute(sql)                            
#     sdata=mycursor.fetchall()
#     for s in sdata:
#         print("{:<20} {:<30} {:<15} {:<30}".format(s[0],s[1],s[2],s[3]))
# except:
#     print("Error...!")
