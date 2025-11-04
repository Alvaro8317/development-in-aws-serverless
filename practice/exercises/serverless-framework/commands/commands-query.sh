# ----- Ajusta estas variables -----
REGION="us-east-1"
USERS_TABLE="users-table-dev"
ORDERS_TABLE="orders-table-dev"

aws dynamodb query \
  --table-name "$USERS_TABLE" \
  --profile local \
  --region "$REGION" \
  --key-condition-expression "userId = :useid" \
  --expression-attribute-values '{
    ":useid": {"S": "U-004Udemy"}
  }'

aws dynamodb query \
  --table-name "$ORDERS_TABLE" \
  --profile local \
  --region "$REGION" \
  --key-condition-expression "userId = :uid AND orderId = :orid" \
  --expression-attribute-values file://key-order.json

aws dynamodb query \
  --table-name "$ORDERS_TABLE" \
  --profile local \
  --region "$REGION" \
  --key-condition-expression "userId = :uid" \
  --expression-attribute-values '{
    ":uid": {"S": "U-001Udemy"}
  }'
