#!/usr/bin/env python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First In First Out caching system
    """
    def __init__(self):
        """ initializes class attribute and superclass """
        super().__init__()
        item_order = []

    def put(self, key, item):
        """ adds new data to cache
        using FIFO algorithm to maintain cache size """
        if key is None or item is None:
            pass
        if BaseCaching.MAX_ITEMS <= len(self.cache_data):
            print("DISCARD: {}".format(self.item_order[0]))
            del self.cache_data[self.item_order[0]]
            del self.item_order[0]
        self.item_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ return value im cache linked to key """
        return self.cache_data[key] if key is not None else None
