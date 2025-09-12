import abc
import decimal

from alvaro8317.models import spend


class BaseRepositorySpend:
    @abc.abstractmethod
    def create_spend(self, item: dict[str, str | float]) -> spend.Spend:
        pass

    @abc.abstractmethod
    def get_spends(self) -> list[spend.Spend]:
        pass


class FakeRepositorySpend(BaseRepositorySpend):
    _FAKE_SPEND = spend.Spend.new_spend(
        name="Gasto falso",
        amount=decimal.Decimal("120"),
        description="Descripción falsa",
    )

    def create_spend(self, item: dict[str, str | float]) -> spend.Spend:
        return self._FAKE_SPEND

    def get_spends(self) -> list[spend.Spend]:
        return [self._FAKE_SPEND, self._FAKE_SPEND]
