# sql join:
# 1.Inner join
# 2.left join
# 3.right join
# 4.eque join

import  pymysql as mq

conn=mq.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="PYSQL1"
)
# mysqlc=conn.cursor()
# tc="""create table fees(
#     s_id int auto_increment,
#     sfees_id int not null,
#     s_fees int not null,
#     primary key(s_id)
     
#     )"""
# mysqlc.execute(tc)
                        ##insert table
# mysqlc=conn.cursor()
# try:
#     ins="INSERT  INTO fees(sfees_id,s_fees) values (%s,%s)"
#     t=(106,7600)
#     mysqlc.execute(ins,t)
#     conn.commit();
#     print("Data inserted successfully....!")
# except:
#     print("Error....!")

# INNER JOIN:

# mycursor=conn.cursor()
# print("{:<20} {:<30} {:<15} {:<30}".format("Student id",
#                                             "Student Name",
#                                             "Student fees",
#                                             "Student class"))
# try:
#     sql="select f.s_id ,s.st_name ,f.s_fees,s.st_class from fees as f inner join student as s on f.s_id=s.st_id"
#     mycursor.execute(sql)
#     sdata=mycursor.fetchall()
#     for s in sdata:
#         # print(s)
#         print("{:<20} {:<30} {:<15} {:<30} ".format(s[0],s[1],s[2],s[3]))
# except:
#     print("Error...!")

#lEFT JOIN:

# mycursor=conn.cursor()
# print("{:<20} {:<30} {:<15} ".format("Student id",
#                                             "Student Name",
#                                             "Student fees",
#                                             ))
# try:
#     sql="select f.s_id ,s.st_name ,f.s_fees from fees as f left join student as s on f.s_id=s.st_id"
#     mycursor.execute(sql)
#     sdata=mycursor.fetchall()
#     for s in sdata:
#         # print(s)
#         print("{:<20} {:<30} {:<15} ".format(s[0],s[1],s[2]))
# except:
#     print("Error...!")

#RIGHT JOIN
# mycursor=conn.cursor()
# print("{:<20} {:<30} {:<15} ".format("Student id",
#                                             "Student Name",
#                                             "Student fees",
#                                             ))
# try:
#     sql="select f.s_id ,s.st_name ,f.s_fees from fees as f right join student as s on f.s_id=s.st_id"
#     mycursor.execute(sql)
#     sdata=mycursor.fetchall()
#     for s in sdata:
#         # print(s)
#         print("{:<20} {:<30} {:<15} ".format(s[0],s[1],s[2]))
# except Exception as e :
#     print("Error...!:-",e)

#Eque join:
# mycursor=conn.cursor()
# print("{:<20} {:<30} {:<15} {:<20} {:<30} {:<15} {:<20}  ".format("Student id",
#                                                                   "Student Name",
#                                                               "Student email",
#                                                                "Student class",
#                                                                "Sudetnt id",
#                                                                "Student feesid",
#                                                                "Student fees"

#                                                                     ))
# try:
#     sql="select * from student,fees where student.st_id=fees.s_id"
    
#     mycursor.execute(sql)
#     sdata=mycursor.fetchall()
#     for s in sdata:
#         # print(s)
#         print("{:<20} {:<30} {:<15} {:<20} {:<30} {:<15} {:<20}  ".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))
# except:
#     print("Error...!")