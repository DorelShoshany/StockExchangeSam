from domain.modles import Stock
from domain.repositories import StocksRepository


class StocksDictRepository(StocksRepository):

    def __init__(self):
        super().__init__()
        self.symbols: dict = {}

    def find_one(self, id: str) -> Stock:
        return self.symbols.get(id)

    def insert_one(self, symbol: Stock):
        self.symbols[symbol.symbol_id] = symbol

