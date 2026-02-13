"""
Utilidades para trabajar con AWS SQS.
"""

import json
import logging
import os
from typing import Any

import boto3
import mypy_boto3_sqs

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sqs_client: mypy_boto3_sqs.Client = boto3.client("sqs")


def send_message_to_sqs(
    queue_url: str,
    message_body: dict[str, Any],
    message_attributes: dict[str, Any] = None,
) -> dict[str, Any]:
    """
    Envía un mensaje a una cola SQS.

    Args:
        queue_url: URL de la cola SQS
        message_body: Cuerpo del mensaje (será convertido a JSON)
        message_attributes: Atributos adicionales del mensaje (opcional)

    Returns:
        Respuesta de SQS con MessageId

    Raises:
        Exception: Si hay error al enviar el mensaje
    """
    try:
        params = {
            "QueueUrl": queue_url,
            "MessageBody": json.dumps(message_body, ensure_ascii=False),
        }

        if message_attributes:
            params["MessageAttributes"] = message_attributes

        response = sqs_client.send_message(**params)

        logger.info(f"Mensaje enviado a SQS. MessageId: {response['MessageId']}")

        return response

    except Exception as e:
        logger.error(f"Error al enviar mensaje a SQS: {str(e)}")
        raise


def send_order_to_queue(order: dict[str, Any]) -> str:
    """
    Envía un pedido a la cola de pedidos.

    Args:
        order: Diccionario con los datos del pedido

    Returns:
        MessageId del mensaje enviado
    """
    queue_url = os.environ.get("ORDERS_QUEUE_URL")

    if not queue_url:
        raise ValueError(
            "ORDERS_QUEUE_URL no está configurada en las variables de entorno"
        )

    message_attributes = {
        "OrderId": {
            "StringValue": order.get("order_id", "UNKNOWN"),
            "DataType": "String",
        },
        "CustomerId": {
            "StringValue": order.get("customer_id", "UNKNOWN"),
            "DataType": "String",
        },
    }

    response = send_message_to_sqs(
        queue_url=queue_url, message_body=order, message_attributes=message_attributes
    )

    return response["MessageId"]
