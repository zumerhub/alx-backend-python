import time
import sqlite3 
import functools


query_cache = {}

"""your code goes here"""
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            results = func(conn, *args, **kwargs)
            return results
        finally:
            conn.close()
    return wrapper

def cache_query(func):
    # def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # check if query is passed as a positional or keyword argument
            if args:
                query - args[0]
            else:
                query = kwargs.get('query', '')
            # check if the result is already cached
            if query in query_cache:
                print("[CACHE HIT] Returning cached result for query: {query}")
                return query_cache[query]
            
            # execute the query and cache the result
            print("[CACHE MISS] Executing query and caching result: {query}")
            result = func(*args, **kwargs)
            query_cache[query] = result
            return result
        return wrapper
    # return decorator
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")