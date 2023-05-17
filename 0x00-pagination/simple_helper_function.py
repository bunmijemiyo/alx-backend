#!/usr/bin/python3

def index_range(page, page_size):
    start = (page - 1) * page_size
    end = start + page_size
    idx = (start, end)
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
