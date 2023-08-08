import logging
from typing import Union

from Infrastructure.stocks_requests_service import StocksRequestsService
from Infrastructure.total_cost_manager import TotalCostManager
from domain.modles.stock import Stock
from domain.services import StocksService, IPsSourceService
from globals import configuration, total_cost_file_path

logging.basicConfig(level=logging.DEBUG)
internal_log = logging.getLogger()


class StockUseCaseInterface:
    def get_stock(self, symbol: str, ip: str):
        pass


class StockUseCase(StockUseCaseInterface):
    stocks_requests_service: StocksRequestsService = None
    stocks_service: StocksService = None
    ips_sources_service: IPsSourceService = None

    def __init__(
            self,
            stocks_requests_service: StocksRequestsService,
            stocks_service: StocksService,
            ips_sources_service: IPsSourceService,
    ):
        self.ips_sources_service = ips_sources_service
        self.stocks_requests_service = stocks_requests_service
        self.stocks_service = stocks_service

    def get_stock(self, symbol_id: str, ip: str) -> Union[dict, None]:
        TotalCostManager(total_cost_file_path).increment(configuration.cost_per_query)
        self.ips_sources_service.handle_ip_request(ip)
        fresh_stock: Stock = self.stocks_service.get_fresh_stock(symbol_id)

        if fresh_stock:
            internal_log.debug('The stock is fresh')
            return fresh_stock.serialize()

        internal_log.debug('The stock is not fresh - call other server')
        stock: Stock = self.stocks_requests_service.get_stock_by_symbol_id(
            symbol_id=symbol_id
        )

        # or not exists and need to insert new one or not fresh need to update exists one
        self.stocks_service.save_stock(stock)
        return stock.serialize()
