from datetime import datetime
from typing import Union
import requests

from domain.modles import Stock
from exceptions import NotFoundError
from globals import configuration


class StocksRequestsService:

    def get_stock_by_symbol_id(self, symbol_id) -> Union[None, Stock]:
        url_request = configuration.stock_url_request
        url_with_symbol = f"{url_request}{symbol_id}"
        headers = {
            "Content-Type": "application/json",
        }

        response = requests.get(url=url_with_symbol, headers=headers)
        global_quote = response.json().get('Global Quote', {})

        if response.status_code == 200 and global_quote:
            return Stock(
                symbol_id=global_quote.get('01. symbol'),
                price=float(global_quote.get('05. price')),
                high=float(global_quote.get('03. high')),
                low=float(global_quote.get('04. low')),
                update_time=datetime.now(),
                change_percent=global_quote.get('10. change percent')
            )

        else:
            raise NotFoundError()
