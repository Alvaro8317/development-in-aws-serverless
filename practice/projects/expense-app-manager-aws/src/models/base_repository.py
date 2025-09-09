import abc

from models import spend


class BaseRepositorySpend:
    @abc.abstractmethod
    def create_spend(self, item: dict[str, str | float]) -> spend.Spend:
        pass

    @abc.abstractmethod
    def get_spends(self) -> list[spend.Spend]:
        pass
