import pymysql as mq

mysql=mq.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="PYSQL1"
)
# mycursor=mysql.cursor()
# print("{:<20} {:<30} {:<15} {:<30}".format("Student id",
#                                             "Student Name",
#                                             "Student class",
#                                             "Student email"))
# try:
#     sql="select * From student order by st_id Desc" #DESC= Descending 
#     mycursor.execute(sql)                             #Asc =Ascending
#     sdata=mycursor.fetchall()
#     for s in sdata:
#         print("{:<20} {:<30} {:<15} {:<30}".format(s[0],s[1],s[2],s[3]))
# except:
#     print("Error...!")

# LIMIT:

# mycursor=mysql.cursor()
# print("{:<20} {:<30} {:<15} {:<30}".format("Student id",
#                                             "Student Name",
#                                             "Student email",
#                                             "Student class"))
# try:
#     sql="select * From student order by st_id ASC LIMIT 0,3" #if 2,2 means (3rd & 4th)value
#     mycursor.execute(sql)                           
#     sdata=mycursor.fetchall()
#     for s in sdata:
#         print("{:<20} {:<30} {:<15} {:<30}".format(s[0],s[1],s[2],s[3]))
# except:
#     print("Error...!")
