# ----- Ajusta estas variables -----
REGION="us-east-1"
ORDERS_TABLE="orders-table-v2-dev"

aws dynamodb batch-write-item --request-items file://batch-orders-v2.json --region "$REGION" --output json --return-consumed-capacity TOTAL --profile local
aws dynamodb batch-write-item --request-items file://batch-orders-2-v2.json --region "$REGION" --output json --return-consumed-capacity TOTAL --profile local

aws dynamodb query \
  --table-name "$ORDERS_TABLE" \
  --profile local \
  --region "$REGION" \
  --key-condition-expression "userId = :uid AND orderId = :orid" \
  --expression-attribute-values file://key-order.json

# Por status dentro de un mismo userId (LSIByStatus)
aws dynamodb query \
  --table-name "$ORDERS_TABLE" \
  --profile local \
  --region "$REGION" \
  --index-name "LSIByStatus" \
  --key-condition-expression "userId = :u AND #st = :s" \
  --expression-attribute-names '{"#st":"status"}' \
  --expression-attribute-values '{
    ":u": {"S":"U-001Udemy"},
    ":s": {"S":"INACTIVE"}
  }'

# Por rango de fechas dentro de un userId (LSIByCreationDate)
aws dynamodb query \
  --table-name "$ORDERS_TABLE" \
  --profile local \
  --region "$REGION" \
  --index-name "LSIByCreationDate" \
  --key-condition-expression "userId = :u AND createdAt BETWEEN :from AND :to" \
  --expression-attribute-values '{
    ":u":    {"S":"U-001Udemy"},
    ":from": {"S":"2025-10-29T00:00:00Z"},
    ":to":   {"S":"2025-10-31T23:59:59Z"}
  }'
