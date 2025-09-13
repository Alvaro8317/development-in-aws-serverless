import decimal
import json
from dataclasses import dataclass

import pytest

from alvaro8317.entrypoints import spend as spend_module
from alvaro8317.models import base_repository


def test__json_default_decimal_and_dataclass() -> None:
    assert spend_module._json_default(decimal.Decimal("12.50")) == 12.5

    @dataclass
    class X:
        a: int
        b: str

    assert spend_module._json_default(X(1, "ok")) == {"a": 1, "b": "ok"}

    assert spend_module._json_default("hola") == "hola"


def test_spend_handler_success(monkeypatch: pytest.MonkeyPatch) -> None:
    """Valida que spend_handler:
    - parsee el body
    - llame a la capa de servicio con los argumentos correctos (amount como Decimal)
    - serialice el resultado usando _json_default
    - responda 200 con body JSON válido
    """

    calls = {}

    class FakeSpend:
        def __init__(
            self, name: str, description: str, amount: decimal.Decimal
        ) -> None:
            self.name = name
            self.description = description
            self.amount = amount

        def as_dict(self) -> dict:
            return {
                "id": "fake-id",
                "name": self.name,
                "description": self.description,
                "amount": float(self.amount),
            }

    class FakeService:
        def __init__(self, repository: base_repository.BaseRepositorySpend) -> None:
            self.repository = repository

        def create_spend(
            self, *, name: str, description: str, amount: decimal.Decimal
        ) -> FakeSpend:
            calls["args"] = {"name": name, "description": description, "amount": amount}
            return FakeSpend(name=name, description=description, amount=amount)

        def get_spends(self) -> None:
            raise AssertionError("No debería llamarse en este test")

    monkeypatch.setattr(spend_module.spend_service, "SpendService", FakeService)
    monkeypatch.setattr(
        spend_module.repo_dynamodb, "DynamoDbRepoSpend", lambda: object()
    )

    event = {
        "body": json.dumps({
            "name": "Prueba",
            "description": "prueba",
            "amount": "12.12",
        })
    }

    resp = spend_module.spend_handler(event, context=None)

    assert resp["statusCode"] == 200
    assert resp["headers"]["Content-Type"] == "application/json"

    body = json.loads(resp["body"])
    assert body["message"] == "Spend created succesfully"

    spend_created = body["spend_created"]
    assert spend_created["name"] == "Prueba"
    assert spend_created["description"] == "prueba"
    assert spend_created["amount"] == pytest.approx(12.12)

    assert isinstance(calls["args"]["amount"], decimal.Decimal)


def test_get_spend_handler_success(monkeypatch: pytest.MonkeyPatch) -> None:
    """Valida que get_spend_handler:
    - cree el servicio
    - retorne una lista serializable en 'spends'
    - responda 200 con body JSON válido
    """

    class FakeService:
        def __init__(self, repository: base_repository.BaseRepositorySpend) -> None:
            self.repository = repository

        def get_spends(self) -> None:
            return [
                {"id": "1", "name": "A", "description": "x", "amount": 10.0},
                {"id": "2", "name": "B", "description": "y", "amount": 20.5},
            ]

        def create_spend(self, *args: dict, **kwargs: dict) -> None:
            raise AssertionError("No debería llamarse en este test")

    monkeypatch.setattr(spend_module.spend_service, "SpendService", FakeService)
    monkeypatch.setattr(
        spend_module.repo_dynamodb, "DynamoDbRepoSpend", lambda: object()
    )

    resp = spend_module.get_spend_handler(event={}, context=None)

    assert resp["statusCode"] == 200
    assert resp["headers"]["Content-Type"] == "application/json"

    body = json.loads(resp["body"])
    spends = body["spends"]
    assert isinstance(spends, list)
    assert spends[0]["id"] == "1"
    assert spends[1]["amount"] == pytest.approx(20.5)
