package com.alvaro8317.expense.repository;

import com.alvaro8317.expense.model.Spend;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;

import java.util.List;
import java.util.Map;

public abstract class BaseRepositorySpend {

    /**
     * Inserta un nuevo Spend en la base de datos.
     *
     * @param spend Objeto de dominio a persistir
     */
    public abstract void createSpend(Spend spend);

    /**
     * Recupera todos los spends de la tabla.
     *
     * @return Lista de items en formato DynamoDB (atributo-valor)
     */
    public abstract List<Map<String, AttributeValue>> getSpends();
}
