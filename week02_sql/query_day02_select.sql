USE Northwind

--Table aliasing
SELECT * FROM Employees etable
WHERE etable.City = 'London';


--------------------------------------------
-- EXERCISES PART 1 --
-- Ex 1 - Using aggregate function count and column aliasing
SELECT COUNT(*) AS "Number of Employees living in London" FROM Employees
WHERE Employees.City = 'London';

-- Ex 2 -  Using concatenation
SELECT Employees.TitleOfCourtesy , Employees.FirstName + ' ' + Employees.LastName AS "Employee Name" FROM Employees
WHERE Employees.TitleOfCourtesy = 'Dr.';

-- Ex 3 
--SELECT Products.Discontinued FROM Products;
SELECT COUNT(*) AS "Discontinued Products" FROM Products
WHERE Products.Discontinued = 1
--------------------------------------------


SELECT TOP 5 Customers.CompanyName, Customers.City FROM Customers WHERE Country = 'France';

SELECT Products.ProductName, Products.UnitPrice FROM Products
WHERE Products.CategoryID=1 AND Products.Discontinued = 0;

SELECT Products.ProductName, Products.UnitPrice FROM Products
WHERE Products.UnitsInStock>0 OR Products.UnitPrice > 29.99;

-- Remove duplicates from results
SELECT DISTINCT Customers.Country FROM Customers
WHERE Customers.ContactTitle = 'Owner';

-- WILDCARDS
-- % match 1 or more of any character
SELECT Products.ProductName FROM Products WHERE Products.ProductName LIKE 'A%';
-- set of letters
SELECT Products.ProductName FROM Products WHERE Products.ProductName LIKE '[ACD]%';
-- Dont match set of numbers
SELECT Products.ProductName FROM Products WHERE Products.ProductName LIKE '[^ACD]%';
-- Match one of any character with _
SELECT Products.ProductName FROM Products WHERE Products.ProductName LIKE '_P%';

-- Ise parenthesies to declare priority to conditions
SELECT * FROM Customers WHERE (Customers.Region = 'WA' OR Customers.Region = 'SP') AND Customers.CompanyName LIKE 'G%';
-- IN operator to make statements smaller
SELECT * FROM Customers WHERE Customers.Region IN ('WA','SP') AND Customers.CompanyName LIKE 'G%';

SELECT * FROM EmployeeTerritories WHERE EmployeeTerritories.TerritoryID BETWEEN 06800 AND 09999;


--------------------------------------------
-- EXERCISES PART 2 --
-- Ex 1
SELECT Products.ProductName, Products.ProductID, Products.UnitPrice FROM Products WHERE Products.UnitPrice < 5.00;

-- Ex2 
SELECT * FROM Categories WHERE Categories.CategoryName LIKE '[BS]%'

-- Ex3 
SELECT COUNT(*) AS "Number of orders for Employees 5 and 7" FROM Orders WHERE Orders.EmployeeID IN (5,7);

SELECT * FROM Orders;
--------------------------------------------


-- GROUP BY Clause
SELECT Orders.EmployeeID,COUNT(*) AS "Number of orders" FROM Orders WHERE Orders.EmployeeID IN (5,7) GROUP BY Orders.EmployeeID;
-- Concatenate Function (instead of using +)
SELECT Customers.CompanyName, CONCAT( Customers.City, ',', Customers.Country) AS "City" FROM Customers;


--------------------------------------------
-- EXERCISES PART 3 --
-- Ex 1
SELECT CONCAT(Employees.FirstName, ' ', Employees.LastName) AS "Employee Name" FROM Employees;
--------------------------------------------


-- EQUATION to NULL;
-- Using `WHERE Region = NULL` will NOT work
SELECT Customers.CompanyName, Customers.Region FROM Customers WHERE Customers.Region IS NULL;
SELECT Customers.CompanyName, Customers.Region FROM Customers WHERE Customers.Region = NULL;    -- doesn't work


--------------------------------------------
-- EXERCISES PART 4
SELECT DISTINCT TOP 7 Customers.Country FROM Customers WHERE Customers.Region IS NOT NULL;
--------------------------------------------


-- Using Operators for calculations ( +, -, *, / and %)
SELECT UnitPrice, Quantity, Discount, UnitPrice*Quantity AS "Gross Total" FROM [Order Details];


