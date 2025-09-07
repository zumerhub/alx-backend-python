import seed


def stream_users():
    # Connect to the ALX_prodev database
    connection = seed.connect_to_prodev()
    if connection is None:
        return
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data")
        
    # Yield rows one by one
    for row in cursor:
        yield row
    cursor.close()
    connection.close()