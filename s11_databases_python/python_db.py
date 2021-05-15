import pyodbc

# Establish connection between python and sql with pyodbc

# temp
server = "18.135.103.95"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

cursor = docker_Northwind.cursor()
cursor.execute("SELECT @@version;")


row = cursor.fetchone()
print()
print(row)

# Let's connect to our DB and fetch some data from Customers tabel

# We use execute to run our queries with a string
customer_rows = cursor.execute("SELECT * FROM Customers").fetchall()
# print(customer_rows)
# fetchall() gets all the data from the table

product_rows = cursor.execute("SELECT * FROM Products").fetchall()
# Let's iterate through the Product Table and check the UnitPrices available.
# for record in product_rows:
#     print(record.ProductName, record.UnitPrice)

while True:
    # As long as there is data availabel, keep runnign
    record = product_rows.fetchone()
    # If there is no more data, then stop.
    if record is None:
        break
    print(record.UnitPrice)


docker_Northwind.close()
