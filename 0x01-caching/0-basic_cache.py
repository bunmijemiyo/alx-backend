#!/usr/bin/env python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class for caching data in key-value pairs

    methods:
        put: adds a key-value pair in cache
        get: retrieves a cache data
    """
    def __init__(self):
        """
        initializes super class
        """
        super().__init__()

    def put(self, key, item):
        """
        Add data in cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves data from cache
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
