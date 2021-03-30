# SQL OOP
> Time: 25 - 30'

## Task: OOP example using pyodbc

- Create an example service object related to a particular table.

- An sql manager for the products table:
  Create an object that relates only to the `products` prepended with your name table (i.e. `alexis_products`) in the Northwind database. 
  The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defined as a 'business function'.
  As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department.
  The stock department may have numerous requirements and it makes sense to contain all the requirements as code actions within a single object.

## Steps:
- Create two files `nw_products.py` and `nw_runner.py` 
- Creating object that handles the functionality.

*Note: APPLY OOP - DRY CRUD where possible*

