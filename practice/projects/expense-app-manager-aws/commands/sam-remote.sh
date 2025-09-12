sam remote test-event put \
  --stack-name expense-app-manager-aws \
  SpendFunction \
  --name EventSharedApiGateway \
  --file events/create-spend.json

sam remote test-event list \
  --stack-name expense-app-manager-aws \
  SpendFunction

sam remote invoke \
  SpendFunction \
  --test-event-name EventSharedApiGateway

sam remote invoke \
  SpendFunction \
  --event-file events/create-spend.json

sam remote invoke \
  SpendFunction \
  --event '{"body": "{\n   \"name\":\"Un gasto cualquiera\",\n   \"description\":\"Una descripción cualquiera\",\n   \"amount\":\"50020.89\"\n}"}'
