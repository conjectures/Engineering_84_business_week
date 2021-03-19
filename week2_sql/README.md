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
> |02|Lewis|Language|
> |03|Jane|Computer Science|
> 
> The first row contains multiple values in the same column for attribute 'Subject'. The above table should change as shown below:
>
> |ID|Name|Subject|
> |---|---|---|
> |01|Bob|Maths,Chemistry|
> |01|Bob|Chemistry|
> |02|Lewis|Language|
> |03|Jane|Computer Science|

- **2NF**
    + Satisfies 1NF
    + Non-prime attirbutes do not have Partial Functional Dependency on *prime* or *candidate* keys.

- **2NF**
    + Satisfies 2NF
    + Doesn't have Transitive Dependency, where, non-prime attributes depend on another non-prime attribute rather than a primary key.


## Terminology

- **Columns**: The attribute / characteristic of a table
- **Row**: one set of attributes (also records or tuples)
- **Table**
- **DBMS**
- **Compound Key**
- **Primary key**
- **Foreign key** Used to create 

**Relations**
- One to one
- One to many
- Many to many

The many to many relation is implemented with a **Junction table** - a table that forms a composite key with the foreign keys of the records that are connected.

## Cheat Sheet

**Data Manipulation Language** (DML) : [SELECT, INSERT, UPDATE, DELETE]

**Data Definition Languate** (DDL) : [CREATE, ALTER, DROP, TRUNCATE]

**Data Control Language** (DCL) : [GRANT, REVOKE]

**Transaction Control Language** (TCL) : [COMMIT, ROLLBACK, SAVEPOINT]







