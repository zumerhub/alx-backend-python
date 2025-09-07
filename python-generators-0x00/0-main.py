from multiprocessing import connection
import seed

# Connect to MysQL server
connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    connection.close()
    print("Connection to MySQL Server Successful")
    
    
# Connect to the ALX_prodev database
connection = seed.connect_to_prodev()
if connection:
    # Create the table
    seed.create_table(connection)
    
    # Insert data from CSV file
    seed.insert_data(connection, 'user_data.csv')
    
    cursor = connection.cursor()
    cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'alx_prodev'")
    result = cursor.fetchone()
    if result:
        print("Database alx_prodev exists")
    cursor.close()
    
    # Stream and print first 5 rows using generator
    print("\nFirst 5 rows using generator:")
    count = 0
    for row in seed.stream_rows(connection):
        print(row)
        count += 1
        if count >= 5:
            break
        
    connection.close()