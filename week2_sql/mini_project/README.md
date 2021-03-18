# Mini Project

## Part 1

> 1.1 Write a query that lists all Customers in either Paris or London. Include Customer ID, Company Name and all address fields. 

*Strategy: List all customers and filter them with a subquery based on their city*

```SQL
SELECT Customers.CustomerID, Customers.CompanyName, CONCAT(Customers.Address, ' ', Customers.PostalCode, ', ', Customers.Region, ', ', Customers.City)
    FROM Customers WHERE Customers.City IN ('London', 'Paris');
```

> 1.2 List all products stored in bottles.

* Strategy: Use a regular expression to find the products that contain the pattern 'bottle' in their quantity*

```SQL
SELECT * FROM Products WHERE Products.QuantityPerUnit LIKE '%bottle%';
```

> 1.3
