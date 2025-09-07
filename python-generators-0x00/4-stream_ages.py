seed = __import__('seed')



def stream_user_ages():
    
    connection = seed.connect_to_prodev()
    if connection is None:
        return
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT age FROM user_data")
    
    for user in cursor: # loop 1
        yield user['age']
        
        
def calculate_average_age():
    total_age = 0
    count = 0
    
    for age in stream_user_ages(): # loop 2
        total_age += float(age)
        count += 1
    
    if count == 0:
        return 0
    
    return total_age / count

if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age}")
