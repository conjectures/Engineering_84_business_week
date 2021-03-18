USE NORTHWIND

-- 1.1 - Customers in Paris or London
SELECT Customers.CustomerID, Customers.CompanyName, CONCAT(Customers.Address, ' ', Customers.PostalCode, ', ', Customers.Region, ', ', Customers.City)
    FROM Customers WHERE Customers.City IN ('London', 'Paris');

--1.2 - Products in bottles
SELECT * FROM Products WHERE Products.QuantityPerUnit LIKE '%bottle%';

--1.3 Include Supplier name and country
SELECT pr.SupplierID, sp.CompanyName, sp.Country, pr.ProductID, pr.ProductName, pr.QuantityPerUnit 
    FROM Products as pr
    INNER JOIN Suppliers as sp ON pr.SupplierID = sp.SupplierID
    WHERE pr.QuantityPerUnit LIKE '%bottle%';


--1.4 - 
SELECT prod.CategoryID, cat.CategoryName, COUNT(*) AS "Item Number" 
    FROM Products as prod 
    INNER JOIN Categories AS cat on prod.CategoryID = cat.CategoryID
    GROUP BY prod.CategoryID, cat.CategoryName
    ORDER BY COUNT(*) DESC;
    
--1.5
SELECT CONCAT(Employees.TitleOfCourtesy, ' ', Employees.FirstName, ' ', Employees.LastName) AS "Employee Name", Employees.City From Employees WHERE Employees.Country = 'UK';


--1.6 List sales totals for all sales regions (via territories table using 4 joins) with sales total greatern than 1Mil. Round or format to present numbers
SELECT rg.RegionID, rg.RegionDescription, FORMAT(ROUND(SUM(odt.Quantity * odt.UnitPrice * (1-odt.Discount)),-5), '###,###,###') as "Total Sales (Approx.)"
    FROM Region as rg
    INNER JOIN Territories as tr on rg.RegionID = tr.RegionID
    INNER JOIN EmployeeTerritories as emt on tr.TerritoryID = emt.TerritoryID
    INNER JOIN Orders as ord on emt.EmployeeID = ord.EmployeeID
    INNER JOIN [Order Details] as odt on ord.OrderID = odt.OrderID
    GROUP BY rg.RegionID, rg.RegionDescription
    HAVING SUM(odt.Quantity * odt.UnitPrice * (1-odt.Discount)) > 1000000;


--1.7 Count orders with freight amount > 100 with USA or UK as destination.
SELECT COUNT(*) AS "Orders with Freight above 100 and destination US or UK" 
    FROM Orders
    WHERE Orders.Freight > 100 AND Orders.ShipCountry IN ('UK', 'USA');

--1.8 Identify Order Number of order with highest amount(value) of discount applied.
--SELECT odt.ProductID,  (prods * odt.Discount) AS "Total discount value" FROM [Order Details] as odt
-- ignore product id

SELECT top 1 *, (odt.UnitPrice*odt.Quantity*odt.Discount) AS "Discount Applied" FROM [Order Details] odt ORDER BY "Discount Applied" DESC

