package com.alvaro8317.expense;

import com.alvaro8317.expense.handler.SpendHandler;
import com.alvaro8317.expense.model.Spend;
import com.alvaro8317.expense.repository.BaseRepositorySpend;
import com.alvaro8317.expense.service.SpendService;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;

import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class SpendHandlerTest {

    static class FakeRepo extends BaseRepositorySpend {
        @Override
        public void createSpend(Spend spend) {
        }

        @Override
        public List<Map<String, AttributeValue>> getSpends() {
            return List.of();
        }
    }

    @Test
    void testHandleRequest() {
        SpendService service = new SpendService(new FakeRepo());

        SpendHandler handler = new SpendHandler(service, "dummy-table");

        Map<String, Object> event = Map.of(
            "body", "{\"name\":\"Test\",\"description\":\"desc\",\"amount\":\"12.34\"}"
        );

        Map<String, Object> resp = handler.handleRequest(event, null);
        assertEquals(200, resp.get("statusCode"));
    }
}
