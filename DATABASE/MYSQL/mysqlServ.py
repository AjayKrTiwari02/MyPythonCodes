import pypyodbc as odbc  #pip install pypyodbc 

Driver_name="SQL SERVER"
SERVER_NAME="LAPTOP-PEG0H2VQ"
DATABASE_NAME="Jan"

# uid=<username
# pwd=<password
connection_string=f"""
    Driver={Driver_name};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    Trust_Connection=yes;  
"""

conn=odbc.connect(connection_string)

# print(conn)
# print("Database Created successfully...!")


cursor = conn.cursor()
cursor.execute(
  """
  CREATE TABLE Persons
  (
  P_Id int,
  LastName varchar(255),
  FirstName varchar(255),
  Address varchar(255),
  City varchar(255)
  )
  """
)
cursor.close()
conn.close()