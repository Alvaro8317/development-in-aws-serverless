import os

import boto3
from mypy_boto3_dynamodb import service_resource, type_defs

from alvaro8317.models import base_repository, spend


def _get_dynamo_table() -> service_resource.Table:
    table_name = os.environ.get("TABLE_NAME")

    is_local = os.environ.get("IS_LOCAL_ENVIRONMENT", "false").lower() == "true"

    if is_local:
        endpoint = os.environ.get("DDB_ENDPOINT", "http://host.docker.internal:8000")
        dynamo = boto3.resource(
            "dynamodb",
            endpoint_url=endpoint,
            region_name=os.getenv("AWS_REGION", "us-east-1"),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", "dummy"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", "dummy"),
        )
    else:
        dynamo = boto3.resource("dynamodb")

    table = dynamo.Table(table_name)
    return table


class DynamoDbRepoSpend(base_repository.BaseRepositorySpend):
    def __init__(self) -> None:
        self._table: service_resource.Table = _get_dynamo_table()

    def create_spend(
        self, item: dict[str, str | float]
    ) -> type_defs.PutItemOutputTableTypeDef:
        item_to_return = self._table.put_item(Item=item)
        return item_to_return

    def get_spends(self) -> list[spend.Spend]:
        return self._table.scan()
