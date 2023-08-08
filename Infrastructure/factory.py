from Infrastructure.stocks_requests_service import StocksRequestsService
from Infrastructure.repositories import StocksMongoDBRepository, IPSourceMongoDBRepository
from domain.services import StocksService, IPsSourceService
from use_cases import TotalCostUseCase, StockUseCase


class Factory:
    def __init__(self, db_client):
        # create repository
        self.symbols_repository = StocksMongoDBRepository(db=db_client)
        self.ips_source_repository = IPSourceMongoDBRepository(db=db_client)

        # create services
        self.stocks_service = StocksService(stocks_repository=self.symbols_repository)
        self.stocks_requests_service = StocksRequestsService()
        self.ips_sources_service = IPsSourceService(ips_sources_repository=self.ips_source_repository)

        # create use cases
        self.stock_use_case = StockUseCase(
            stocks_service=self.stocks_service,
            stocks_requests_service=self.stocks_requests_service,
            ips_sources_service=self.ips_sources_service,
        )

        self.total_cost_use_case = TotalCostUseCase()
