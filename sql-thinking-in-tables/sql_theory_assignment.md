Q1. Importance of Databases in Real-World AI Systems

1.Databases play a crucial role in real-world AI systems because they store, manage, and organize large volumes of data required for training and decision-making.
AI systems depend heavily on data such as:
1.User data (profiles, preferences)
2.Transaction data (orders, payments)
3.Sensor data (IoT devices, audio, images)
4.Logs and historical records

Structured storage is necessary because:
1.It ensures data consistency and accuracy
2.Enables fast querying and retrieval
3.Supports data preprocessing for ML models
4.Helps in scaling AI applications efficiently
Example:
In a fraud news detection system, databases store:
1.News articles
2.User feedback
3.Model predictions
This allows the AI model to learn patterns and improve over time.


2. Relational Database Mental Model
A relational database organizes data into tables, which consist of:
Rows (Records): Represent individual entries
Columns (Attributes): Represent properties of the data
Each table should represent a single entity to maintain clarity and avoid redundancy.
Example:
| user_id | name  | email                                     |
| ------- | ----- | ----------------------------------------- |
| 1       | John  | [john@email.com](mailto:john@email.com)   |
| 2       | Alice | [alice@email.com](mailto:alice@email.com) |

Here:
Table = Users (entity)
Row = One user
Column = User attributes

Why one entity per table?
Avoids duplication
Improves data integrity
Makes queries easier


Q3. Primary Key Concept

A primary key is a column (or set of columns) that uniquely identifies each record in a table.
Properties:
1.Must be unique
2.Cannot be NULL

Importance:
1.Ensures each record is identifiable
2.Prevents duplicate entries
3.Helps in linking tables

Example:| user_id (PK) | name  |
| ------------ | ----- |
| 1            | John  |
| 2            | Alice |
Here, user_id is the primary key.

Without a primary key:
Data duplication may occur
Records cannot be uniquely identified

4. Database Schema

A database schema is the structure or blueprint of a database. It defines:
1.Tables
2.Columns and data types
3.Relationships between tables
4.Constraints (primary key, foreign key)

Why schemas are important:
1.Maintain consistency
2.Ensure data integrity
3.Help developers understand the database design

Example:
Users(user_id INT, name VARCHAR)
Orders(order_id INT, user_id INT, amount FLOAT)
This defines:
Table structures
Relationships between data


5. Relationships Between Tables

In relational databases, tables are connected using foreign keys.
A foreign key is a column that refers to the primary key of another table.

Types of Relationships:
1.One-to-One
2.One-to-Many
3.Many-to-Many

Example:
Table: Users
| user_id (PK) | name |
| ------------ | ---- |
| 1            | John |

Table: Orders
| order_id | user_id (FK) | amount |
| -------- | ------------ | ------ |
| 101      | 1            | 500    |
Here:
1.user_id in Orders is a foreign key
2.It connects Orders to Users

Why relationships matter:

1.Avoid data duplication
2.Maintain consistency
3.Enable complex queries using JOINs

Example Query:
SELECT Users.name, Orders.amount
FROM Users
JOIN Orders ON Users.user_id = Orders.user_id;