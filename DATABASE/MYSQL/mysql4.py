#DELETE:
import pymysql as mq 

mysql=mq.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="PYSQL1"
)
cursorobj=mysql.cursor()

st_id=input("Enter The student Id: ")

sql="Delete From student where st_id=%s"
try:
    cursorobj.execute(sql,st_id)
    mysql.commit()
    print("Data  Deleted successfully.....!")
except:
    print("Error...!")
