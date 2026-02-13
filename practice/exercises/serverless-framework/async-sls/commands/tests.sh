# Petición de prueba
curl https://TU_HTTP_API_ID.execute-api.us-east-1.amazonaws.com/

# Creación de transacciones financieras
for i in {1..20}; do
    curl -s -o /dev/null -w "%{http_code}\n" \
        -X POST "https://TU_HTTP_API_ID.execute-api.us-east-1.amazonaws.com/transactions" \
        -H "content-type: application/json" \
        -d '{"amount": 42000, "merchantId":"m_777", "userId":"u_1234", "idempotencyKey":"idem-demo-1"}'
done
