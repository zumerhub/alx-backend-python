seed = __import__('seed')


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    
    if connection is None:
        print("Connection to ALX_prodev database failed.")
        return []
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    offset = 0
    while True: # only loop allowed 
        page = paginate_users(page_size, offset)
        if not page:  #No more rows
            break
        
        for user in page:
            yield user

        offset += page_size