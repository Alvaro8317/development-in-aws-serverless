package com.alvaro8317.expense.model;

import java.math.BigDecimal;
import java.util.UUID;

public class Spend {
    private String id;
    private String name;
    private String description;
    private BigDecimal amount;

    public Spend(String name, String description, BigDecimal amount) {
        this.id = UUID.randomUUID().toString();
        this.name = name;
        this.description = description;
        this.amount = amount;
    }

    public String getId() { return id; }
    public String getName() { return name; }
    public String getDescription() { return description; }
    public BigDecimal getAmount() { return amount; }
}
