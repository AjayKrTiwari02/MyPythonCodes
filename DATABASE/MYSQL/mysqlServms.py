import pyodbc


conn = pyodbc.connect(
    "Driver={SQL SERVER};"
    "Server=LAPTOP-PEG0H2VQ;"
    "Database=Jan;"
    "Trusted_Connection=yes;"
)


cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE products10 (
    product_id int primary key,
    product_name nvarchar(50),
    price int
    )
    """
)

conn.commit()

# python -m pip install pyodbc