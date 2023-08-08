from typing import Union

from domain.modles import Stock
from domain.repositories import StocksRepository


class StocksMongoDBRepository(StocksRepository):

    def __init__(self, db):
        self.stocks_collection = db["stocks"]
        self.stocks_collection.create_index([("symbol_id", 1)])
        # we don't need to save stock after 1 hour - it's the must old stock that we may return
        self.stocks_collection.create_index("expiration_time", expireAfterSeconds=3600)
        super().__init__()

    def find_one(self, symbol_id: str) -> Union[Stock, None]:
        document = self.stocks_collection.find_one({"symbol_id": symbol_id})
        if document:
            stock = Stock(
                symbol_id=document.get("symbol_id"),
                update_time=document.get("update_time"),
                price=document.get("price"),
                change_percent=document.get('change_percent'),
                high=document.get("high"),
                low=document.get("low")
            )
            return stock
        return None

    def insert_one(self, stock: Stock):
        document: {} = self._to_document(stock)
        self.stocks_collection.update_one(
            filter={'symbol_id': stock.symbol_id},
            update={'$set': document},
            upsert=True
        )

    def _to_document(self, stock: Stock) -> {}:
        return {
            "symbol_id": stock.symbol_id,
            "update_time": stock.update_time,
            "price": stock.price,
            "change_percent": stock.change_percent,
            "high": stock.high,
            "low": stock.low
        }
