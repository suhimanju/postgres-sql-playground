# SQL CREATE INDEX Statement
The CREATE INDEX statement is used to create indexes in tables.

Indexes are used to retrieve data from the database very fast. The users cannot see the indexes,they are just used to speed up searches/queries.

**Note:** Updating a table with indexes takes more time than updating a table without (because the indexes also need an update). So, only create indexes on columns that will be frequently searched against.

## CREATE INDEX Syntax
Creates an index on a table. Duplicate values are allowed:

```
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

## CREATE UNIQUE INDEX Syntax
Creates a unique index on a table. Duplicate values are not allowed:

```
CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ...);
```

**Note:** The syntax for creating indexes varies among different databases. Therefore: Check the syntax for creating indexes in your database.

## CREATE INDEX Example
The SQL statement below creates an index named "idx_lastname" on the "LastName" column in the "Persons" table:
```
CREATE INDEX idx_lastname
ON Persons (LastName);
```

If you want to create an index on a combination of columns, you can list the column names within the parentheses, separated by commas:

```
CREATE INDEX idx_pname
ON Persons (LastName, FirstName);
```

## DROP INDEX Statement
The DROP INDEX statement is used to delete an index in a table.

## MS Access:
```
DROP INDEX index_name ON table_name;
```

## SQL Server:
```
DROP INDEX table_name.index_name;
```

## DB2/Oracle:
```
DROP INDEX index_name;
```

## MySQL:
```
ALTER TABLE table_name
DROP INDEX index_name;
```