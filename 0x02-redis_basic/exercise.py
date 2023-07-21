import redis
from uuid import uuid4
from typing import Union

class Cache:
    '''
        Cache class.
    '''
    def __init__(self):
        '''
            Initialize the cache.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' store data in the cache '''
        randomKey = str(uuid4())
        self._redis.set(randomKey, data)
        return randomKey
