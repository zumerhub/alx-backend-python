#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
print(mysql.connector.__version__)

import csv
import uuid
import os

DB_NAME = "alx_prodev"
TABLE_NAME = "user_data"

def connect_db():
    """Connects to MySQL server (without specifying a database)."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="samuel1234"  
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """Creates the ALX_prodev database if it does not exist."""
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
        print(f"Database {DB_NAME} created or already exists")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    finally:
        cursor.close()

def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="samuel1234",  
            database=DB_NAME
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """Creates the user_data table if it does not exist."""
    cursor = connection.cursor()
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX (user_id)
    )
    """
    try:
        cursor.execute(create_table_query)
        print(f"Table {TABLE_NAME} created successfully")
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")
    finally:
        cursor.close()

def insert_data(connection, csv_file):
    """Inserts data from CSV file into user_data table."""
    if not os.path.isfile(csv_file):
        print(f"CSV file {csv_file} does not exist.")
        return
    
    cursor = connection.cursor()
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            user_id = str(uuid.uuid4())  # generate unique UUID for each row
            name = row['name']
            email = row['email']
            age = row['age']
            try:
                cursor.execute(f"""
                INSERT INTO {TABLE_NAME} (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, age))
            except mysql.connector.Error as err:
                print(f"Error inserting row: {err}")
    connection.commit()
    cursor.close()
    print(f"Data from {csv_file} inserted successfully")

def stream_rows(connection):
    """Generator to stream rows from the user_data table one by one."""
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    for row in cursor:
        yield row
    cursor.close()
