# SQL Wildcards

## SQL Wildcard Characters
A wildcard character is used to substitute one or more characters in a string.

Wildcard characters are used with the SQL LIKE operator. The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

## Wildcard Characters in MS Access
| Symbol | Description | Example |
| *	| Represents zero or more characters |	bl* finds bl, black, blue, and blob |
| ?	| Represents a single character	| h?t finds hot, hat, and hit |
| [] | Represents any single character within the brackets | h[oa]t finds hot and hat, but not hit |
| !	| Represents any character not in the brackets | h[!oa]t finds hit, but not hot and hat |
| -	| Represents a range of characters	| c[a-b]t finds cat and cbt |
| #	| Represents any single numeric character | 2#5 finds 205, 215, 225, 235, 245, 255, 265, 275, 285, and 295 |

## Wildcard Characters in SQL Server
| Symbol | Description | Example |
| ------ | ----------- | ------- |
| %	| Represents zero or more characters | bl% finds bl, black, blue, and blob |
| _	| Represents a single character | h_t finds hot, hat, and hit |
| [] | Represents any single character within the brackets | h[oa]t finds hot and hat, but not hit |
| ^	| Represents any character not in the brackets	| h[^oa]t finds hit, but not hot and hat |
| -	| Represents a range of characters | c[a-b]t finds cat and cbt |

All the wildcards can also be used in combinations!

Here are some examples showing different LIKE operators with '%' and '_' wildcards:

| LIKE Operator | Description |
| WHERE CustomerName LIKE 'a%' | Finds any values that starts with "a" |
| WHERE CustomerName LIKE '%a' | Finds any values that ends with "a" |
| WHERE CustomerName LIKE '%or%' | Finds any values that have "or" in any position |
| WHERE CustomerName LIKE '_r%'	| Finds any values that have "r" in the second position |
| WHERE CustomerName LIKE 'a_%_%' | Finds any values that starts with "a" and are at least 3 | characters in length |
| WHERE ContactName LIKE 'a%o' | Finds any values that starts with "a" and ends with "o" |


## Using the % Wildcard
The following SQL statement selects all customers with a City starting with "ber":

### Example
```
SELECT * FROM Customers
WHERE City LIKE 'ber%';
```

The following SQL statement selects all customers with a City containing the pattern "es": 

### Example
```
SELECT * FROM Customers
WHERE City LIKE '%es%';
```

## Using the _ Wildcard
The following SQL statement selects all customers with a City starting with any character, followed by "ondon":

### Example
```
SELECT * FROM Customers
WHERE City LIKE '_ondon';
```

The following SQL statement selects all customers with a City starting with "L", followed by any character, followed by "n", followed by any character, followed by "on":

### Example
```
SELECT * FROM Customers
WHERE City LIKE 'L_n_on';
```

## Using the [charlist] Wildcard
The following SQL statement selects all customers with a City starting with "b", "s", or "p":

### Example
```
SELECT * FROM Customers
WHERE City LIKE '[bsp]%';
```

The following SQL statement selects all customers with a City starting with "a", "b", or "c":

### Example
```
SELECT * FROM Customers
WHERE City LIKE '[a-c]%';
```

## Using the [!charlist] Wildcard
The two following SQL statements select all customers with a City NOT starting with "b", "s", or "p":

### Example
```
SELECT * FROM Customers
WHERE City LIKE '[!bsp]%';
```

Or:

### Example
```
SELECT * FROM Customers
WHERE City NOT LIKE '[bsp]%';
```