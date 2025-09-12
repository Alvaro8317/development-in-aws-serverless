"""Este código contiene el modelo de la base de datos de un gasto"""

import dataclasses
import decimal
import typing
import uuid
from datetime import datetime, timezone


@dataclasses.dataclass
class Spend:
    id: str
    name: str
    description: str | None
    amount: float
    datetime_spend: str

    @staticmethod
    def new_spend(
        name: str, amount: decimal.Decimal, description: str | None
    ) -> "Spend":
        iso = datetime.now(timezone.utc).date().isoformat()
        return Spend(
            id=str(uuid.uuid4()),
            name=name,
            description=description,
            amount=amount,
            datetime_spend=iso,
        )

    def as_dict(self) -> dict[str, str | float]:
        return dataclasses.asdict(self)

    def __iter__(self) -> typing.Generator:
        yield from dataclasses.asdict(self).items()
