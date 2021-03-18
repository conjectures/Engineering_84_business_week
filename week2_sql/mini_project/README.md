# Mini Project

## Part 1

> 1.1 Write a query that lists all Customers in either Paris or London. Include Customer ID, Company Name and all address fields. 

*Strategy: List all customers and filter them with a subquery based on their city*

```SQL
SELECT Customers.CustomerID, Customers.CompanyName, CONCAT(Customers.Address, ' ', Customers.PostalCode, ', ', Customers.Region, ', ', Customers.City)
    FROM Customers WHERE Customers.City IN ('London', 'Paris');
```

<br>

> 1.2 List all products stored in bottles.

*Strategy: Use a regular expression to find the products that contain the pattern 'bottle' in their quantity*

```SQL
SELECT * FROM Products WHERE Products.QuantityPerUnit LIKE '%bottle%';
```
<br>

> 1.3 Repeat question above, but add in the Supplier Name and Country.

*Strategy: Supplier Name and Country are not included in the Products Table, therefore an inner join is needed with the Suppliers Table.*

```SQL
SELECT pr.SupplierID, sp.CompanyName, sp.Country, pr.ProductID, pr.ProductName, pr.QuantityPerUnit
    FROM Products as pr
    INNER JOIN Suppliers as sp ON pr.SupplierID = sp.SupplierID
    WHERE pr.QuantityPerUnit LIKE '%bottle%';
```

<br>

> 1.4 Write an SQL Statement that shows how many products there are in each category. Include Category Name in result set and list the highest number first. 

*Strategy:*

```SQL
```
<br>

> 1.5 List all UK employees using concatenation to join their title of courtesy, first name and last name together. Also include their city of residence. 

*Strategy:*

```SQL
```
<br>

>

List Sales Totals for all Sales Regions (via the Territories table using 4 joins) with a Sales Total greater than 1,000,000. Use rounding or FORMAT to present the numbers.  

Count how many Orders have a Freight amount greater than 100.00 and either USA or UK as Ship Country. 

Write an SQL Statement to identify the Order Number of the Order with the highest amount(value) of discount applied to that order.
