#!/usr/bin/env bash

# ----- Ajusta estas variables -----
REGION="us-east-1"
USERS_TABLE="users-table-dev"
ORDERS_TABLE="orders-table-dev"

aws dynamodb put-item \
  --table-name "$USERS_TABLE" \
  --region "$REGION" \
  --item '{
    "userId":   {"S":"U-004Udemy"},
    "email":    {"S":"alvaro@example.com"},
    "name":     {"S":"Alvaro Garzón"},
    "webpage":     {"S":"https://alvaro8317.lat/"},
    "createdAt":{"S":"2025-10-28T15:00:00Z"}
  }' \
  --profile local

# ----- Ordenes -----


aws dynamodb put-item \
  --table-name "$ORDERS_TABLE" \
  --region "$REGION" \
  --item '{
    "userId":  {"S": "U-001Udemy"},
    "orderId": {"S": "O1001"},
    "status":  {"S": "PENDING"},
    "total":   {"N": "99.99"},
    "currency":{"S": "USD"},
    "items":   {"L": [
                  {"S": "Mouse"},
                  {"S": "Keyboard"}
                ]},
    "createdAt": {"S": "2025-10-28T15:00:00Z"}
  }' \
  --return-consumed-capacity TOTAL

aws dynamodb put-item \
  --table-name "$ORDERS_TABLE" \
  --region "$REGION" \
  --item '{
    "userId":  {"S": "U-001Udemy"},
    "orderId": {"S": "O1002"},
    "status":  {"S": "ACTIVE"},
    "total":   {"N": "35.000"},
    "currency":{"S": "COP"},
    "items":   {"L": [
                  {"S": "Desarrollo serverless con AWS - De cero a experimentado"},
                  {"S": "De cero a contratado - Cómo usar IA para conseguir trabajo"}
                ]},
    "createdAt": {"S": "2025-10-28T15:00:00Z"}
  }'

# --- LLAMADOS A LAS APIs DE DYNAMODB --- #

# Scan

aws dynamodb scan \
  --table-name "$USERS_TABLE" \
  --return-consumed-capacity TOTAL \
  --region "$REGION" \
  --profile local

# Put item

aws dynamodb put-item \
  --table-name "$USERS_TABLE" \
  --region "$REGION" \
  --item '{
    "userId":   {"S":"U-003Udemy"},
    "email":    {"S":"alvaro@example.com"},
    "name":     {"S":"Alvaro Garzón"},
    "webpage":     {"S":"https://alvaro8317.lat/"},
    "createdAt":{"S":"2025-10-28T15:00:00Z"}
  }' \
  --profile local

# Put item con condición de expresiones

aws dynamodb put-item \
  --table-name "$USERS_TABLE" \
  --region "$REGION" \
  --item '{
    "userId":   {"S":"U-004Udemy"},
    "email":    {"S":"alvaro@example.com"},
    "name":     {"S":"Alvaro Garzón"},
    "webpage":     {"S":"https://alvaro8317.lat/"},
    "createdAt":{"S":"2025-10-28T15:00:00Z"}
  }' \
  --condition-expression "attribute_exists(userId)" \
  --profile local

# --- return-consumed-capacity TOTAL --- #

aws dynamodb batch-write-item --request-items file://batch-orders.json --region "$REGION" --output json --return-consumed-capacity TOTAL --profile local
aws dynamodb batch-write-item --request-items file://batch-orders-2.json --region "$REGION" --output json --return-consumed-capacity TOTAL --profile local

# Get item

aws dynamodb get-item \
  --table-name "$USERS_TABLE" \
  --region "$REGION" \
  --key '{
    "userId":   {"S":"U-004Udemy"}
    }' \
  --profile local

aws dynamodb get-item \
  --table-name "$USERS_TABLE" \
  --region "$REGION" \
  --key file://key-user.json \
  --profile local

aws dynamodb get-item \
  --table-name "$ORDERS_TABLE" \
  --region "$REGION" \
  --key '{
    "userId":  {"S": "U-001Udemy"},
    "orderId": {"S": "O1002"}
    }' \
  --profile local