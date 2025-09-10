docker network ls
docker network create sam-net


docker run --network sam-net -p 8000:8000 amazon/dynamodb-local 

aws dynamodb create-table \
  --table-name SpendsTableLocal \
  --attribute-definitions AttributeName=id,AttributeType=S \
  --key-schema AttributeName=id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region us-east-1 \
  --endpoint-url http://localhost:8000

aws dynamodb list-tables --endpoint-url http://localhost:8000 --region us-east-1

sam build --no-cached

sam local start-api --host 0.0.0.0 --port 3000 \
  --env-vars env.json \
  --docker-network sam-net
