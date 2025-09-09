from src.services import spend_service

class TestSpendService:

    def test_create_spend(self):
        subject = spend_service.SpendService("Fake repository")
        subject.create_spend(name="Prueba", description="prueba", amount=12.12)
