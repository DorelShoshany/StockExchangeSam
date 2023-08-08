class Configuration:
    def __init__(
            self,
            queries_configration: dict,
            stock_url_request: str,
            cost_per_query: float,
            stock_value_fresh: float
    ):
        self.queries_configration = queries_configration
        self.stock_url_request = stock_url_request
        self.cost_per_query = cost_per_query
        self.stock_value_fresh = stock_value_fresh
