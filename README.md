Python Generators – ALX Backend

This project explores the use of Python generators for handling large datasets efficiently.
It demonstrates how to use lazy evaluation and streaming to minimize memory usage when working with files and databases.

📂 Project Structure
alx-backend-python/
└── python-generators-0x00/
    ├── seed.py
    ├── user_data.csv
    ├── 0-stream_users.py
    ├── 0-main.py
    ├── 1-main.py
    ├── 2-batch_processing.py
    ├── 3-lazy_paginate.py
    ├── 4-stream_ages.py
    └── README.md

⚙️ Setup Instructions
1. Install MySQL

Make sure MySQL server is installed and running on your machine.

On Ubuntu/Debian:

sudo apt update
sudo apt install mysql-server

2. Create the Database

Login to MySQL:

mysql -u root -p


Create the database:

CREATE DATABASE ALX_prodev;
USE ALX_prodev;


The Python script seed.py will automatically create the user_data table if it doesn’t exist.

3. Install Dependencies
pip install mysql-connector-python

4. Seed the Database

Create a file user_data.csv with sample data:

name,email,age
John Doe,john@example.com,30
Jane Smith,jane@example.com,25
Alice Johnson,alice@example.com,40
Bob Brown,bob@example.com,35
Charlie Black,charlie@example.com,28


Run the seeding script:

python3 0-main.py


Expected output:

connection successful
Table user_data created successfully
Database ALX_prodev is present 
[('...', 'John Doe', 'john@example.com', 30), ('...', 'Jane Smith', 'jane@example.com', 25)]

🚀 Tasks & Example Outputs
1. Streaming Users
python3 1-main.py

{'user_id': '...', 'name': 'John Doe', 'email': 'john@example.com', 'age': 30}
{'user_id': '...', 'name': 'Jane Smith', 'email': 'jane@example.com', 'age': 25}

2. Batch Processing
python3 2-batch_processing.py

Users older than 25:
{'user_id': '...', 'name': 'Alice Johnson', 'email': 'alice@example.com', 'age': 40}
{'user_id': '...', 'name': 'Bob Brown', 'email': 'bob@example.com', 'age': 35}

3. Lazy Pagination
python3 3-lazy_paginate.py

Page 1:
{'user_id': '...', 'name': 'John Doe', 'email': 'john@example.com', 'age': 30}
{'user_id': '...', 'name': 'Jane Smith', 'email': 'jane@example.com', 'age': 25}

Page 2:
{'user_id': '...', 'name': 'Alice Johnson', 'email': 'alice@example.com', 'age': 40}

4. Memory-Efficient Aggregation
python3 4-stream_ages.py

Average age of users: 31.6

🛠️ Requirements

Python 3.8+

MySQL server

mysql-connector-python

Install dependencies:

pip install mysql-connector-python

📚 Learning Objectives

Understand Python generators and the yield keyword.

Work with lazy evaluation to process large datasets.

Implement streaming, batching, and pagination efficiently.

Perform aggregation without loading all data into memory.# alx-backend-python
