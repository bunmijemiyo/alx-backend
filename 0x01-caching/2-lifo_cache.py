#!/usr/bin/env python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Last In First Out caching system """
    def __init__(self):
        """ initializes class attribute and superclass """
        super().__init__()
        item_order = []

    def put(self, key, item):
        """ adds new data to cache
        using LIFO algorithm to maintain cache size """
        if key is None or item is None:
            pass
        if key in self.item_order:
            del self.item_order[self.item_order.index(key)]
        if BaseCaching.MAX_ITEMS <= len(self.cache_data):
            print("DISCARD: {}".format(self.item_order[-1]))
            del self.cache_data[self.item_order[-1]]
            del self.item_order[-1]
        self.item_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ return value im cache linked to key """
        return self.cache_data[key] if key is not None else None
