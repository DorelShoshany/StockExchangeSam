from typing import Union

from domain.modles.ip_source import IPSource
from domain.repositories import IPsSourceRepository


class IPSourceDictRepository(IPsSourceRepository):
    def __init__(self):
        self.ip_sources: dict = {}
        super().__init__()

    def find_one(self, ip: str) -> Union[IPSource, None]:
        return self.ip_sources.get(ip)

    def insert_one(self, source_ip: IPSource):
        self.ip_sources[source_ip.ip] = source_ip

    def update_one(self, source_ip: IPSource):
        self.ip_sources[source_ip.ip] = source_ip
