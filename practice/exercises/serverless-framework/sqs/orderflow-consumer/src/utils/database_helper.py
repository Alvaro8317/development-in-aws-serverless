"""
Utilidades para trabajar con DynamoDB.
"""

import logging
import os
from decimal import Decimal
from typing import Any, Dict

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Cliente de DynamoDB
dynamodb = boto3.resource("dynamodb")


def get_table():
    """Obtiene la referencia a la tabla de DynamoDB."""
    table_name = os.environ.get("ORDERS_TABLE_NAME")
    if not table_name:
        raise ValueError("ORDERS_TABLE_NAME no está configurada")
    return dynamodb.Table(table_name)


def convert_floats_to_decimal(obj: Any) -> Any:
    """
    Convierte floats a Decimal para DynamoDB.
    DynamoDB no soporta float nativo, necesita Decimal.

    Args:
        obj: Objeto a convertir (dict, list, float, etc.)

    Returns:
        Objeto con floats convertidos a Decimal
    """
    if isinstance(obj, float):
        return Decimal(str(obj))
    elif isinstance(obj, dict):
        return {k: convert_floats_to_decimal(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_floats_to_decimal(item) for item in obj]
    return obj


def convert_decimal_to_float(obj: Any) -> Any:
    """
    Convierte Decimal a float para serialización JSON.

    Args:
        obj: Objeto a convertir

    Returns:
        Objeto con Decimals convertidos a float
    """
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, dict):
        return {k: convert_decimal_to_float(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_decimal_to_float(item) for item in obj]
    return obj


def save_order(order: Dict[str, Any]) -> Dict[str, Any]:
    """
    Guarda un pedido en DynamoDB con idempotencia.

    Args:
        order: Diccionario con los datos del pedido

    Returns:
        Respuesta de DynamoDB

    Raises:
        Exception: Si hay error al guardar
    """
    try:
        table = get_table()

        # Convertir floats a Decimal
        order_item = convert_floats_to_decimal(order)

        # Guardar con condition expression para idempotencia
        # Solo crea el item si no existe O si existe pero está PENDING
        response = table.put_item(
            Item=order_item,
            ConditionExpression=(
                "attribute_not_exists(order_id) OR #status = :pending_status"
            ),
            ExpressionAttributeNames={"#status": "status"},
            ExpressionAttributeValues={":pending_status": "PENDING"},
        )

        logger.info(f"Pedido {order['order_id']} guardado en DynamoDB")
        return response

    except dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
        # El pedido ya fue procesado (no está PENDING)
        logger.info(
            f"Pedido {order['order_id']} ya fue procesado previamente. "
            "Ignorando duplicado (idempotencia)."
        )
        return {"message": "Duplicado ignorado"}

    except Exception as e:
        logger.error(f"Error guardando pedido en DynamoDB: {str(e)}")
        raise


def get_orders_by_customer(customer_id: str, limit: int = 10) -> list:
    """
    Obtiene pedidos de un cliente usando el GSI.

    Args:
        customer_id: ID del cliente
        limit: Número máximo de pedidos a retornar

    Returns:
        Lista de pedidos
    """
    try:
        table = get_table()

        response = table.query(
            IndexName="customer-index",
            KeyConditionExpression="customer_id = :customer_id",
            ExpressionAttributeValues={":customer_id": customer_id},
            Limit=limit,
            ScanIndexForward=False,  # Ordenar por fecha descendente (más recientes primero)
        )

        items = response.get("Items", [])

        # Convertir Decimal a float
        return [convert_decimal_to_float(item) for item in items]

    except Exception as e:
        logger.error(f"Error obteniendo pedidos del cliente {customer_id}: {str(e)}")
        raise


def update_order_status(order_id: str, new_status: str, **kwargs) -> Dict[str, Any]:
    """
    Actualiza el status de un pedido.

    Args:
        order_id: ID del pedido
        new_status: Nuevo status
        **kwargs: Campos adicionales a actualizar

    Returns:
        Pedido actualizado
    """
    try:
        table = get_table()

        # Construir expression
        update_expr = "SET #status = :status"
        expr_attr_names = {"#status": "status"}
        expr_attr_values = {":status": new_status}

        # Agregar campos adicionales
        for key, value in kwargs.items():
            update_expr += f", {key} = :{key}"
            expr_attr_values[f":{key}"] = convert_floats_to_decimal(value)

        response = table.update_item(
            Key={"order_id": order_id},
            UpdateExpression=update_expr,
            ExpressionAttributeNames=expr_attr_names,
            ExpressionAttributeValues=expr_attr_values,
            ReturnValues="ALL_NEW",
        )

        updated_item = response.get("Attributes", {})
        return convert_decimal_to_float(updated_item)

    except Exception as e:
        logger.error(f"Error actualizando pedido {order_id}: {str(e)}")
        raise
