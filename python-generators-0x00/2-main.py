
from itertools import islice
batch_users_module = __import__('1-batch_processing')

print("Users older than 25:")
for user in islice(batch_users_module.batch_processing(3), 6):
    print(user)