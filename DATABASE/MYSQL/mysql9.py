import pymysql as mq 

# mysql=mq.connect(
#     host="localhost",
#     user="root",
#     passwd="password",
#     database="PYSQL1"
# )
# cursorobj=mysql.cursor()

# try:
#     cursorobj.execute("truncate  table fees")
#     mysql.commit()
#     print("Data  truncated successfully.....!")
# except:
#     print("Error...!")

## Drop
mysql=mq.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="PYSQL1"
)
cursorobj=mysql.cursor()
try:
    # cursorobj.execute("Drop  table student")
    cursorobj.execute("Drop  database pysql1")
    mysql.commit()
    # print("table  droped successfully.....!")
    print("Database  droped successfully.....!")
except:
    print("Error...!")