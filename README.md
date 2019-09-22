# postgres-sql-playground
This repository contains sample syntax and examples pertaining to SQL queries, connecting to PostgresDB using python and executing of SQL on a PostgresDB


## What is SQL?
SQL is a standard language for storing, manipulating and retrieving data in databases.

## What is PostgreSQL?
PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads. The origins of PostgreSQL date back to 1986 as part of the POSTGRES project at the University of California at Berkeley and has more than 30 years of active development on the core platform.

PostgreSQL has earned a strong reputation for its proven architecture, reliability, data integrity, robust feature set, extensibility, and the dedication of the open source community behind the software to consistently deliver performant and innovative solutions. PostgreSQL runs on all major operating systems, has been ACID-compliant since 2001, and has powerful add-ons such as the popular PostGIS geospatial database extender. It is no surprise that PostgreSQL has become the open source relational database of choice for many people and organisations.

Getting started with using PostgreSQL has never been easier - pick a project you want to build, and let PostgreSQL safely and robustly store your data.

## Why use PostgreSQL?
PostgreSQL comes with many features aimed to help developers build applications, administrators to protect data integrity and build fault-tolerant environments, and help you manage your data no matter how big or small the dataset. In addition to being free and open source, PostgreSQL is highly extensible. For example, you can define your own data types, build out custom functions, even write code from different programming languages without recompiling your database!

PostgreSQL tries to conform with the SQL standard where such conformance does not contradict traditional features or could lead to poor architectural decisions. Many of the features required by the SQL standard are supported, though sometimes with slightly differing syntax or function. Further moves towards conformance can be expected over time. As of the version 11 release in October 2018, PostgreSQL conforms to at least 160 of the 179 mandatory features for SQL:2011 Core conformance. As of this writing, no relational database meets full conformance with this standard.

## Below is an inexhaustive list of various features found in PostgreSQL:

## Data Types
* *Primitives: Integer, Numeric, String, Boolean*
      * Structured: Date/Time, Array, Range, UUID
      * Document: JSON/JSONB, XML, Key-value (Hstore)
      * Geometry: Point, Line, Circle, Polygon
      * Customizations: Composite, Custom Types

* *Data Integrity*
      * UNIQUE, NOT NULL
      * Primary Keys
      * Foreign Keys
      * Exclusion Constraints
      * Explicit Locks, Advisory Locks
* *Concurrency, Performance*
      * Indexing: B-tree, Multicolumn, Expressions, Partial
      * Advanced Indexing: GiST, SP-Gist, KNN Gist, GIN, BRIN, Covering indexes, Bloom filters
      * Sophisticated query planner / optimizer, index-only scans, multicolumn statistics
      * Transactions, Nested Transactions (via savepoints)
      * Multi-Version concurrency Control (MVCC)
      * Parallelization of read queries and building B-tree indexes
      * Table partitioning
      * All transaction isolation levels defined in the SQL standard, including Serializable
      * Just-in-time (JIT) compilation of expressions
* *Reliability, Disaster Recovery*
      * Write-ahead Logging (WAL)
      * Replication: Asynchronous, Synchronous, Logical
      * Point-in-time-recovery (PITR), active standbys
      * Tablespaces
* *Security*
    * Authentication: GSSAPI, SSPI, LDAP, SCRAM-SHA-256, Certificate, and more
    * Robust access-control system
    * Column and row-level security
* *Extensibility*
    * Stored functions and procedures
    * Procedural Languages: PL/PGSQL, Perl, Python (and many more)
    * Foreign data wrappers: connect to other databases or streams with a standard SQL interface
    * Many extensions that provide additional functionality, including PostGIS
* *Internationalisation, Text Search*
    * Support for international character sets, e.g. through ICU collations
    * Full-text search

There are many more features that you can discover in the PostgreSQL documentation. Additionally, PostgreSQL is highly extensible: many features, such as indexes, have defined APIs so that you can build out with PostgreSQL to solve your challenges.

Below is the link for current version of Postgresql documentation:
*Link*: https://www.postgresql.org/docs/current/index.html 

PostgreSQL has been proven to be highly scalable both in the sheer quantity of data it can manage and in the number of concurrent users it can accommodate. There are active PostgreSQL clusters in production environments that manage many terabytes of data, and specialized systems that manage petabytes.

