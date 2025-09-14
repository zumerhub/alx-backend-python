import sqlite3
import functools

# Decorator to handle DB connections
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # oprn a connection to the database
        conn = sqlite3.connect('users.db')
        try:
            # inject the connection as the first argument to the decorated function
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper

# Decorator to manage transactions
@with_db_connection
def fetch_all_users(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchall()
    
# Fetch user with ID 1 while managing the DB connection
users = fetch_all_users(user_id=1)
print(users)