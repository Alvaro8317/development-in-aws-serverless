from alvaro8317.models import spend


def test_new_spend() -> None:
    subject = spend.Spend.new_spend(
        name="Mi primer gasto",
        amount=10500.25,
        description="Prueba unitaria de mi primer gasto",
    )
    assert isinstance(subject.amount, float)
