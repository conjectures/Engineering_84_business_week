# Python: Using SQL

We use the pyodbc library to connect to an AWS hosted database that is using the SQL Server DBMS by Microsoft.
The DB is running the Northwind example dataset for testing purposes.

![Python-AWS-DB connection](python-db-aws.png)

## Establishing connection with `pyodbc`
```python
# define connection credentials
server = [database-location or ip]
database = [database name]
username = [username]
password = [password]
db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
```
When establishing connection with SQL Server on ubuntu, the following dependencies may be required:
- `unixodbc-dev`
- [msodbcsql17 driver](https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/m/msodbcsql17/)

The `unixodbc-dev` dependency can be installed with `apt`:
```
sudo apt update
sudo apt install unixodbc-dev
sudo apt upgrade
```
### Testing connection
To test the connection with the database, we execute a query asking for the database version
```python
cursor = NorthwindDB.cursor()
cursor.execute("SELECT @@version;")
```


### Fetching data
After executing a query, we can eiter fetch all the data, or fetch one with the `fetchall` and `fetchone` methods accordingly.
Examples:
```python
# We use execute to run our queries with a string
customer_rows = cursor.execute("SELECT * FROM Customers").fetchall()
print(customer_rows)


# We can also iterate through the data records:
while True:
    # As long as there is data availabel, keep runnign
    record = product_rows.fetchone()
    # If there is no more data, then stop.
    if record is None:
        break
    print(record.UnitPrice)
```
To close the establish connection, we can use the `close` keyword:
```python
NorthwidnDB.close()
```

## Applying CRUD

## Making data persistent

