'''
Retry decorator:
  * tries: how many times should function be retried
  * delay: seconds interval between retries
  * backoff multiplier e.g. value of 2 will double the delay each retry
'''

from functools import wraps
import random
import time
from datetime import datetime
import os
file_path= os.getcwd()

def retry(Exception: tuple, tries: int, delay: int, backoff: int, logger: str) -> callable:
    def retrier(func: callable) -> callable :
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict):
            err = None
            local_tries = tries
            local_delay = delay
            while local_tries > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    local_tries -= 1
                    error = exc
                time.sleep(local_delay)
                local_delay *= backoff
                with open(logger, 'a+') as f:
                    f.write(' '.join((' Datetime :: ', datetime.now().isoformat() ,' Retrying',
                            func.__name__, 'for', str(local_tries),'time!','\n' ))  )
                    f.close
            raise error

        return wrapper
    return retrier



@retry(Exception, tries=3, delay=2, backoff=1,logger = 'Info.log')
def random_numbers_interval(p, q) :
    number = random.random()
    if number < p :
        raise Exception('less than lower bound')
    if number > q :
        raise Exception('grader than upper bound')
    return number

if __name__ == '__main__' :
    print(random_numbers_interval(0.4, 0.5))














