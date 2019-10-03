## The SQL AND, OR and NOT Operators

The WHERE clause can be combined with AND, OR, and NOT operators.

The AND and OR operators are used to filter records based on more than one condition:

* The AND operator displays a record if all the conditions separated by AND are TRUE.
* The OR operator displays a record if any of the conditions separated by OR is TRUE.
* The NOT operator displays a record if the condition(s) is NOT TRUE.

## AND Syntax

```
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```

## OR Syntax

```
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
```

## NOT Syntax

```
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```

## Demo Database
Below is a selection from the "Customers" table in the Northwind sample database:

| CustomerID  | CustomerName  | ContactName | Address | City | PostalCode | Country |
| ----------- | ------------- | ----------- | ------- | ---- | ---------- | ------- |
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany |
| 2	| Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución | 2222 | México D.F. | 05021	| Mexico |
| 3 | Antonio Moreno Taquería |	Antonio Moreno | Mataderos 2312 | México D.F.	| 05023 | Mexico |
| 4  | Around the Horn |	Thomas Hardy | 120 Hanover Sq. | London	| WA1 1DP |	UK |
| 5	| Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden |


## AND Example
The following SQL statement selects all fields from "Customers" where country is "Germany" AND city is "Berlin":

### Example

```
SELECT * FROM Customers
WHERE Country='Germany' AND City='Berlin';
```

### Output

| CustomerID  | CustomerName  | ContactName | Address | City | PostalCode | Country |
| ----------- | ------------- | ----------- | ------- | ---- | ---------- | ------- |
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany |


## OR Example
The following SQL statement selects all fields from "Customers" where city is "Berlin" OR "München":

### Example

```
SELECT * FROM Customers
WHERE City='Berlin' OR City='München';
```

### Output

| CustomerID  | CustomerName  | ContactName | Address | City | PostalCode | Country |
| ----------- | ------------- | ----------- | ------- | ---- | ---------- | ------- |
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany |
| 25 | Frankenversand | Peter Franken | Berliner Platz 43 | München | 80805 | Germany |


## NOT Example
The following SQL statement selects all fields from "Customers" where country is NOT "Germany":

### Example

```
SELECT * FROM Customers
WHERE NOT Country='Germany';
```

### Output

| CustomerID  | CustomerName  | ContactName | Address | City | PostalCode | Country |
| ----------- | ------------- | ----------- | ------- | ---- | ---------- | ------- |
| 2	| Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución | 2222 | México D.F. | 05021	| Mexico |
| 3 | Antonio Moreno Taquería |	Antonio Moreno | Mataderos 2312 | México D.F.	| 05023 | Mexico |
| 4  | Around the Horn |	Thomas Hardy | 120 Hanover Sq. | London	| WA1 1DP |	UK |
| 5	| Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden |


### Combining AND, OR and NOT
You can also combine the AND, OR and NOT operators.

The following SQL statement selects all fields from "Customers" where country is "Germany" AND city must be "Berlin" OR "München" (use parenthesis to form complex expressions):

### Example

```
SELECT * FROM Customers
WHERE Country='Germany' AND (City='Berlin' OR City='München');
```

### Output

| CustomerID  | CustomerName  | ContactName | Address | City | PostalCode | Country |
| ----------- | ------------- | ----------- | ------- | ---- | ---------- | ------- |
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany |
| 25 | Frankenversand | Peter Franken | Berliner Platz 43 | München | 80805 | Germany |


The following SQL statement selects all fields from "Customers" where country is NOT "Germany" and NOT "USA":

### Example

```
SELECT * FROM Customers
WHERE NOT Country='Germany' AND NOT Country='USA';
```

### Output

| CustomerID  | CustomerName  | ContactName | Address | City | PostalCode | Country |
| ----------- | ------------- | ----------- | ------- | ---- | ---------- | ------- |
| 2	| Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución | 2222 | México D.F. | 05021	| Mexico |
| 3 | Antonio Moreno Taquería |	Antonio Moreno | Mataderos 2312 | México D.F.	| 05023 | Mexico |
| 4  | Around the Horn |	Thomas Hardy | 120 Hanover Sq. | London	| WA1 1DP |	UK |
| 5	| Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden |