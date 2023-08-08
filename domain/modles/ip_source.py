from datetime import datetime


class IPSource:
    def __init__(self, ip: str):
        self.ip = ip
        self.number_of_requests = 0
        self.creation_time = datetime.now()  # Initialize to None or set to a specific datetime

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value

    @property
    def number_of_requests(self):
        return self._number_of_requests

    @number_of_requests.setter
    def number_of_requests(self, value):
        self._number_of_requests = value

    @property
    def creation_time(self):
        return self._creation_time

    @creation_time.setter
    def creation_time(self, value):
        self._creation_time = value
