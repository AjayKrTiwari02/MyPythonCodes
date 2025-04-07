import  pymysql as mq

conn=mq.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="PYSQL1"
)
# table student(st_id,st_name,st_class ,st_email)

                            #1
# mysqlc=conn.cursor()
# try:
#     ins="INSERT  INTO student(st_name,st_class,st_email) values (%s,%s,%s)"
#     t=('Sumit Roy','1oth','sumit06@gmail.com')
#     mysqlc.execute(ins,t)
#     conn.commit();
#     print("Data inserted successfully....!")
# except:
#     print("Error....!")

                            #2

# #MULTIPLE DATA :

# mysqlc=conn.cursor()
# try:
#     ins="INSERT  INTO student(st_name,st_class,st_email) values (%s,%s,%s)"
#     t=[('Amit Das','12th','amitdas12@gmail.com'),
#        ('Souvanik Sarkar','10th','souvonik11@gmail.com'),
#        ('Anurag Biswas','12th','anurag12@gmail.com'),
#        ('Soumyajit Roy','10th','soumya1@gmail.com'),
#         ('Randeep Singh','12th','randeep111@gmail.com')]
#     mysqlc.executemany(ins,t)
#     conn.commit();
#     print("Data inserted successfully....!")
# except Exception as e:
#     print("Error....!",e)
