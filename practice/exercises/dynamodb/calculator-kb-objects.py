import json
import uuid

from boto3.dynamodb import types

# Objeto JSON que se introduciría en DynamoDB
item = {
    "UserId": str(uuid.uuid4()),
    "Name": "Alvaro",
    "LastName": "Garzón",
    "Age": 28,
    "alias": "Alvaro8317",
}

# Serializador
serializer = types.TypeSerializer()
size_bytes = len(json.dumps({k: serializer.serialize(v) for k, v in item.items()}))
size_kb = size_bytes / 1024

print(f"Tamaño estimado: {size_bytes} bytes ({size_kb:.2f} KB)")
