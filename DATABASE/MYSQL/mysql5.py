# UPDATE:
import pymysql as mq 

mysql=mq.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="PYSQL1"
)
cursorobj=mysql.cursor()

st_name=input("Enter the name:- ")
st_class=input("Enter the class name:-")
st_email=input("Enter the emial:-")
st_id=input("Enter The student Id:-")


sql="UPDATE student set st_name=%s,st_class=%s,st_email=%s where st_id=%s"
data=(st_name,st_class,st_email,st_id)
try:
    cursorobj.execute(sql,data)
    mysql.commit()
    print("Data  updated successfully.....!")
except:
    print("Error...!")