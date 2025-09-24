import decimal
import json

from aws_lambda_powertools.utilities import typing
from aws_lambda_typing import events

from alvaro8317.models import repo_dynamodb
from alvaro8317.services import auth, spend_service, utils


@auth.with_auth
def spend_handler(
    event: events.APIGatewayProxyEventV2, context: typing.LambdaContext
) -> dict:
    body_json: dict = json.loads(event.get("body"))
    repo = repo_dynamodb.DynamoDbRepoSpend()
    spend = spend_service.SpendService(repository=repo)
    spend_created = spend.create_spend(
        name=body_json.get("name"),
        description=body_json.get("description"),
        amount=decimal.Decimal(body_json.get("amount")),
    )
    return {
        "statusCode": 200,
        "headers": utils.cors_headers(),
        "body": json.dumps(
            {
                "message": "Spend created succesfully",
                "spend_created": spend_created.as_dict(),
            },
            default=utils.json_default,
        ),
    }


@auth.with_auth
def get_spend_handler(
    event: events.APIGatewayProxyEventV2, context: typing.LambdaContext
) -> dict:
    repo = repo_dynamodb.DynamoDbRepoSpend()
    spend = spend_service.SpendService(repository=repo)
    spends = spend.get_spends()
    return {
        "statusCode": 200,
        "headers": utils.cors_headers(),
        "body": json.dumps({"spends": spends}, default=utils.json_default),
    }
