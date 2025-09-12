import { DynamoDBClient } from "@aws-sdk/client-dynamodb"
import { DynamoDBDocumentClient, PutCommand, ScanCommand } from "@aws-sdk/lib-dynamodb"
import { Spend } from "../models/spend"
import { BaseRepositorySpend } from "./spendRepository"

function getDynamoDocClient(): DynamoDBDocumentClient {
    const tableRegion = process.env.AWS_REGION ?? "us-east-1"
    const isLocal = (process.env.IS_LOCAL_ENVIRONMENT ?? "false").toLowerCase() === "true"

    const dynamoClient = new DynamoDBClient({
        region: tableRegion,
        endpoint: isLocal ? process.env.DDB_ENDPOINT ?? "http://host.docker.internal:8000" : undefined,
        credentials: isLocal
            ? {
                accessKeyId: process.env.AWS_ACCESS_KEY_ID ?? "dummy",
                secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY ?? "dummy",
            }
            : undefined,
    })

    return DynamoDBDocumentClient.from(dynamoClient)
}

export class DynamoDbRepoSpend implements BaseRepositorySpend {
    private tableName: string
    private docClient: DynamoDBDocumentClient

    constructor() {
        this.tableName = process.env.TABLE_NAME ?? ""
        if (!this.tableName) throw new Error("TABLE_NAME environment variable is required")
        this.docClient = getDynamoDocClient()
    }

    async createSpend(item: Record<string, string | number>): Promise<any> {
        const command = new PutCommand({
            TableName: this.tableName,
            Item: item,
        })
        return this.docClient.send(command)
    }

    async getSpends(): Promise<Spend[]> {
        const command = new ScanCommand({
            TableName: this.tableName,
        })
        const result = await this.docClient.send(command)
        return (result.Items as Spend[]) ?? []
    }
}
