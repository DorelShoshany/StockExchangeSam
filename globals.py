import os

from domain.modles.configuration import Configuration

# data_directory = os.path.join(os.path.dirname(__file__), 'data')
total_cost_file_path = ('total_cost.txt')
configuration = Configuration(
            queries_configration={
                'limit_requests_per_ip': True,
                'max_size_requests_per_ip': 10,
                'max_minutes_per_max_queries': 10
            },
            stock_url_request=f"https://www.alphavantage.co"
                              f"/query?function=GLOBAL_QUOTE&apikey=Y2R9RKOESRRHSO10&"
                              f"symbol=",
            cost_per_query=0.1,
            stock_value_fresh=1.03,
        )