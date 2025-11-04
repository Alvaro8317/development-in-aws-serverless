# ----- Ajusta estas variables -----
REGION="us-east-1"
ORDERS_TABLE="orders-table-dev"

# Escaneo
aws dynamodb scan \
  --table-name "$ORDERS_TABLE" \
  --region "$REGION" \
  --return-consumed-capacity TOTAL \
  --profile local

# ¿Si está bien este comando?
aws dynamodb scan \
  --table-name "$ORDERS_TABLE" \
  --region "$REGION" \
  --filter-expression "status = :s" \
  --expression-attribute-values '{
    ":s": {"S": "INACTIVE"}
  }' \
  --return-consumed-capacity TOTAL \
  --profile local

# Solución error
aws dynamodb scan \
  --table-name "$ORDERS_TABLE" \
  --region "$REGION" \
  --filter-expression "#st = :s" \
  --expression-attribute-names '{
  "#st": "status"
  }' \
  --expression-attribute-values '{
  ":s": {"S": "INACTIVE"}
  }' \
  --return-consumed-capacity TOTAL \
  --profile local

# Resumen ejecutivo
aws dynamodb scan \
  --table-name "$ORDERS_TABLE" \
  --region "$REGION" \
  --filter-expression "#st = :s" \
  --expression-attribute-names '{
  "#st": "status"
    }' \
  --expression-attribute-values '{":s":{"S":"INACTIVE"}}' \
  --return-consumed-capacity TOTAL \
  --profile local \
  --output json \
| jq '{count:.Count, scanned:.ScannedCount, rcu:.ConsumedCapacity.CapacityUnits}'
