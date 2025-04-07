import  pymysql as mq

conn=mq.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="pysql1"
)
mysqlc=conn.cursor()
tc="""create table student(
    st_id int primary key auto_increment,
    st_name varchar(30),
    st_class varchar(10),
    st_email varchar(20)
    )"""
mysqlc.execute(tc)
print("Table created Successfully....")




