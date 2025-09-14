import sqlite3


class databaseConnection():
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        
    def __enter__(self):
        print(f"[OPEN] Connecting to database: {self.db_name}")
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(f"[ERROR] An error occurred: {exc_value} - rolling back transaction.")
            self.conn.rollback()
        else: 
            self.conn.commit()
            print(f"[COMMIT] Transaction committed successfully.")
        self.conn.close()
        print(f"[CLOSE] Connection to database {self.db_name} closed.")
        
        # return False means re-raise exception if any
        return False
    
with databaseConnection('users.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)





# Sample 1
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()        
        
# Sample 2        
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True

with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()