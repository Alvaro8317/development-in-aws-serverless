"""
Utilidades para procesar pedidos.
Estas funciones SIMULAN la lógica de negocio real.
En producción, estas llamarían a APIs reales de inventario, pagos, etc.
"""

import logging
import random
import time
from typing import Any

logger = logging.getLogger()


def validate_stock(items: list[dict[str, Any]]) -> dict[str, Any]:
    """
    SIMULACIÓN: Valida disponibilidad de stock para los items del pedido.

    En producción, esto llamaría a un servicio de inventario real.
    Aquí simplemente simulamos que:
    - 80% de las veces hay stock disponible
    - 20% de las veces no hay stock (para demostrar el flujo de error)

    Args:
        items: Lista de items del pedido

    Returns:
        Dict con 'available' (bool) y 'reason' (str) si no está disponible
    """
    logger.info(f"🔍 Validando stock para {len(items)} items...")

    time.sleep(0.1)

    stock_available = random.random() > 0.2

    if stock_available:
        logger.info("✓ Stock disponible para todos los items")
        return {"available": True, "items_validated": len(items)}
    else:
        out_of_stock_item = random.choice(items)
        reason = f"Stock insuficiente para {out_of_stock_item['product_name']}"

        logger.warning(f"✗ {reason}")
        return {
            "available": False,
            "reason": reason,
            "out_of_stock_product": out_of_stock_item["product_id"],
        }


def calculate_total(items: list[dict[str, Any]]) -> dict[str, float]:
    """
    Calcula subtotal, impuestos y total del pedido.

    Args:
        items: Lista de items del pedido

    Returns:
        Dict con subtotal, tax y total
    """
    logger.info("💰 Calculando totales...")

    subtotal = sum(item["quantity"] * item["price"] for item in items)

    tax_rate = 0.19
    tax = round(subtotal * tax_rate, 2)

    total = round(subtotal + tax, 2)

    logger.info(f"Subtotal: ${subtotal:.2f}, Tax: ${tax:.2f}, Total: ${total:.2f}")

    return {"subtotal": subtotal, "tax": tax, "total": total}


def process_payment(order_id: str, amount: float, customer_id: str) -> dict[str, Any]:
    """
    SIMULACIÓN: Procesa el pago del pedido.

    En producción, esto integraría con Stripe, PayPal, etc.
    Aquí simulamos que:
    - 90% de las veces el pago es exitoso
    - 10% de las veces falla (tarjeta rechazada, fondos insuficientes, etc.)

    Args:
        order_id: ID del pedido
        amount: Monto a cobrar
        customer_id: ID del cliente

    Returns:
        Dict con 'success', 'payment_id' si exitoso, o 'error' si falla
    """
    logger.info(f"💳 Procesando pago de ${amount:.2f} para pedido {order_id}...")

    time.sleep(0.2)

    payment_successful = random.random() > 0.1

    if payment_successful:
        payment_id = f"PAY-{order_id}-{int(time.time())}"

        logger.info(f"✓ Pago procesado exitosamente. Payment ID: {payment_id}")

        return {
            "success": True,
            "payment_id": payment_id,
            "amount": amount,
            "currency": "USD",
            "method": "credit_card",
            "last_four": "4242",
        }
    else:
        errors = [
            "Tarjeta rechazada",
            "Fondos insuficientes",
            "Tarjeta expirada",
            "Error de conexión con el procesador de pagos",
        ]
        error_message = random.choice(errors)

        logger.warning(f"✗ Pago rechazado: {error_message}")

        return {
            "success": False,
            "error": error_message,
            "error_code": "PAYMENT_DECLINED",
        }


def reserve_inventory(items: list[dict[str, Any]], order_id: str) -> dict[str, Any]:
    """
    SIMULACIÓN: Reserva inventario para el pedido.

    En producción, esto actualizaría la base de datos de inventario.

    Args:
        items: Lista de items a reservar
        order_id: ID del pedido

    Returns:
        Dict con resultado de la reserva
    """
    logger.info(f"📦 Reservando inventario para pedido {order_id}...")

    time.sleep(0.1)

    reserved_items = []
    for item in items:
        reserved_items.append(
            {
                "product_id": item["product_id"],
                "quantity_reserved": item["quantity"],
                "reservation_id": f"RES-{order_id}-{item['product_id']}",
            }
        )

    logger.info(f"✓ Inventario reservado para {len(items)} items")

    return {"success": True, "reserved_items": reserved_items}


def send_confirmation_email(
    order_id: str, email: str, order_data: dict[str, Any]
) -> dict[str, Any]:
    """
    SIMULACIÓN: Envía email de confirmación al cliente.

    En producción, esto usaría AWS SES, SendGrid, etc.

    Args:
        order_id: ID del pedido
        email: Email del cliente
        order_data: Datos del pedido

    Returns:
        Dict con resultado del envío
    """
    logger.info(
        f"📧 Enviando email de confirmación a {email} para pedido {order_id}..."
    )

    time.sleep(0.05)

    logger.info(f"✓ Email de confirmación enviado a {email}")

    return {"success": True, "email": email, "message_id": f"MSG-{int(time.time())}"}


def log_order_summary(order_data: dict[str, Any]) -> None:
    """
    Registra un resumen del pedido en los logs.
    Útil para debugging y monitoreo.
    """
    logger.info("=" * 60)
    logger.info(f"📋 RESUMEN DEL PEDIDO: {order_data['order_id']}")
    logger.info(f"👤 Cliente: {order_data['customer_id']}")
    logger.info(f"📧 Email: {order_data['email']}")
    logger.info(f"📦 Items: {len(order_data['items'])}")

    for idx, item in enumerate(order_data["items"], 1):
        logger.info(
            f"   {idx}. {item['product_name']} x{item['quantity']} "
            f"@ ${item['price']:.2f} = ${item['quantity'] * item['price']:.2f}"
        )

    logger.info(f"💵 Total: ${order_data.get('total', 0):.2f}")
    logger.info(f"📊 Status: {order_data.get('status', 'PENDING')}")
    logger.info("=" * 60)
