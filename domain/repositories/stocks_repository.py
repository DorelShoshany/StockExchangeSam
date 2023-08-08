from typing import Union

from domain.modles import Stock
from abc import ABC


class StocksRepository(ABC):

    def __init__(self):
        ...

    def find_one(self, symbol_id: str) -> Union[Stock, None]:
        ...

    def insert_one(self, stock: Stock):
        ...
