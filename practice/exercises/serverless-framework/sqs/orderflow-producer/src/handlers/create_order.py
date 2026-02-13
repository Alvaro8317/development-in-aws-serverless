"""
Handler para crear pedidos.
Recibe pedidos vía API Gateway y los envía a SQS.
"""

import json
import logging
from typing import Any

import pydantic
from aws_lambda_powertools.utilities import typing

from src.models import order
from src.utils import response, sqs_helper

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event: dict[str, Any], context: typing.LambdaContext):
    """
    Handler de Lambda para crear pedidos.

    Este handler:
    1. Recibe el pedido vía API Gateway (HTTP POST)
    2. Valida los datos usando Pydantic
    3. Genera un Order con ID único y timestamp
    4. Envía el pedido a SQS
    5. Retorna respuesta inmediata al cliente con status PENDING

    Args:
        event: Evento de API Gateway
        context: Contexto de Lambda

    Returns:
        Respuesta HTTP con el resultado
    """
    try:
        logger.info(f"Evento recibido: {json.dumps(event)}")

        if not event.get("body"):
            return response.error_response(
                message="El body del request está vacío", status_code=400
            )

        try:
            body = json.loads(event["body"])
        except json.JSONDecodeError as e:
            return response.error_response(
                message=f"JSON inválido: {str(e)}", status_code=400
            )

        try:
            order_request = order.CreateOrderRequest(**body)
        except pydantic.ValidationError as e:
            errors = []
            for error in e.errors():
                field = " -> ".join(str(loc) for loc in error["loc"])
                errors.append(f"{field}: {error['msg']}")

            return response.error_response(
                message="Errores de validación: " + "; ".join(errors),
                status_code=400,
                error_type="ValidationError",
            )

        order_request = order.Order.from_request(order_request)

        logger.info(f"Pedido creado: {order_request.order_id}")

        try:
            message_id = sqs_helper.send_order_to_queue(order_request.model_dump())
            logger.info(f"Pedido enviado a SQS. MessageId: {message_id}")
        except Exception as e:
            logger.error(f"Error al enviar a SQS: {str(e)}")
            return response.error_response(
                message="Error al procesar el pedido. Por favor intenta nuevamente.",
                status_code=500,
                error_type="InternalServerError",
            )

        response_order = order.CreateOrderResponse(
            order_id=order_request.order_id,
            status=order_request.status,
            message="Tu pedido está siendo procesado",
            total=order_request.total,
            created_at=order_request.created_at,
        )

        return response.success_response(
            data=response_order.model_dump(), status_code=201
        )

    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}", exc_info=True)
        return response.error_response(
            message="Error interno del servidor",
            status_code=500,
            error_type="InternalServerError",
        )
