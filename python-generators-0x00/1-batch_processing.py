import re
import seed


def stream_users_in_batches(batch_size):
    # Connect to the ALX_prodev database
    connection = seed.connect_to_prodev()
    if connection is None:
        print("Connection to ALX_prodev database failed.")
        return
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data")
    
    batch = []
    for row in cursor: # loop 1
        batch.append(row)
        if len(batch) >= batch_size:
            yield batch
            batch = []
            
            
    # Yield rows one by one
    if batch:
        yield batch
        
    cursor.close()
    connection.close()
    
        
def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size): # loop 2
        for user in batch: # loop 3
            print(user)
            if user['age'] > 25:
                yield user
                
                