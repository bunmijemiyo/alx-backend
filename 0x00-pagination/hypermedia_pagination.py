#!/usr/bin/python3import csv
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def assert_type_integer_positive(value: int) -> None:
        assert type(value) is int and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        self.assert_type_integer_positive(page)
        self.assert_type_integer_positive(page_size)
        try:
            dataset = self.dataset()
            idxs = index_range(page, page_size)
            return dataset[idxs[0]:idxs[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10):
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size + 1
        hyper = {
            'data': data,
            'page': page,
            'page_size': page_size if len(data) >= page_size else len(data),
            'prev_page': page - 1 if page > 1 else None,
            'next_page': page + 1 if page < total_pages else None,
            'total_pages': total_pages,
            }
        return hyper
