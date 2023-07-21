import redis
import sys
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps

# UnionOfTypes = Union[str, bytes, int, float]

def count_calls(fn: Callable) -> Callable:
    key = fn.__qualname__

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return fn(self, *args, **kwargs)

    return wrapper

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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' store data in the cache '''
        randomKey = str(uuid4())
        self._redis.set(randomKey, data)
        return randomKey

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
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
