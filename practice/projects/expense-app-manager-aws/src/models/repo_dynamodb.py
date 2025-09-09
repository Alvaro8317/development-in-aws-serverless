import os

import boto3
from models import base_repository, spend


def _get_dynamo_table():
    table_name = os.environ.get("TABLE_NAME")
    print("Nombre de la tabla:", table_name)

    is_local = os.environ.get("IS_LOCAL_ENVIRONMENT", "false").lower() == "true"

    if is_local:
        print("La BD es local")
        endpoint = os.environ.get("DDB_ENDPOINT", "http://host.docker.internal:8000")
        dynamo = boto3.resource(
            "dynamodb",
            endpoint_url=endpoint,
            region_name=os.getenv("AWS_REGION", "us-east-1"),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", "dummy"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", "dummy"),
        )
    else:
        print("La BD NO es local")
        dynamo = boto3.resource("dynamodb")

    table = dynamo.Table(table_name)
    print("Endpoint efectivo:", table.meta.client.meta.endpoint_url)
    print("Nombre de _TABLE:", table)
    return table


_TABLE = _get_dynamo_table()
print("Nombre de _TABLE: ", _TABLE)


class DynamoDbRepoSpend(base_repository.BaseRepositorySpend):
    def create_spend(self, item: dict[str, str | float]):
        item_to_return = _TABLE.put_item(Item=item)
        return item_to_return

    def get_spends(self) -> list[spend.Spend]:
        return _TABLE.scan()
