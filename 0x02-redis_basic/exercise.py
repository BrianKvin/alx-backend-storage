import redis
import sys
from uuid import uuid4
from typing import Union, Callable, Optional

UnionOfTypes = Union[str, bytes, int, float]


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

    def store(self, data: UnionOfTypes) -> str:
        ''' store data in the cache '''
        randomKey = str(uuid4())
        self._redis.set(randomKey, data)
        return randomKey

    def get(self, key: str, fn: Optional[Callable] = None) -> UnionOfTypes:
        ''' get data from cache '''
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key).decode()

    def get_str(self: bytes) -> int:
        """Returns a number"""
        return int.from_bytes(self, sys.byteorder)

    def get_int(self: bytes) -> str:
        """ returns a string """
        return self.decode("utf-8")
