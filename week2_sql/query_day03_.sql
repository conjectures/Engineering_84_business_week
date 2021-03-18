USE Northwind

SELECT SUM(UnitsOnOrder) AS "Total On Order",
    AVG(UnitsOnOrder) AS "Avg On Order",
    MIN(UnitsOnOrder) AS "Min On Order",
    MAX(UnitsOnOrder) AS "Max On Order"
    FROM Products;


-- Data per supplier ID
SELECT SupplierID, AVG(UnitsOnOrder) AS "Avg On Order", SUM(UnitsOnOrder) AS "Total on Order", MAX(UnitsOnOrder) AS "Max On Order"
    FROM Products
    GROUP BY SupplierID;


--------------------------------------------------------------------
-- Activity 1
SELECT Products.CategoryID, AVG(Products.ReorderLevel) AS "Average Reorder Level" FROM Products GROUP BY Products.CategoryID, Products.CategoryID ORDER BY AVG(Products.ReorderLevel) DESC;

SELECT Products.SupplierID, SUM(Products.UnitPrice) AS "Total On Order",
    AVG(Products.UnitsOnOrder) AS "Avg On Order"
    FROM Products
    GROUP BY Products.SupplierID
    HAVING AVG(Products.UnitsOnOrder)>1
    ORDER BY SUM(Products.UnitsOnOrder) DESC;
--------------------------------------------------------------------


-- INNER JOIN


--------------------------------------------------------------------
--Activity 2
select * from Products

SELECT Suppliers.CompanyName, AVG(Products.UnitsOnOrder) AS "Average units on order"
    FROM Products
    INNER JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID
    GROUP BY Suppliers.SupplierID, Suppliers.CompanyName
--------------------------------------------------------------------


--------------------------------------------------------------------
-- Activity 3
SELECT Orders.OrderID, Orders.OrderDate, Orders.Freight, Customers.CompanyName, CONCAT(Employees.FirstName, ' ', Employees.LastName) AS "Employee Full Name" FROM Orders
    INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
    INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID;
--------------------------------------------------------------------


-- CONVERT - FORMAT
SELECT Orders.OrderID, CONVERT(VARCHAR(10), Orders.OrderDate, 103) AS [dd/MM/yyy]
    FROM Orders; /* Before 2012 */

SELECT Orders.OrderID, FORMAT(Orders.OrderDate, 'dd/MM/yyyy')
    FROM Orders;


-- SUBQUERIES
SELECT Customers.CompanyName AS "Customer"
    FROM Customers
    WHERE CustomerID NOT IN (SELECT Orders.CustomerID FROM Orders);

-- Same query with joins:
SELECT Customers.CompanyName AS "Customer"
    FROM Customers
    LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    WHERE Orders.OrderID is NULL

-- SUBQUERY BROADCASTING (?)
SELECT odt.OrderID, odt.ProductID, odt.UnitPrice, odt.Quantity, odt.Discount,
    (SELECT MAX([Order Details].UnitPrice) FROM [Order Details]) AS "Max Price"
    FROM [Order Details] as odt


SELECT od.ProductID, sq1.totalamnt AS "Total Sold for this Product", UnitPrice, (UnitPrice/totalamnt)*100 AS "% of Total"
    FROM [Order Details] od 
    INNER JOIN
        (SELECT ProductID, SUM(UnitPrice*Quantity) AS totalamnt FROM [Order Details]
        GROUP BY ProductID) sq1 ON sq1.ProductID = od.ProductID


SELECT  SUM((UnitPrice/totalamnt)*100 )AS "% of Total"
    FROM [Order Details] od 
    INNER JOIN
        (SELECT ProductID, SUM(UnitPrice*Quantity) AS totalamnt FROM [Order Details]
        GROUP BY ProductID) sq1 ON sq1.ProductID = od.ProductID


--------------------------------------------------------------------
-- Activity 4
SELECT odt.OrderID, odt.ProductID, odt.UnitPrice, odt.Quantity, odt.Discount FROM [Order Details] as odt
    WHERE odt.ProductID IN (SELECT Products.ProductID FROM Products WHERE Products.Discontinued != 0)

SELECT odt.OrderID, odt.ProductID, odt.UnitPrice, odt.Quantity, odt.Discount
    FROM [Order Details] as odt
    INNER JOIN Products ON Products.ProductID = odt.ProductID
    WHERE Products.Discontinued != 0;
--------------------------------------------------------------------

    

-- UNION ALL
SELECT EmployeeID AS " Employee/Supplier"
    FROM Employees
    UNION ALL
    SELECT SupplierID
    FROM Suppliers

-- UNION 
SELECT EmployeeID AS " Employee/Supplier"
    FROM Employees
    UNION
    SELECT SupplierID
    FROM Suppliers
