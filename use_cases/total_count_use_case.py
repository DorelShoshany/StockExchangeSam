from Infrastructure.total_cost_manager import TotalCostManager
from globals import total_cost_file_path


class TotalCountUseCaseInterface:
    def get_total_count(self):
        ...

    def reset_total_count(self):
        ...


class TotalCostUseCase(TotalCountUseCaseInterface):

    def get_total_count(self) -> float:
        manager = TotalCostManager(total_cost_file_path)
        return manager.read_total_cost()

    def reset_total_count(self):
        manager = TotalCostManager(total_cost_file_path)
        manager.write_total_cost(0)
