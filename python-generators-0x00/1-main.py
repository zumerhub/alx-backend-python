
from itertools import islice
streams_users = __import__('0-stream_users')

for user in islice(streams_users.stream_users(), 6):
    print(user)