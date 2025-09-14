import sqlite3

class ExecutQuery:
    def __init__(self, dbname, query, params=None):
        self.dbname = dbname
        self.query = query
        self.params = params if params is not None else ()
        self.conn = None
        self.cursor = None
        self.results = None
        
    def __enter__(self):
        print(f"[OPEN] Connecting to database: {self.dbname}")
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        print(f"[EXECUTE] Executing query: {self.query} with params: {self.params}")
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(f"[ERROR] An error occurred: {exc_value} - rolling back transaction.")
            self.conn.rollback()
        else: 
            self.conn.commit()
            print(f"[COMMIT] Transaction committed successfully.")
        self.conn.close()
        print(f"[CLOSE] Connection to database {self.dbname} closed.")
        
        # return False means re-raise exception if any
        return False
        