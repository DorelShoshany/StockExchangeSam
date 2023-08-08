import logging
from typing import Union
from datetime import datetime, timedelta

from domain.modles import IPSource
from domain.repositories import IPsSourceRepository
from exceptions import LimitQueriesError
from globals import configuration

logging.basicConfig(level=logging.DEBUG)
internal_log = logging.getLogger()


class IPsSourceService:

    def __init__(self, ips_sources_repository: IPsSourceRepository, ):
        self.ips_sources_repository = ips_sources_repository

    def incr_number_requests_ip_source(self, ip_source: IPSource):
        query = {"ip": ip_source.ip}
        update = {
            "$inc": {"number_of_requests": 1},
            "$set": {"creation_time": ip_source.creation_time}
        }
        self.ips_sources_repository.find_one_and_update(query, update, upsert=True)

    def validate_limit_requests_per_ip(self, ip_source: IPSource):
        queries_configration = configuration.queries_configration
        max_size_queries = queries_configration.get('max_size_requests_per_ip', 10)
        max_minutes = queries_configration.get('max_minutes_per_max_queries', 10)
        now = datetime.now()
        ip_excessive_max_requests = \
            ip_source.number_of_requests >= max_size_queries \
            and now - ip_source.creation_time < timedelta(minutes=max_minutes)
        if ip_excessive_max_requests:
            raise LimitQueriesError

    def handle_ip_request(self, ip):
        queries_configration = configuration.queries_configration
        limit_requests_per_ip = queries_configration.get('limit_requests_per_ip', False)
        ip_source: Union[None, IPSource] = self.ips_sources_repository.find_one(ip)
        if limit_requests_per_ip and ip_source:
            self.validate_limit_requests_per_ip(ip_source)
        else:
            ip_source = IPSource(ip=ip)
        self.incr_number_requests_ip_source(ip_source)
        internal_log.debug(f'increase number of query for the ip source {ip}')
