"""
Utilidades para generar respuestas HTTP estandarizadas.
"""

import json
from typing import Any


def create_response(
    status_code: int, body: dict[str, Any], headers: dict[str, str] = None
) -> dict[str, Any]:
    """
    Crea una respuesta HTTP estandarizada para API Gateway.

    Args:
        status_code: Código de estado HTTP
        body: Cuerpo de la respuesta
        headers: Headers adicionales (opcional)

    Returns:
        Diccionario con formato esperado por API Gateway
    """
    default_headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True,
    }

    if headers:
        default_headers.update(headers)

    return {
        "statusCode": status_code,
        "headers": default_headers,
        "body": json.dumps(body, ensure_ascii=False),
    }


def success_response(data: dict[str, Any], status_code: int = 200) -> dict[str, Any]:
    """
    Crea una respuesta de éxito.

    Args:
        data: Datos a retornar
        status_code: Código de estado (por defecto 200)

    Returns:
        Respuesta HTTP de éxito
    """
    return create_response(status_code, data)


def error_response(
    message: str, status_code: int = 400, error_type: str = "ValidationError"
) -> dict[str, Any]:
    """
    Crea una respuesta de error.

    Args:
        message: Mensaje de error
        status_code: Código de estado (por defecto 400)
        error_type: Tipo de error

    Returns:
        Respuesta HTTP de error
    """
    return create_response(status_code, {"error": error_type, "message": message})
