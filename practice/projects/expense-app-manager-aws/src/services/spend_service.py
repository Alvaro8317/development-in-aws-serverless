import decimal

from models import base_repository, spend


class SpendService:
    def __init__(self, repository: base_repository.BaseRepositorySpend):
        self.repository = repository

    def create_spend(
        self, name: str, description: str, amount: decimal.Decimal
    ) -> spend.Spend:
        spend_item = spend.Spend.new_spend(
            name=name, description=description, amount=amount
        )
        self.repository.create_spend(spend_item.as_dict())
        return spend_item  #

    def get_spends(self) -> list[spend.Spend]:
        return self.repository.get_spends()  #
