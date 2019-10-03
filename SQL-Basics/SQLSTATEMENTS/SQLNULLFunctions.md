# SQL NULL Functions

## SQL IFNULL(), ISNULL(), COALESCE(), and NVL() Functions
Look at the following "Products" table:

| P_Id | ProductName | UnitPrice | UnitsInStock | UnitsOnOrder |
| ---- | ----------- | --------- | ------------ | ------------ |
| 1	| Jarlsberg	| 10.45	| 16  | 15 | 
| 2	| Mascarpone | 32.56 | 23 |	   | 
| 3	| Gorgonzola | 15.67 | 9  |	20 | 

Suppose that the "UnitsOnOrder" column is optional, and may contain NULL values.

Look at the following SELECT statement:
```
SELECT ProductName, UnitPrice * (UnitsInStock + UnitsOnOrder)
FROM Products;
```

In the example above, if any of the "UnitsOnOrder" values are NULL, the result will be NULL.

# Solutions
### MySQL

The MySQL IFNULL() function lets you return an alternative value if an expression is NULL:
```
SELECT ProductName, UnitPrice * (UnitsInStock + IFNULL(UnitsOnOrder, 0))
FROM Products;
```

or we can use the COALESCE() function, like this:

```
SELECT ProductName, UnitPrice * (UnitsInStock + COALESCE(UnitsOnOrder, 0))
FROM Products;
```

### SQL Server

The SQL Server ISNULL() function lets you return an alternative value when an expression is NULL:
```
SELECT ProductName, UnitPrice * (UnitsInStock + ISNULL(UnitsOnOrder, 0))
FROM Products;
```

### MS Access

The MS Access IsNull() function returns TRUE (-1) if the expression is a null value, otherwise FALSE (0):
```
SELECT ProductName, UnitPrice * (UnitsInStock + IIF(IsNull(UnitsOnOrder), 0, UnitsOnOrder))
FROM Products;
```

### Oracle

The Oracle NVL() function achieves the same result:

```
SELECT ProductName, UnitPrice * (UnitsInStock + NVL(UnitsOnOrder, 0))
FROM Products;
```