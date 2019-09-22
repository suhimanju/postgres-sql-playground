## Database Tables

A database most often contains one or more tables. Each table is identified by a name (e.g. "Customers" or "Orders"). Tables contain records (rows) with data.

Below is a selection from the "Customers" table:

| CustomerID  | CustomerName  | ContactName | Address | City | PostalCode | Country |
| ----------- | ------------- | ----------- | ------- | ---- | ---------- | ------- |
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany |
| 2	| Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución | 2222 | México D.F. | 05021	| Mexico |
| 3 | Antonio Moreno Taquería |	Antonio Moreno | Mataderos 2312 | México D.F.	| 05023 | Mexico |
| 4  | Around the Horn |	Thomas Hardy | 120 Hanover Sq. | London	| WA1 1DP |	UK |
| 5	| Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden |


The table above contains five records (one for each customer) and seven columns (CustomerID, CustomerName, ContactName, Address, City, PostalCode, and Country).


## SQL Statements
Most of the actions you need to perform on a database are done with SQL statements.

The following SQL statement selects all the records in the "Customers" table:

### Example
```
SELECT * FROM Customers;
```

## Keep in Mind That...
SQL keywords are NOT case sensitive: select is the same as SELECT

## Semicolon after SQL Statements?
Some database systems require a semicolon at the end of each SQL statement.

Semicolon is the standard way to separate each SQL statement in database systems that allow more than one SQL statement to be executed in the same call to the server.

## SQL commands are mainly categorized into four categories as:

1. DDL – Data Definition Language
2. DQl – Data Query Language
3. DML – Data Manipulation Language
4. DCL – Data Control Language


1. **DDL(Data Definition Language)** : DDL or Data Definition Language actually consists of the SQL commands that can be used to define the database schema. It simply deals with descriptions of the database schema and is used to create and modify the structure of database objects in the database.

**Examples of DDL commands**:

* **CREATE** –is used to create the database or its objects (like table, index, function, views, store procedure and triggers).
* **DROP** –is used to delete objects from the database.
* **ALTER** –is used to alter the structure of the database.
* **TRUNCATE** -is used to remove all records from a table, including all spaces allocated for the records are removed.
* **COMMENT** –is used to add comments to the data dictionary.
* **RENAME** –is used to rename an object existing in the database.

2. **DQL (Data Query Language)** : DQL statements are used for performing queries on the data within schema objects. The purpose of DQL Command is to get some schema relation based on the query passed to it.

**Example of DQL**:

* **SELECT** – is used to retrieve data from the a database.

3. **DML(Data Manipulation Language)** : The SQL commands that deals with the manipulation of data present in the database belong to DML or Data Manipulation Language and this includes most of the SQL statements.

**Examples of DML:**

* **INSERT** – is used to insert data into a table.
* **UPDATE** – is used to update existing data within a table.
* **DELETE** – is used to delete records from a database table.

**DCL(Data Control Language)** : DCL includes commands such as GRANT and REVOKE which mainly deals with the rights, permissions and other controls of the database system.

**Examples of DCL commands:**

* **GRANT**-gives user’s access privileges to database.
* **REVOKE**-withdraw user’s access privileges given by using the GRANT command.

**TCL(transaction Control Language)** : TCL commands deals with the transaction(s) within the database.

**Examples of TCL commands:**

**COMMIT**– commits a Transaction.
**ROLLBACK**– rollbacks a transaction in case of any error occurs.
**SAVEPOINT**–sets a savepoint within a transaction.
**SET TRANSACTION**–specify characteristics for the transaction.