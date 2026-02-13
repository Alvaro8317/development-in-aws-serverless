curl -X POST https://[tu-api-id].execute-api.us-east-1.amazonaws.com/dev/orders \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "CUST-12345",
    "email": "cliente@example.com",
    "items": [
      {
        "product_id": "PROD-001",
        "product_name": "Laptop HP Pavilion",
        "quantity": 1,
        "price": 899.99
      }
    ]
  }'