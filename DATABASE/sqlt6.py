
import sqlite3


conn = sqlite3.connect('sqlt4.db')
cursor = conn.cursor()

# table ="""CREATE TABLE EMPLOYEE(FIRST_NAME VARCHAR(255),
# LAST_NAME VARCHAR(255),AGE int, SEX VARCHAR(255), INCOME int);"""
# cursor.execute(table)

# cursor.execute(
# 	'''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
# 	VALUES ('Anand', 'Choubey', 25, 'M', 10000)''')
# cursor.execute(
# 	'''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
# 	VALUES ('Mukesh', 'Sharma', 20, 'M', 9000)''')
# cursor.execute(
# 	'''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
# 	VALUES ('Ankit', 'Pandey', 24, 'M', 6300)''')

# cursor.execute(
# 	'''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
# 	VALUES ('Subhdra ', 'Singh', 26, 'F', 8000)''')

# cursor.execute(
# 	'''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
# 	VALUES ('Tanu', 'Mishra', 24, 'F', 6500)''')


# print("EMPLOYEE Table: ")
# data = cursor.execute('''SELECT * FROM EMPLOYEE''')
# for row in data:
# 	print(row)

# # Updating:

# cursor.execute('''UPDATE EMPLOYEE SET INCOME = 5000 WHERE Age<25;''')
# print('\nAfter Updating...\n')


# print("EMPLOYEE Table: ")
# data = cursor.execute('''SELECT * FROM EMPLOYEE''')
# for row in data:
# 	print(row)


# conn.commit()
# conn.close()
