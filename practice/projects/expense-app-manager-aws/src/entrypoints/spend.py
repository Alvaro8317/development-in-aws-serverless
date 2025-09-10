import decimal
import json
from typing import Any

from aws_lambda_powertools.utilities import typing
from models import repo_dynamodb
from services import spend_service


def _json_default(o):
    if isinstance(o, decimal.Decimal):
        return float(o)
    try:
        import dataclasses

        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
    except Exception:
        pass
    return str(o)


def spend_handler(event: dict[str, Any], context: typing.LambdaContext) -> dict:
    body = event.get("body")
    body_json: dict[str, str] = json.loads(body)
    repo = repo_dynamodb.DynamoDbRepoSpend()
    spend = spend_service.SpendService(repository=repo)
    spend_created = spend.create_spend(
        name=body_json.get("name"),
        description=body_json.get("description"),
        amount=decimal.Decimal(body_json.get("amount")),
    )
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(
            {
                "message": "Spend created succesfully",
                "spend_created": spend_created.as_dict(),
            },
            default=_json_default,
        ),
    }


def get_spend_handler(event: dict[str, Any], context: typing.LambdaContext) -> dict:
    repo = repo_dynamodb.DynamoDbRepoSpend()
    spend = spend_service.SpendService(repository=repo)
    spends = spend.get_spends()
    response = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(
            {
                "spends": spends,
            },
            default=_json_default,
        ),
    }
    return response
