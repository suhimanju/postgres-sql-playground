# The SQL HAVING Clause
The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.

## HAVING Syntax
```
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```

## SQL HAVING Examples
The following SQL statement lists the number of customers in each country. Only include countries with more than 5 customers:

### Example
```
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;
```

The following SQL statement lists the number of customers in each country, sorted high to low (Only include countries with more than 5 customers):

### Example
```
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5
ORDER BY COUNT(CustomerID) DESC;
```