-- Test 1 
-- Alexis Othonos
-- Start time 13:52

USE Northwind
/*1. Create a report showing the title of courtesy and the first and last name
of all employees whose title of courtesy is not "Ms." or "Mrs.".*/
SELECT Employees.TitleOfCourtesy, CONCAT(Employees.FirstName, ' ', Employees.LastName) AS "Employee Name"
    FROM Employees
    WHERE Employees.TitleOfCourtesy NOT IN ('Ms.', 'Mrs.')

/*2. Create a report that shows the company name, contact title, city and country of all customers 
in Mexico or in any city in Spain except Madrid(in Spain).*/
SELECT Customers.CompanyName, Customers.ContactTitle, Customers.City, Customers.Country 
    FROM Customers
    WHERE Customers.Country IN ('Mexico', 'Spain') AND Customers.City != 'Madrid'

/*3. Create a report showing the title of courtesy and the first and
last name of all employees whose title of courtesy begins with "M" and
is followed by a character and a period (.).*/
SELECT Employees.TitleOfCourtesy, Employees.FirstName, Employees.LastName
    FROM Employees
    WHERE Employees.TitleOfCourtesy LIKE 'M_.'

/*4. Create a report showing the first and last names of
all employees whose region is defined.*/
SELECT Employees.FirstName, Employees.LastName
    FROM Employees
    WHERE Employees.Region IS NOT NULL

/*5. Select the TitleOfCourtesy, FirstName and LastName columns from the Employees table.
  Sort first by TitleOfCourtesy in ascending order and then by LastName 
   in descending order.*/
SELECT Employees.TitleOfCourtesy, Employees.FirstName, Employees.LastName
    FROM Employees
    ORDER BY Employees.TitleOfCourtesy, Employees.LastName DESC 
    
/*6. Write a query to get the number of employees with the same job title.*/
SELECT Employees.Title, COUNT(*) AS "Number of employees"
    FROM Employees
    GROUP BY Employees.Title

/*7.
Create a report showing the Order ID, the name of the company that placed the order,
and the first and last name of the associated employee.
Only show orders placed after January 1, 1998 that shipped after they were required.
Sort by Company Name.
*/
SELECT Orders.OrderID, Customers.CompanyName, CONCAT(Employees.FirstName, ' ', Employees.LastName) AS "Employee Name"
    FROM Orders
    INNER JOIN Customers ON Customers.CustomerID = Orders.CustomerID
    INNER JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID
    WHERE Orders.OrderDate > '19980101' AND DATEDIFF(d, Orders.RequiredDate, Orders.ShippedDate) > 0
    ORDER BY Customers.CompanyName

/*8.
Create a report that shows the total quantity of per products (from the OrderDetails table) ordered. Only show records for products for which the quantity ordered is fewer than 200. 
*/
SELECT odt.ProductID, SUM(odt.Quantity) as "Total Quantity"
    FROM [Order Details] as odt
    GROUP BY odt.ProductID
    HAVING SUM(odt.Quantity) < 200
    ORDER BY odt.ProductID

/*9.Create a report that shows the total number of orders by Customer since December 31, 1996. 
The report should only return rows for which the NumOrders is greater than 15. 
*/
SELECT inner_table.CustomerID, COUNT(inner_table.OrderID) AS "Total orders"
    FROM (SELECT Orders.OrderID, Orders.CustomerID FROM Orders WHERE Orders.OrderDate > '19961231' GROUP BY Orders.OrderID, Orders.CustomerID) as inner_table
    GROUP BY inner_table.CustomerID
    HAVING COUNT(inner_table.OrderID) > 15
    ORDER BY "Total orders" DESC

/*10.  SQL statement will return all customers, and number of orders they might have placed. 
Include those customers as well who have not placed any orders.*/
--(SELECT COUNT(*) FROM Orders GROUP BY Orders.CustomerID) 
SELECT Customers.CustomerID, Customers.ContactName, inner_table.OrderNum
    FROM Customers
    LEFT JOIN (SELECT Orders.CustomerID, COUNT(*) AS "OrderNum" FROM Orders GROUP BY Orders.CustomerID) AS inner_table ON  inner_table.CustomerID = Customers.CustomerID

-- Finished 14:49
