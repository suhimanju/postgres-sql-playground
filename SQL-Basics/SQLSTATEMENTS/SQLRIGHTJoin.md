# SQL RIGHT JOIN Keyword
The RIGHT JOIN keyword returns all records from the right table (table2), and the matched records from the left table (table1). The result is NULL from the left side, when there is no match.

## RIGHT JOIN Syntax
```
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```

**Note:** ```In some databases RIGHT JOIN is called RIGHT OUTER JOIN.```

## SQL RIGHT JOIN Example
The following SQL statement will return all employees, and any orders they might have placed:

### Example
```
SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;
```

**Note:** ```The RIGHT JOIN keyword returns all records from the right table (Employees), even if there are no matches in the left table (Orders).```