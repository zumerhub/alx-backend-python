from itertools import islice
import sys
lazy_paginator = __import__('2-lazy_paginate')


try:
    for user in islice(lazy_paginator.lazy_paginate(3), 10):  #fetch 3 users at a time. islice(..., 10) → print only the first 10 users
        for user in user:
            print(user)

except BrokenPipeError:
    sys.stderr.close()