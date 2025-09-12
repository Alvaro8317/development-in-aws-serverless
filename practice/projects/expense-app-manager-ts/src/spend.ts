import { APIGatewayProxyHandlerV2 } from "aws-lambda";

export const handler: APIGatewayProxyHandlerV2 = async (event) => {
  const body = JSON.parse(event.body || "{}");

  const spend = {
    id: crypto.randomUUID(),
    name: body.name,
    description: body.description,
    amount: parseFloat(body.amount),
  };

  return {
    statusCode: 200,
    body: JSON.stringify({
      message: "Spend created successfully",
      spend,
    }),
  };
};