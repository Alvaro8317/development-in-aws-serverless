
# ThrottlingException o ProvisionedThroughputExceededException

**¿Qué hago?**
- Llorar
- Fingir que no pasó
- Echarle la bendición a mi código
- Implementar **backoff exponencial**

---

### ¿Qué es el backoff exponencial?

Es una estrategia para **reintentar solicitudes fallidas** sin saturar más al servicio.
Cada vez que DynamoDB te lanza `ThrottlingException`, esperas **el doble de tiempo que antes** antes de volver a intentar.

---

### Ejemplo visual

```text
Intento 1 → Falla → Esperar 10 segundos
Intento 2 → Falla → Esperar 20 segundos
Intento 3 → Falla → Esperar 40 segundos
Intento 4 → Éxito 🎉 (o seguir esperando si no)
```

En cada intento aumentas el tiempo de espera, para darle “respiro” al servicio.
Si además agregas **jitter** (una pequeña variación aleatoria), evitas que todos tus clientes esperen lo mismo y vuelvan a golpear al mismo tiempo.

[Jitter con backoff](https://dev.to/biomousavi/understanding-jitter-backoff-a-beginners-guide-2gc)