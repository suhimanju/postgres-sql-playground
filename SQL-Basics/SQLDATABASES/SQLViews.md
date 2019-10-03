# SQL Views

## SQL CREATE VIEW Statement
In SQL, a view is a virtual table based on the result-set of an SQL statement.

A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.

You can add SQL functions, WHERE, and JOIN statements to a view and present the data as if the data were coming from one single table.

## CREATE VIEW Syntax
```
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**Note:** A view always shows up-to-date data! The database engine recreates the data, using the view's SQL statement, every time a user queries a view.

## SQL CREATE VIEW Examples
The following SQL creates a view that shows all customers from Brazil:

### Example
```
CREATE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName
FROM Customers
WHERE Country = "Brazil";
```

We can query the view above as follows:

### Example
```
SELECT * FROM [Brazil Customers];
```

The following SQL creates a view that selects every product in the "Products" table with a price higher than the average price:

### Example
```
CREATE VIEW [Products Above Average Price] AS
SELECT ProductName, Price
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);
```

We can query the view above as follows:

### Example
```SELECT * FROM [Products Above Average Price];```

## SQL Updating a View
A view can be updated with the CREATE OR REPLACE VIEW command.

## SQL CREATE OR REPLACE VIEW Syntax
```
CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

The following SQL adds the "City" column to the "Brazil Customers" view:

### Example
```
CREATE OR REPLACE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName, City
FROM Customers
WHERE Country = "Brazil";
```

## SQL Dropping a View
A view is deleted with the DROP VIEW command.

## SQL DROP VIEW Syntax
```
DROP VIEW view_name;
```

The following SQL drops the "Brazil Customers" view:

### Example
```
DROP VIEW [Brazil Customers];
```