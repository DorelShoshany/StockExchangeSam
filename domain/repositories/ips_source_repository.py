from abc import ABC

from domain.modles.ip_source import IPSource


class IPsSourceRepository(ABC):
    def __init__(self):
        ...

    def find_one(self, ip: str) -> IPSource:
        ...

    def insert_one(self, Source_ip: IPSource):
        ...

    def update_one(self, source_ip: IPSource):
        ...

    def find_one_and_update(self, query, update, upsert=True):
        ...
