import { APIGatewayProxyEvent, APIGatewayProxyResult, Context } from "aws-lambda"
import { Spend } from "../models/spend"
import { DynamoDbRepoSpend } from "../repositories/dynamoDbRepoSpend"
import { SpendService } from "../services/spendService"

export async function spendHandler(
    event: APIGatewayProxyEvent,
    context: Context
): Promise<APIGatewayProxyResult> {
    try {
        const body = event.body ? JSON.parse(event.body) : {}
        const repo = new DynamoDbRepoSpend()
        const service = new SpendService(repo)

        const spendCreated: Spend = await service.createSpend(
            body.name,
            body.description,
            Number(body.amount)
        )

        return {
            statusCode: 200,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                message: "Spend created successfully",
                spend_created: spendCreated.asDict(),
            }),
        }
    } catch (error) {
        console.error("Error creating spend:", error)
        return {
            statusCode: 500,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: "Internal server error" }),
        }
    }
}

export async function getSpendHandler(
    event: APIGatewayProxyEvent,
    context: Context
): Promise<APIGatewayProxyResult> {
    try {
        const repo = new DynamoDbRepoSpend()
        const service = new SpendService(repo)

        const spends = await service.getSpends()

        return {
            statusCode: 200,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ spends }),
        }
    } catch (error) {
        console.error("Error fetching spends:", error)
        return {
            statusCode: 500,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: "Internal server error" }),
        }
    }
}
