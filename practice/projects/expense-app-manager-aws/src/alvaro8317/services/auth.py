import base64
import functools
import json
import os
from typing import Any, Callable

import boto3
from aws_lambda_powertools.utilities import typing
from mypy_boto3_ssm import Client

from alvaro8317.services import utils


class InvalidAuth(Exception): ...


def get_username_and_password(authorization: str) -> tuple:
    if not authorization:
        raise InvalidAuth()
    _, b64_encoded_data = authorization.split(" ")
    result = base64.b64decode(b64_encoded_data).decode("utf-8")
    return result.split(":")


def can_invoke_response(headers: dict[str, str]) -> bool:
    client: Client = boto3.client("ssm")
    parameter_username = os.getenv("SSM_USERNAME")
    parameter_password = os.getenv("SSM_PASSWORD")
    response_username = client.get_parameter(
        Name=parameter_username, WithDecryption=False
    )
    response_password = client.get_parameter(
        Name=parameter_password, WithDecryption=True
    )
    username, password = get_username_and_password(headers.get("Authorization"))
    is_same_user = response_username.get("Parameter").get("Value") == username
    is_same_password = response_password.get("Parameter").get("Value") == password
    result = is_same_user and is_same_password
    return result


def with_auth(handler: Callable) -> Callable:
    """Decorador para validar autorización antes de ejecutar el handler"""

    @functools.wraps(handler)
    def wrapper(event: dict[str, Any], context: typing.LambdaContext) -> dict:
        headers = event.get("headers")
        try:
            if not can_invoke_response(headers=headers):
                return {
                    "statusCode": 401,
                    "headers": utils.cors_headers(),
                    "body": json.dumps(
                        {"message": "Unauthorized"}, default=utils.json_default
                    ),
                }
        except InvalidAuth:
            return {
                "statusCode": 400,
                "headers": utils.cors_headers(),
                "body": json.dumps(
                    {"message": "Invalid credentials"}, default=utils.json_default
                ),
            }
        except Exception as e:
            return {
                "statusCode": 500,
                "headers": utils.cors_headers(),
                "body": json.dumps(
                    {"message": f"Unexpected error: {str(e)}"},
                    default=utils.json_default,
                ),
            }
        return handler(event, context)

    return wrapper