--------------------------------------------
-- EXERCISES PART 5
SELECT * FROM [Order Details];
SELECT od.UnitPrice, Quantity, Discount, UnitPrice*Quantity AS "Gross Total", UnitPrice*Quantity*(1-Discount) AS "Net Total" FROM [Order Details] AS od;
--------------------------------------------


-- Sorting (ORDER BY)
SELECT od.UnitPrice, od.Quantity, od.Discount, od.UnitPrice*od.Quantity AS "Gross Total" FROM [Order Details] AS od ORDER BY "Gross Total" DESC;


--------------------------------------------
-- EXERCISES PART 6
-- Exercise 1 - Using ORDER BY 5th column as shorthand.
SELECT TOP 2 od.UnitPrice, od.Quantity, od.Discount, od.UnitPrice*od.Quantity AS "Gross Total", od.UnitPrice*od.Quantity*(1-od.Discount) AS "Net Total" FROM [Order Details] od ORDER BY 5 DESC;
--------------------------------------------


-- STRING OPERATIONS
SELECT PostalCode "Post Code", LEFT(PostalCode, CHARINDEX(' ',PostalCode)-1) AS "Post Code Region", CHARINDEX(' ',PostalCode) AS "Space Found", Customers.Country 
FROM Customers WHERE Customers.Country='UK';


--------------------------------------------
-- EXERCISES PART 7
-- Escape character
SELECT Products.ProductName, CHARINDEX('''', Products.ProductName) AS "Position" FROM Products WHERE Products.ProductName LIKE '%''%';
-- Use CHARINDEX to find apostrophe
SELECT Products.ProductName, CHARINDEX('''', Products.ProductName) AS "Position" FROM Products WHERE CHARINDEX('''', Products.ProductName)!= 0;
-- Only 1 apostrophe in string (savi)
SELECT ProductName From Products WHERE LEN(ProductName) - LEN(REPLACE(ProductName, '''', '')) = 1
--------------------------------------------


-- DATES
-- Year: year, yyyy, yy
-- Day: day, dy, y
SELECT OrderDate, DATEADD(d,5,OrderDate) AS "Due Date", DATEDIFF(d, OrderDate, ShippedDate) AS "Ship Days" FROM Orders;


--------------------------------------------
-- EXERCISES PART 8
-- Output a list of Employees from the Employees table including their Name (concatenated) and their Age (calculated from BirthDate)
SELECT * FROM Employees;
SELECT CONCAT(Employees.FirstName, ' ', Employees.LastName), DATEDIFF(YY, Employees.BirthDate, GETDATE()) AS "Age" FROM Employees;
-- Get age as decimal
SELECT CONCAT(Employees.FirstName, ' ', Employees.LastName), DATEDIFF(d, Employees.BirthDate, GETDATE())/365.25 AS "Age" FROM Employees;
--------------------------------------------


-- ROUNDING
SELECT CONCAT(Employees.FirstName, ' ', Employees.LastName), 
DATEDIFF(d, Employees.BirthDate, GETDATE())/365.25 AS "Age",
CEILING(DATEDIFF(d, Employees.BirthDate, GETDATE())/365.25) AS "Ceil",
FLOOR(DATEDIFF(d, Employees.BirthDate, GETDATE())/365.25) AS "Floor",
ROUND(DATEDIFF(d, Employees.BirthDate, GETDATE())/365.25, 2) AS "Round"
 FROM Employees;

-- CASE statements
SELECT Orders.OrderID, CASE WHEN DATEDIFF(d, OrderDate, ShippedDate) < 10 THEN 'On Time' ELSE 'Overdue' END AS "Status" FROM Orders;
-- Note: "Status" is double quoted since it is column name, while the others are just strings.


--------------------------------------------
-- EXERCISES PART 9
SELECT CONCAT(Employees.FirstName, ' ', Employees.LastName), DATEDIFF(YY, Employees.BirthDate, GETDATE()) AS "AGE",
CASE WHEN DATEDIFF(YY, Employees.BirthDate, GETDATE()) > 65 THEN 'Retired'
WHEN DATEDIFF(YY, Employees.BirthDate, GETDATE()) < 60 THEN 'More than 5 years to go' ELSE 'Retirement Due' 
END AS "Status" FROM Employees;
--------------------------------------------