-- SQL Mini Project PART 3
-- Alexis Othonos

USE NORTHWIND

-- 3.1 List all employees and who they report to. Mention Employee names and report to names
SELECT CONCAT(emp.TitleOfCourtesy, ' ', emp.FirstName, ' ', emp.LastName) AS "Employee", CONCAT(man.TitleOfCourtesy, ' ', man.FirstName, ' ', man.LastName) AS "Manager"
    FROM Employees as emp
    LEFT JOIN Employees as man ON emp.ReportsTo = man.EmployeeID 

-- 3.2 List suppliers with total sales over 10k in Order Details table. Include company name (from Suppliers) 
SELECT prd.SupplierID, Suppliers.CompanyName, FORMAT(SUM(odt.Quantity*odt.UnitPrice), '###,###,###')
    FROM [Order Details] as odt
    INNER JOIN Products as prd ON odt.ProductID = prd.ProductID
    INNER JOIN Suppliers ON prd.SupplierID = Suppliers.SupplierID
    GROUP BY prd.SupplierID, Suppliers.CompanyName
    HAVING SUM(odt.Quantity*odt.UnitPrice) > 10000
    ORDER BY SUM(odt.Quantity*odt.UnitPrice)

-- 3.3 List top 10 customers YTD for latest year in order file (based on total value of orders shipped)
-- Assume it is 1998
SELECT TOP 10 Customers.CustomerID, Customers.ContactName, SUM(odt.UnitPrice*odt.Quantity) AS "Value of Orders"
    FROM Orders
    INNER JOIN Customers On Orders.CustomerID = Customers.CustomerID
    INNER JOIN [Order Details] as odt ON Orders.OrderID = odt.OrderID
    WHERE Orders.OrderDate >= '19980101'
    GROUP BY Customers.CustomerID, Customers.ContactName
    ORDER BY SUM(odt.UnitPrice*odt.Quantity) DESC

-- 3.4 Plot average ship time by month for all data in Orders
SELECT DATEPART(MONTH, Orders.ShippedDate)
    FROM Orders
    GROUP BY DATEPART(MONTH, Orders.ShippedDate) 

-- iter 2: change month to mmYY date
SELECT DATEPART(MONTH, Orders.OrderDate) AS "Shipment month", AVG(DATEDIFF(d, Orders.OrderDate, Orders.ShippedDate)) AS "Days to Ship"
    FROM Orders
    GROUP BY DATEPART(MONTH, Orders.OrderDate)
    ORDER BY DATEPART(MONTH, Orders.OrderDate)

-- iter 3
SELECT CONCAT(YEAR(Orders.OrderDate), MONTH(Orders.OrderDate)) AS "Shipment month", AVG(DATEDIFF(d, Orders.OrderDate, Orders.ShippedDate)) AS "Days to Ship"
    FROM Orders
    GROUP BY CONCAT(YEAR(Orders.OrderDate), MONTH(Orders.OrderDate))
    ORDER BY CONCAT(YEAR(Orders.OrderDate), MONTH(Orders.OrderDate))

--iter 4 - improve format
SELECT FORMAT(Orders.OrderDate, 'MM-yy') AS "Shipment month", AVG(DATEDIFF(d, Orders.OrderDate, Orders.ShippedDate)) AS "Days to Ship"
    FROM Orders
    GROUP BY FORMAT(Orders.OrderDate, 'MM-yy')
    ORDER BY FORMAT(Orders.OrderDate, 'MM-yy') 
