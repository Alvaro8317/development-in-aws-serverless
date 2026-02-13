import json
import logging
import random
import time
from typing import Any

from aws_lambda_powertools.utilities import typing
from aws_lambda_typing import events

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event: events.SQSEvent, context: typing.LambdaContext) -> None:
    logger.info(f"Procesando batch de {len(event['Records'])} mensajes")

    batch_item_failures = []

    for record in event.get("Records"):
        message_id = record["messageId"]

        try:
            body: dict[str, Any] = json.loads(record.get("body"))

            logger.info(f"Procesando pedido {body.get('order_id', 'UNKNOWN')}")

            result = process_order()

            if result["success"]:
                logger.info(
                    f"✓ Pedido {body['order_id']} procesado exitosamente. "
                    f"Status: {result['status']}"
                )
            else:
                logger.error(f"✗ Pedido {body['order_id']} falló: {result['error']}")

                batch_item_failures.append({"itemIdentifier": message_id})

        except Exception as e:
            logger.error(
                f"Error procesando mensaje {message_id}: {str(e)}", exc_info=True
            )
            batch_item_failures.append({"itemIdentifier": message_id})

    logger.info(
        f"Batch procesado. Exitosos: {len(event['Records']) - len(batch_item_failures)}, "
        f"Fallidos: {len(batch_item_failures)}"
    )
    return {"batchItemFailures": batch_item_failures}


def process_order() -> dict[str, str | bool]:
    i_am_lucky: bool = random.choices(population=[True, False], weights=[1, 4])[0]
    if i_am_lucky:
        return {
            "success": True,
            "status": "COMPLETED",
            "message": "Pedido procesado",
        }
    return {
        "success": False,
        "status": "FAILED",
        "error": "Falló porque no soy suertudo",
        "message": "Pedido fallido",
    }
