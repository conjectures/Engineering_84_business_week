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
> |Subject| Teacher |
> |---   | ---     |
> |Maths   | Mr.John |
> |Chemistry| Ms. Mary |
> |Computer Science| Ms. Smith|

- **3NF**
    + Satisfies 2NF
    + Doesn't have Transitive Dependency, where, non-prime attributes depend on another non-prime attribute rather than a primary key.

> Example:
>
> |ID|Name|Subject| School| Total Students|
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
In a relational database, the Primary Key is an attribute that is used to uniquely identifies a row (or tuple). 
It has to be an attribute that is guaranteed to be unique and does not change. 
Also, it cannot be blank or Null. 
The DBMS will enforce the Primary key to take a unique, non-null value and will restrict the existence of repeated records.


### What is a composite/compound key
A composite key is a specific type of primary key which uses the contents of two or more fields from a table to create a unique value.  
In the below table the Name and Subject attributes are not entirely unique, but together they form a composite key which is unique.
>|Name|Subject|Mark|
>|---|---|---|
>|Bob|C++|90| 
>|Bob|Java|80|
>|John|Java|70|
>
A compound key is similar to a composite key, in that two ro more fields are needed to create a unique key, but it is formed when two ro more
primary keys of different tables are combined.

### What is a candidate key
Candidate keys are the set of attributes that uniquely identify tuples in a table, ie. They are  attributes without repeating values. 
The Primary key should be selected from within the candidate keys. 
In essence, a candidate key is an attribute that contains only unique values and can identify each record in the table, it may have mutliple columns and it must not contain null values.

### What is a foreign key
The primary key of a table can be linked to a different table as a foreign key. Via this link, the two tables are connected (or related).  Foreign keys ensure that info in table A is correlated correctly to a row of information in table B (data integration) 

There are no uniqueness constraints for a foreign key, that is, a foreign key can appear multiple times in the same table. 

Special care needs to be taken when removing information that appears in another table via a foreign key. 
A primary key that appears as foreign key in another table must be first removed from the related table it appears, and then can be safely removed. 
Alternatively, the relation can be defined as 'ON DELETE CASCADE' where the foreign key appearances are automatically removed.


### What are the Table Relations
- One to one
- One to many
- Many to many

### What is a Junction Table
The many to many relation is implemented with a **Junction table** - a table that forms a composite key with the foreign keys of the records that are connected.

## Cheat Sheet

## Tips

- **Escaping apostrophe**








