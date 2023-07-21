import redis
import sys
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps

# UnionOfTypes = Union[str, bytes, int, float]

def count_calls(method: Callable) -> Callable:
    """ mplement a system to count how many times methods of the Cache class are called. """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper

def call_history(method: Callable) -> Callable:
    key1 = method.__qualname__+ ":inputs"
    key2 = method.__qualname__+ ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(key1, str(args))
        x = method(self, *args)
        self._redis.rpush(key2, x)
        return x

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

    @call_history
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
