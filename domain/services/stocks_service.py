from datetime import datetime, time, timedelta
from typing import Union

from domain.modles import Stock
from domain.repositories import StocksRepository
from globals import configuration


class StocksService:

    def __init__(self, stocks_repository: StocksRepository):
        self.stocks_repository = stocks_repository

    def get_fresh_stock(self, symbol_id) -> Union[Stock, None]:
        stock: Stock = self.stocks_repository.find_one(symbol_id)
        if stock and self._is_fresh_stock(stock):
            return stock

    def save_stock(self, stock):
        self.stocks_repository.insert_one(stock)

    def _is_fresh_stock(self, stock: Stock):
        stock_value_fresh = configuration.stock_value_fresh
        now = datetime.now()
        update_delta = now - stock.update_time
        time_between_trading = self._is_time_between(time(10, 00), time(17, 00))
        if not time_between_trading and update_delta >= timedelta(hours=1):
            return False

        if stock.high > stock_value_fresh or stock.low > stock_value_fresh:
            if update_delta >= timedelta(minutes=10):
                return False

        elif stock.high < stock_value_fresh or stock.low < stock_value_fresh:
            if update_delta >= timedelta(minutes=20):
                return False

        return True

    @staticmethod
    def _is_time_between(begin_time, end_time, check_time=None):
        # If check time is not given, default to current UTC time
        check_time = check_time or datetime.utcnow().time()
        if begin_time < end_time:
            return check_time >= begin_time and check_time <= end_time
        else:  # crosses midnight
            return check_time >= begin_time or check_time <= end_time
