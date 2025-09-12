package com.alvaro8317.expense.handler;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.alvaro8317.expense.model.Spend;
import com.alvaro8317.expense.repository.DynamoDbRepoSpend;
import com.alvaro8317.expense.service.SpendService;
import com.fasterxml.jackson.databind.ObjectMapper;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

import java.math.BigDecimal;
import java.util.Map;

public class SpendHandler implements RequestHandler<Map<String, Object>, Map<String, Object>> {
    private final ObjectMapper mapper = new ObjectMapper();
    private final SpendService service;
    private final String tableName;

    public SpendHandler() {
        String tn = System.getenv("TABLE_NAME");
        DynamoDbClient client = DynamoDbClient.create();
        this.tableName = tn;
        this.service = new SpendService(new DynamoDbRepoSpend(client, tn));
    }

    public SpendHandler(SpendService service, String tableName) {
        this.service = service;
        this.tableName = tableName;
    }

    @Override
    @SuppressWarnings("unchecked")
    public Map<String, Object> handleRequest(Map<String, Object> event, Context context) {
        try {
            String body = (String) event.get("body");
            Map<String, String> payload = mapper.readValue(
                body, new com.fasterxml.jackson.core.type.TypeReference<Map<String, String>>() {}
            );

            Spend created = service.createSpend(
                payload.get("name"),
                payload.get("description"),
                new BigDecimal(payload.get("amount"))
            );

            return Map.of(
                "statusCode", 200,
                "headers", Map.of("Content-Type", "application/json"),
                "body", mapper.writeValueAsString(Map.of(
                    "message", "Spend created successfully",
                    "spend_created", created
                ))
            );
        } catch (Exception e) {
            return Map.of(
                "statusCode", 500,
                "headers", Map.of("Content-Type", "application/json"),
                "body", "{\"error\": \"Internal server error\"}"
            );
        }
    }
}
