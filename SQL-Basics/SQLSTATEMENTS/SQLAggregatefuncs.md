# SQL MIN() and MAX() Functions

The MIN() function returns the smallest value of the selected column.

The MAX() function returns the largest value of the selected column.

## MIN() Syntax

```
SELECT MIN(column_name)
FROM table_name
WHERE condition;
```

## MAX() Syntax

```
SELECT MAX(column_name)
FROM table_name
WHERE condition;
```

## MIN() Example
The following SQL statement finds the price of the cheapest product:

### Example

```
SELECT MIN(Price) AS SmallestPrice
FROM Products;
```

## MAX() Example
The following SQL statement finds the price of the most expensive product:

### Example

```
SELECT MAX(Price) AS LargestPrice
FROM Products;
```

# The SQL COUNT(), AVG() and SUM() Functions

The COUNT() function returns the number of rows that matches a specified criteria.

The AVG() function returns the average value of a numeric column.

The SUM() function returns the total sum of a numeric column.

## COUNT() Syntax

```
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

## AVG() Syntax

```
SELECT AVG(column_name)
FROM table_name
WHERE condition;
```

## SUM() Syntax

```
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```

## COUNT() Example
The following SQL statement finds the number of products:

### Example

```
SELECT COUNT(ProductID)
FROM Products;
```

**Note:** ```NULL values are not counted.```


## AVG() Example
The following SQL statement finds the average price of all products:

### Example

```
SELECT AVG(Price)
FROM Products;
```

**Note:** ```NULL values are ignored.```


## SUM() Example
The following SQL statement finds the sum of the "Quantity" fields in the "OrderDetails" table:

### Example

```
SELECT SUM(Quantity)
FROM OrderDetails;
```

**Note:** ```NULL values are ignored.```





