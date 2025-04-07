import pymysql as mq

mysql=mq.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="PYSQL1"
)
                            #1
# mycursor=mysql.cursor()
# print("{:<20} {:<30} {:<15} {:<30}".format("Student id",
#                                             "Student Name",
#                                             "Student class",
#                                             "Student email"))
# try:
#     sql="select * From student"
#     mycursor.execute(sql)
#     sdata=mycursor.fetchall()
#     for s in sdata:
#         # print(s)
#         print("{:<20} {:<30} {:<15} {:<30}".format(s[0],s[1],s[2],s[3]))
# except:
#     print("Error...!")

                            #2
# mycursor=mysql.cursor()
# print("{:<20} {:<30}".format("Student id","Student Name"))

# try:
#     sql="select st_id,st_name From student"
#     mycursor.execute(sql)
#     sdata=mycursor.fetchall()
#     for s in sdata:
#         # print(s)
#         print("{:<20} {:<30} ".format(s[0],s[1]))
# except:
#     print("Error...!")