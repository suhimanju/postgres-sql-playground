# PostgreSQL Python: Connect To PostgreSQL Database Server

Python has various database drivers for PostgreSQL. Currently, the psycopg is the most popular PostgreSQL database adapter for the Python language. The psycopg fully implements the Python DB-API 2.0 specification.

The current version of the psycopg is 2 or psycopg2. The psycopg2 database adapter implemented in C as a libpq wrapper resulting in both fast and secure. The psycopg2 provides many useful features such as client-side and server-side cursors, asynchronous notification and communication, COPY command support, etc.

In addition, the psycopg2 driver supports many Python types out-of-the-box. The psycopg2 matches Python objects to the PostgreSQL data types e.g., list to the array, tuples to records, and dictionary to hstore.  If you want to customize and extend the type adaption, you can use a flexible object adaption system.

### Install psycopg2:

```pip3 install psycopg2```

The following statement creates a new database named suppliers in the PostgreSQL database server.

```CREATE DATABASE suppliers;```

To connect to the suppliers database, you use the `connect()` function of the `psycopg2` module. The `connect()` function creates a new database session and returns a new instance of the `connection` class.

With a `connection` object, you can create a new `cursor` to execute an SQL statement and terminate a transaction using either `commit()` or `rollback()` method.

You can specify the connection parameters as a string and pass it to the `connect()` function as follows:

1. ```conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")```

Or you can use a list of keyword arguments:

2. ```conn = psycopg2.connect(host="localhost",database="suppliers", user="postgres", password="postgres")```

The following is the list of the connection parameters:

* `database`: the name of the `database` that you want to connect.
* `user`: the `username` used to authenticate.
* `password`: `password` used to authenticate.
* `host`: database server address e.g., `localhost` or an `IP address`.
* `port`: the `port` number that defaults to `5432` if it is not provided.

To make it more convenient, we will use a configuration file to store all connection parameters. The following is the content of the `database.ini` file. 

```
[postgresql]
host=localhost
database=suppliers
user=postgres
password=postgres
```

The following `config()` function will read the database.ini file and returns the `connection` parameters. Put the `config()` function in the `config.py` file.

```
#!/usr/bin/python
from configparser import ConfigParser
  
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db
```

The following `connect()` function connects to the `suppliers` database and prints out the PostgreSQL database version.

```
#!/usr/bin/python
import psycopg2
from config import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
      
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    connect()
```

## How this works?

* First, read database connection parameters from the `database.ini` file.
* Next, create a new database connection by calling the `connect()` function.
* Then, `create` a new cursor and execute an SQL statement to get the PostgreSQL database version.
* After that, read the result set by calling the  fetchone() method of the cursor object.
* Finally, close the communication with the database server by calling the close() method of the cursor and connection objects.

The `connect()` function raises the `DatabaseError` exception if an error occurred. To see how it works, we can change the connection parameters in the `database.ini` file.

For example, if we change the host to  `localhosts`, the program will output the following message:

```
Connecting to the PostgreSQL database...
could not translate host name "localhosts" to address: Unknown host
```

The following displays error message when we change the database to a non-existing one: supplier

```
Connecting to the PostgreSQL database...
FATAL: database "supplier" does not exist
```

If we change the user to  postgress, it will not be authenticated successfully as shown below:

```
Connecting to the PostgreSQL database...
FATAL: password authentication failed for user "postgress"
```