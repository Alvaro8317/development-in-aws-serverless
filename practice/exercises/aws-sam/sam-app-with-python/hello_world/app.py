import json

import boto3

ssm = boto3.client("ssm")

response = ssm.get_parameter(
    Name="/sam/app/hello/world/java/db-password:2", WithDecryption=True
)
secret = response["Parameter"]["Value"]


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
                "response_of_ssm": secret,
                "new_value": "Hey there!",
            }
        ),
    }
