# SQL Week

## Theory

### What is a database?

  It is an organized collection of structured information, stored in a computer sustem, and is accessible in various ways.
  A database is usually controlled by a database management system (DMBS) that acts as a mediator between the user and tha database.

### What is a relational database?

  Relational databases organize their data in tables that are linked to columns that are common in other tables. This 
  relation enables data to be retrieved from multiple tables with a single query.
  The benefit of using relational databases is that they can retrieve a lot of data with complex queries very fast.

### What is SQL

  Structured Query Language (SQL) is the standard way of communicating with databases. The commands used by SQL are
  categorised into mainly four categories; **Data Manipulation**, **Data Definition**, **Data Control** and *Transaction Control** Languages

| DML | DDL | DCL | TCL |
| --- | --- | --- | --- |
|SELECT|CREATE|GRANT| COMMIT  |
|INSERT|ALTER|REVOKE| ROLLBACK|
|UPDATE|DROP|      |SAVEPOINT |
|DELETE|TRUNCATE|  |          |

<br>

### What is Database Normalisation

  It is the process of structuring (relational) databases, in accordance to normal forms, ...
  Normalising the databases makes it more space and time efficient and prevents insert and update anomalies, that is, information is not maintained in multiple tables and
  only needs to be inserted or updated once, in one location.

  The first three Normal Forms are listed below:

- **1NF**
    + Values in each column of a table must be atomic.
    + Values in the same column should be of the same domain
    + All the columns in a table should have unique names

> Example
> 
> |ID|Name|Subject|
> |---|---|---|
> |01|Bob|Maths,Chemistry|
> |02|Lewis|Maths|
> |03|Jane|Computer Science|
> 
> The first row contains multiple values in the same column for attribute 'Subject'. The above table should change as shown below:
>
> |ID|Name|Subject|
> |---|---|---|
> |01|Bob|Maths|
> |01|Bob|Chemistry|
> |02|Lewis|Maths|
> |03|Jane|Computer Science|

- **2NF**
    + Satisfies 1NF
    + Non-prime attirbutes do not have Partial Functional Dependency on *prime* or *candidate* keys.

> Example
> 
> |ID|Name|Subject| Teacher |
> |---|---| ---   | ---     |
> |01|Bob|Maths   | Mr.John |
> |01|Bob|Chemistry| Ms. Mary |
> |02|Lewis|Maths|   Mr.John|
> |04|Jane|Computer Science| Ms. Smith|
>
> In the above table, the primary key is the combination of Student ID and Subject. However the teacher only depends on the Subject and not on the ID of the student.
> The table should be split into two with both adhering the first and second normal form:
>
> |ID|Name|Subject| 
> |---|---| ---   |
> |01|Bob|Maths   | 
> |01|Bob|Chemistry|
> |02|Lewis|Maths| 
> |04|Jane|Computer Science| 
>
> ||Subject| Teacher |
> |---   | ---     |
> |Maths   | Mr.John |
> |Chemistry| Ms. Mary |
> |Computer Science| Ms. Smith|

- **3NF**
    + Satisfies 2NF
    + Doesn't have Transitive Dependency, where, non-prime attributes depend on another non-prime attribute rather than a primary key.

> Example:
>
> |ID|Name|Subject| School| Total Students
> |---|---| ---   | ---     | --- |
> |01|Bob|Maths   | St. Johns| 150|
> |01|Bob|Chemistry| St. Johns| 150|
> |02|Lewis|Maths| Edmonton| 200|
> |04|Jane|Computer Science| St. Johns| 150|
>
> In the above table, the Total Student attribute depends on a non-prime attribue, the School. For the table to satisfy the 3NF, the School Students table must
> be split into a related table:
>
> |ID|Name|Subject| School| 
> |---|---| ---   | ---     |
> |01|Bob|Maths   | St. Johns|
> |01|Bob|Chemistry| St. Johns|
> |02|Lewis|Maths| Edmonton|
> |04|Jane|Computer Science| St. Johns|
>
> |School| Total Students
> | ---     | --- |
> | St. Johns| 150|
> | Edmonton| 200|


### What is a primary key

### What is a foreign key

### What is a candidate key

### What is a composite key


### What are the Table Relations
- One to one
- One to many
- Many to many

### What is a Junction Table
The many to many relation is implemented with a **Junction table** - a table that forms a composite key with the foreign keys of the records that are connected.

## Cheat Sheet

## Tips

- **Escaping apostrophe**








