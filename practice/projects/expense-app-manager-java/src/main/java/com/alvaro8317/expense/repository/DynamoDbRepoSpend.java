package com.alvaro8317.expense.repository;

import com.alvaro8317.expense.model.Spend;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.PutItemRequest;
import software.amazon.awssdk.services.dynamodb.model.ScanRequest;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DynamoDbRepoSpend extends BaseRepositorySpend {
    private final DynamoDbClient client;
    private final String tableName;

    public DynamoDbRepoSpend(DynamoDbClient client, String tableName) {
        this.client = client;
        this.tableName = tableName;
    }

    @Override
    public void createSpend(Spend spend) {
        Map<String, AttributeValue> item = new HashMap<>();
        item.put("id", AttributeValue.builder().s(spend.getId()).build());
        item.put("name", AttributeValue.builder().s(spend.getName()).build());
        item.put("description", AttributeValue.builder().s(spend.getDescription()).build());
        item.put("amount", AttributeValue.builder().n(spend.getAmount().toPlainString()).build());

        client.putItem(PutItemRequest.builder()
                .tableName(tableName)
                .item(item)
                .build());
    }

    @Override
    public List<Map<String, AttributeValue>> getSpends() {
        return client.scan(ScanRequest.builder().tableName(tableName).build()).items();
    }
}
