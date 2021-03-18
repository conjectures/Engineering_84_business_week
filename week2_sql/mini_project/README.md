# Mini Project

## Part 1

> 1.1 Write a query that lists all Customers in either Paris or London. Include Customer ID, Company Name and all address fields. 

*Strategy: List all customers and filter them with a subquery based on their city*

```SQL
SELECT Customers.CustomerID, Customers.CompanyName, CONCAT(Customers.Address, ' ', Customers.PostalCode, ', ', Customers.Region, ', ', Customers.City)
    FROM Customers WHERE Customers.City IN ('London', 'Paris');
```

<br>
<br>

> 1.2 List all products stored in bottles.

*Strategy: Use a regular expression to find the products that contain the pattern 'bottle' in their quantity*

```SQL
SELECT * FROM Products WHERE Products.QuantityPerUnit LIKE '%bottle%';
```
<br>
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
<br>

> 1.4 Write an SQL Statement that shows how many products there are in each category. Include Category Name in result set and list the highest number first. 

*Strategy: Get Category name from Categories Table - join with Products. Then join the products based on their category id*

```SQL
SELECT prod.CategoryID, cat.CategoryName, COUNT(*) AS "Item Number" 
    FROM Products as prod 
    INNER JOIN Categories AS cat on prod.CategoryID = cat.CategoryID
    GROUP BY prod.CategoryID, cat.CategoryName
    ORDER BY COUNT(*) DESC;
```
<br>
<br>

> 1.5 List all UK employees using concatenation to join their title of courtesy, first name and last name together. Also include their city of residence. 

*Strategy: Simple WHERE filtering for Employee Country. Concatenation of Employee name, last name and title between spaces.*

```SQL
SELECT CONCAT(Employees.TitleOfCourtesy, ' ', Employees.FirstName, ' ', Employees.LastName) AS "Employee Name", Employees.City
    FROM Employees
    WHERE Employees.Country = 'UK';
```
<br>
<br>

> 1.6 List Sales Totals for all Sales Regions (via the Territories table using 4 joins) with a Sales Total greater than 1,000,000. Use rounding or FORMAT to present the numbers.  

*Strategy: In this exercise, the NORTHWIND database diagram was used to find the appropriate connection between tables, such that the 4 joints condition is met. 
For the Territories Table to also be included, the connection follows, as seen in the diagram below, starting from the Regions, then Territories, Employee Territories, then Orders and finally [Order Details].
The Employee Table was skipped, as the Employee IDs are included in the Order Table as well. The value of each Region was calculated by taking in account the discount applied as well.*
![NorthWind Diagram](media/database_diagram_ex1p6.jpg)

```SQL
SELECT rg.RegionID, rg.RegionDescription, FORMAT(ROUND(SUM(odt.Quantity * odt.UnitPrice * (1-odt.Discount)),-5), '###,###,###') as "Total Sales (Approx.)"
    FROM Region as rg
    INNER JOIN Territories as tr on rg.RegionID = tr.RegionID
    INNER JOIN EmployeeTerritories as emt on tr.TerritoryID = emt.TerritoryID
    INNER JOIN Orders as ord on emt.EmployeeID = ord.EmployeeID
    INNER JOIN [Order Details] as odt on ord.OrderID = odt.OrderID
    GROUP BY rg.RegionID, rg.RegionDescription
    HAVING SUM(odt.Quantity * odt.UnitPrice * (1-odt.Discount)) > 1000000;
```
<br>
<br>

> 1.7 Count how many Orders have a Freight amount greater than 100.00 and either USA or UK as Ship Country. 

*Strategy: Simple Filtering with two conditions; an inequality condition and a subquery looking for the keywords 'UK' and 'USA' in the Order Countries*

```SQL
SELECT COUNT(*) AS "Orders with Freight above 100 and destination US or UK" 
    FROM Orders
    WHERE Orders.Freight > 100 AND Orders.ShipCountry IN ('UK', 'USA');
```
<br>
<br>


> 1.8 Write an SQL Statement to identify the Order Number of the Order with the highest amount(value) of discount applied to that order.

*Strategy: Initially, the value of the products was taken from the Products Table, however that wasn't helpful as the value of the same products would be different in the [Order Details] Table.
Therefore, only the [Order Details] info is used. The orders are grouped by ID and then sorted with descending order based on the discount that is applied, which is calculated in the select statement. The first 
result is the order with the highest discount applied* 

```SQL
SELECT TOP 1 odt.OrderID, ROUND(SUM(odt.UnitPrice*odt.Quantity*odt.Discount),0) AS "Discount Applied" 
    FROM [Order Details] odt 
    GROUP BY odt.OrderID
    ORDER BY "Discount Applied" DESC
```

