# exceptions.py

class NotFoundError(Exception):
    def __init__(self, message="Not found"):
        self.message = message
        super().__init__(self.message)


class ValidationError(Exception):
    def __init__(self, message="Validation error"):
        self.message = message
        super().__init__(self.message)


class LimitQueriesError(Exception):
    def __init__(self, message="specific IP source up to 10 queries per minute"):
        self.message = message
        super().__init__(self.message)