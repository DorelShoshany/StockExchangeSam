# from domain.modles.configuration import Configuration
# from domain.repositories import ConfigurationsRepository
#
#
# class ConfigurationsMongoDBRepository(ConfigurationsRepository):
#     def __init__(self, db):
#         self.configurations_collection = db["configurations"]
#         self.configuration_id = 'configuration'
#         super().__init__()
#         # init configuration
#         self.default_configuration = Configuration(
#             queries_configration={
#                 'limit_requests_per_ip': True,
#                 'max_size_requests_per_ip': 10,
#                 'max_minutes_per_max_queries': 10
#             },
#             stock_url_request=f"https://www.alphavantage.co"
#                               f"/query?function=GLOBAL_QUOTE&apikey=Y2R9RKOESRRHSO10&"
#                               f"symbol=",
#             cost_per_query=0.1,
#             stock_value_fresh=1.03,
#         )
#
#     def find_one(self) -> Configuration:
#         document = self.configurations_collection.find_one({"_id": self.configuration_id})
#         if not document:
#             self.insert_one(self.default_configuration)
#             return self.default_configuration
#
#         return Configuration(
#             queries_configration=document.get(
#                 'queries_configration', self.default_configuration.queries_configration
#             ),
#             cost_per_query=document.get(
#                 'cost_per_query', self.default_configuration.cost_per_query
#             ),
#             stock_url_request=document.get(
#                 'stock_url_request', self.default_configuration.stock_url_request
#             ),
#             stock_value_fresh=document.get(
#                 'stock_value_fresh', self.default_configuration.stock_value_fresh
#             ),
#         )
#
#     def insert_one(self, configuration: Configuration):
#         document: {} = self._to_document(configuration)
#         self.configurations_collection.insert_one(document)
#
#     def _to_document(self, configuration: Configuration) -> {}:
#         return {
#             '_id': self.configuration_id,
#             'queries_configration': configuration.queries_configration,
#             'cost_per_query': configuration.cost_per_query,
#             'stock_url_request': configuration.stock_url_request,
#             'stock_value_fresh': configuration.stock_value_fresh
#         }
