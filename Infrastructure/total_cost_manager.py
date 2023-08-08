
class TotalCostManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_total_cost(self):
        try:
            with open(self.file_path, 'r') as file:
                total_cost = float(file.read())
            return total_cost
        except (FileNotFoundError, ValueError):
            return 0  # Default value if file doesn't exist or is invalid

    def write_total_cost(self, total_cost):
        with open(self.file_path, 'w') as file:
            file.write(str(total_cost))

    def increment(self, value=1):
        total_cost = self.read_total_cost()
        total_cost = total_cost + value
        self.write_total_cost(total_cost)
