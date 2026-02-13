"""
Modelos Pydantic para validación de datos de pedidos.
"""

import uuid
from datetime import datetime

import pydantic


class OrderItem(pydantic.BaseModel):
    """Representa un item individual en el pedido."""

    product_id: str = pydantic.Field(
        ..., min_length=1, max_length=100, description="ID único del producto"
    )
    product_name: str = pydantic.Field(
        ..., min_length=1, max_length=200, description="Nombre del producto"
    )
    quantity: int = pydantic.Field(
        ..., gt=0, le=100, description="Cantidad del producto (1-100)"
    )
    price: float = pydantic.Field(..., gt=0, description="Precio unitario del producto")

    @pydantic.field_validator("price")
    @classmethod
    def validate_price(cls, v):
        """Valida que el precio tenga máximo 2 decimales."""
        if round(v, 2) != v:
            raise ValueError("El precio debe tener máximo 2 decimales")
        return v

    def get_subtotal(self) -> float:
        """Calcula el subtotal del item."""
        return round(self.quantity * self.price, 2)


class CreateOrderRequest(pydantic.BaseModel):
    """Request para crear un nuevo pedido."""

    customer_id: str = pydantic.Field(
        ..., min_length=1, max_length=100, description="ID único del cliente"
    )
    email: pydantic.EmailStr = pydantic.Field(
        ..., description="Email del cliente para notificaciones"
    )
    items: list[OrderItem] = pydantic.Field(
        ...,
        min_length=1,
        max_length=50,
        description="Lista de items del pedido (1-50 items)",
    )

    @pydantic.field_validator("items")
    @classmethod
    def validate_items_not_empty(cls, v):
        """Valida que haya al menos un item."""
        if not v:
            raise ValueError("El pedido debe tener al menos un item")
        return v

    def get_total(self) -> float:
        """Calcula el total del pedido."""
        return round(sum(item.get_subtotal() for item in self.items), 2)


class Order(pydantic.BaseModel):
    """Modelo completo del pedido que se enviará a SQS."""

    order_id: str = pydantic.Field(
        default_factory=lambda: f"ORD-{uuid.uuid4().hex[:12].upper()}",
        description="ID único del pedido",
    )
    customer_id: str
    email: pydantic.EmailStr
    items: list[OrderItem]
    total: float = pydantic.Field(..., description="Total del pedido")
    status: str = pydantic.Field(default="PENDING", description="Estado del pedido")
    created_at: str = pydantic.Field(
        default_factory=lambda: datetime.utcnow().isoformat() + "Z",
        description="Timestamp de creación en formato ISO 8601",
    )

    @classmethod
    def from_request(cls, request: CreateOrderRequest) -> "Order":
        """Crea un Order desde un CreateOrderRequest."""
        return cls(
            customer_id=request.customer_id,
            email=request.email,
            items=request.items,
            total=request.get_total(),
        )


class CreateOrderResponse(pydantic.BaseModel):
    """Respuesta al crear un pedido."""

    order_id: str
    status: str
    message: str
    total: float
    created_at: str
