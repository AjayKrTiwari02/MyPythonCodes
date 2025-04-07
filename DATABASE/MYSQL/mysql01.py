import pymysql as mq

mysql=mq.connect(
    host="localhost",
    user="root",
    passwd="password"
)
mycursor=mysql.cursor()
mycursor.execute("create DATABASE PYSQL1 ")
# mycursor.execute("use PYSQL1 ")
print("Database Created successfully...!")



#table student(st_id,st_name,st_class ,st_email)
# pip install mysql-connector-python

