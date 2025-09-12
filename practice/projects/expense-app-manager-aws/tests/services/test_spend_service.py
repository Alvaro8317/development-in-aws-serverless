from alvaro8317.models import base_repository, spend
from alvaro8317.services import spend_service


class TestSpendService:
    def test_create_spend(self) -> None:
        subject = spend_service.SpendService(base_repository.FakeRepositorySpend())
        result = subject.create_spend(name="Prueba", description="prueba", amount=12.12)
        assert isinstance(result, spend.Spend)
        assert result.name == "Prueba"

    def test_get_spends(self) -> None:
        subject = spend_service.SpendService(base_repository.FakeRepositorySpend())
        result = subject.get_spends()
        assert isinstance(result, list)
        for spend_got in result:
            assert isinstance(spend_got, spend.Spend)
