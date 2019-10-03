# SQL Self JOIN
A self JOIN is a regular join, but the table is joined with itself.

## Self JOIN Syntax
```
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
```

T1 and T2 are different table aliases for the same table.

## SQL Self JOIN Example
The following SQL statement matches customers that are from the same city:

### Example
```
SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City
ORDER BY A.City;
```