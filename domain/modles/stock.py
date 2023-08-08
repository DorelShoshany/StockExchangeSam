from datetime import datetime


class Stock:
    def __init__(
            self,
            symbol_id: str,
            update_time: datetime,
            price: float,
            change_percent: str,
            high: float,
            low: float
    ):
        self.symbol_id = symbol_id
        self.update_time = update_time
        self.price = price
        self.change_percent = change_percent
        self.high = high
        self.low = low

    def serialize(self):
        return {
            'symbol': self.symbol_id,
            'update_time': self.update_time,
            'price': self.price,
            'change_percent': self.change_percent
        }
