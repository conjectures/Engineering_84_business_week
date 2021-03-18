# SQL Week

## Theory

> **What is a database?**

  It is an organized collection of structured information, stored in a computer sustem, and is accessible in various ways.
  A database is usually controlled by a database management system (DMBS) that acts as a mediator between the user and tha database.

> **What is a relational database?**

  Relational databases organize their data in tables that are linked to columns that are common in other tables. This 
  relation enables data to be retrieved from multiple tables with a single query.
  The benefit of using relational databases is that they can retrieve a lot of data with complex queries very fast.

**What is SQL**

    Structured Query Language (SQL) is the standard way of communicating with databases. The commands used by SQL are
    categorised into mainly four categories:

      - **Data Definition Language**


<br>

**Database Normalisation**

> It is the process of structuring (relational) databases, in accordance to the normal forms, such that data redundancy is reduced. 

- *First Normal Form (1NF)*

  make everything atomic, ie as small as it can be

  no repeating groups

- *Second Normal Form(2NF)*

  Must satisfy 1NF

  Non primary key attributes are ...


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







