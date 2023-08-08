from typing import Union

from domain.modles.ip_source import IPSource
from domain.repositories import IPsSourceRepository


class IPSourceMongoDBRepository(IPsSourceRepository):
    def __init__(self, db):
        self.ip_sources_collection = db["ips_source"]
        self.ip_sources_collection.create_index([("ip", 1)])
        self.ip_sources_collection.create_index("creation_time", expireAfterSeconds=600)
        super().__init__()

    def find_one(self, ip: str) -> Union[IPSource, None]:
        document = self.ip_sources_collection.find_one({"ip": ip})
        if document:
            ip_source = IPSource(document.get("ip"))
            ip_source.creation_time = document.get('creation_time')
            ip_source.number_of_requests = document.get('number_of_requests')
            return ip_source
        return None

    def insert_one(self, source_ip: IPSource):
        document: {} = self._to_document(source_ip)
        self.ip_sources_collection.insert_one(document)

    def update_one(self, source_ip: IPSource):
        document: {} = self._to_document(source_ip)
        self.ip_sources_collection.replace_one({"ip": source_ip.ip}, document)

    def _to_document(self, source_ip: IPSource) -> {}:
        return {
            "ip": source_ip.ip,
            "creation_time": source_ip.creation_time,
            "number_of_requests": source_ip.number_of_requests,
        }

    def find_one_and_update(self, query, update, upsert=True):
        self.ip_sources_collection.find_one_and_update(filter=query, update=update, upsert=upsert)