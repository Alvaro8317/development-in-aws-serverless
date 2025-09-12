package com.alvaro8317.expense.service;

import com.alvaro8317.expense.model.Spend;
import com.alvaro8317.expense.repository.BaseRepositorySpend;

import java.math.BigDecimal;

public class SpendService {
    private final BaseRepositorySpend repo;

    public SpendService(BaseRepositorySpend repo) {
        this.repo = repo;
    }

    public Spend createSpend(String name, String description, BigDecimal amount) {
        Spend spend = new Spend(name, description, amount);
        repo.createSpend(spend);
        return spend;
    }

    public Spend getSpends(String name, String description, BigDecimal amount) {
        Spend spend = new Spend(name, description, amount);
        repo.getSpends();
        return spend;
    }
}
