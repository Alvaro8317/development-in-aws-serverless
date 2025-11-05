# Solución - PlasticWorld: Índices, consultas y creatividad con DynamoDB

Oye, ¿Ya intentaste hacer el lab por tu cuenta? Revisa este archivo solo si te estancaste o tienes dudas de algo puntual, la idea es que tú mismo/a hagas este lab, animo que sé que puedes. 😉😉

No siendo más, te dejo la solución:

## Paso 1:

```yml
...
resources:
  Resources:
    PlasticWorldTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: PlasticWorld
        BillingMode: PAY_PER_REQUEST
        AttributeDefinitions:
          - AttributeName: artistId
            AttributeType: S
          - AttributeName: creationId
            AttributeType: S
          - AttributeName: likes
            AttributeType: N
          - AttributeName: category
            AttributeType: S
          - AttributeName: color
            AttributeType: S
        KeySchema:
          - AttributeName: artistId
            KeyType: HASH
          - AttributeName: creationId
            KeyType: RANGE

        # LSI (debe crearse junto con la tabla)
        LocalSecondaryIndexes:
          - IndexName: LikesIndex
            KeySchema:
              - AttributeName: artistId
                KeyType: HASH
              - AttributeName: likes
                KeyType: RANGE
            Projection:
              ProjectionType: ALL
```

## Paso 2:
Put item (5 items distintos)
```bash
aws dynamodb put-item \
  --table-name PlasticWorld \
  --item '{
    "artistId":   {"S":"A-001"},
    "creationId": {"S":"C-1001"},
    "category":   {"S":"Animal"},
    "color":      {"S":"Azul"},
    "likes":      {"N":"45"},
    "createdAt":  {"S":"2025-11-03T10:00:00Z"}
  }' \
  --return-consumed-capacity TOTAL
```

BatchWriteItem (5 items distintos)
```bash
aws dynamodb batch-write-item \
  --request-items '{
    "PlasticWorld": [
      { "PutRequest": { "Item": {
        "artistId":{"S":"A-001"},"creationId":{"S":"C-1002"},
        "category":{"S":"Animal"},"color":{"S":"Rojo"},
        "likes":{"N":"10"},"createdAt":{"S":"2025-11-03T10:10:00Z"}
      }}},
      { "PutRequest": { "Item": {
        "artistId":{"S":"A-001"},"creationId":{"S":"C-1003"},
        "category":{"S":"Comida"},"color":{"S":"Azul"},
        "likes":{"N":"28"},"createdAt":{"S":"2025-11-03T10:20:00Z"}
      }}}
      // ... añade más PutRequest hasta completar 15
    ]
  }'
```

## Paso 3:

GetItem
```bash
aws dynamodb get-item \
  --table-name PlasticWorld \
  --key '{"artistId":{"S":"A-001"},"creationId":{"S":"C-1001"}}'
```

Scan (recuerda no usarlo en producción)
```bash
aws dynamodb scan \
  --table-name PlasticWorld \
  --limit 5
```

## Paso 4:
Solo sería añadir estas modificaciones al serverless.yml:

```yml
Properties:
        TableName: PlasticWorld
        BillingMode: PAY_PER_REQUEST
        AttributeDefinitions:
          - AttributeName: artistId
            AttributeType: S
          - AttributeName: creationId
            AttributeType: S
          - AttributeName: likes
            AttributeType: N
          - AttributeName: category # Nuevo
            AttributeType: S
          - AttributeName: color # Nuevo
            AttributeType: S
        KeySchema:
          - AttributeName: artistId
            KeyType: HASH
          - AttributeName: creationId
            KeyType: RANGE
        GlobalSecondaryIndexes: # Nuevo
          - IndexName: CategoryIndex
            KeySchema:
              - AttributeName: category
                KeyType: HASH
            Projection:
              ProjectionType: ALL
          - IndexName: ColorIndex
            KeySchema:
              - AttributeName: color
                KeyType: HASH
            Projection:
              ProjectionType: ALL
```

## Paso 5:
Query por LSI:

```bash
aws dynamodb query \
  --table-name PlasticWorld \
  --index-name LikesIndex \
  --key-condition-expression "artistId = :a AND likes >= :min" \
  --expression-attribute-values '{
    ":a":{"S":"A-001"},
    ":min":{"N":"20"}
  }'
```

Query por GSI (categoria)
```bash
aws dynamodb query \
  --table-name PlasticWorld \
  --index-name CategoryIndex \
  --key-condition-expression "category = :c" \
  --expression-attribute-values '{":c":{"S":"Animal"}}'
```

Query por GSI (color)
```bash
aws dynamodb query \
  --table-name PlasticWorld \
  --index-name ColorIndex \
  --key-condition-expression "color = :col" \
  --expression-attribute-values '{":col":{"S":"Azul"}}'
```

Y listo el 🐤, espero que hayas aprendido bastante en este lab, ¡Nos vemos en la próxima sección!