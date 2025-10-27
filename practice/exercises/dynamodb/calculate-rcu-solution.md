# ✅ Soluciones — Cálculo de RCUs (Read Capacity Units)

---

### 1️⃣
2 KB, eventual, 50 lecturas/s  
RCU = ceil(2 / 4) × 50 × 0.5 = 1 × 50 × 0.5 = **25 RCUs**

---

### 2️⃣
8 KB, fuerte, 20 lecturas/s  
RCU = ceil(8 / 4) × 20 × 1 = 2 × 20 × 1 = **40 RCUs**

---

### 3️⃣
3 KB, transaccional, 10 lecturas/s  
RCU = ceil(3 / 4) × 10 × 2 = 1 × 10 × 2 = **20 RCUs**

---

### 4️⃣
5 KB, eventual, 80 lecturas/s  
RCU = ceil(5 / 4) × 80 × 0.5 = 2 × 80 × 0.5 = **80 RCUs**

---

### 5️⃣
1 KB, fuerte, 200 lecturas/s  
RCU = ceil(1 / 4) × 200 × 1 = 1 × 200 × 1 = **200 RCUs**

---

### 6️⃣
4 KB, transaccional, 25 lecturas/s  
RCU = ceil(4 / 4) × 25 × 2 = 1 × 25 × 2 = **50 RCUs**

---

### 7️⃣
6 KB, fuerte, 15 lecturas/s  
RCU = ceil(6 / 4) × 15 × 1 = 2 × 15 × 1 = **30 RCUs**

---

### 8️⃣
2.5 KB, eventual, 100 lecturas/s  
RCU = ceil(2.5 / 4) × 100 × 0.5 = 1 × 100 × 0.5 = **50 RCUs**

---

### 9️⃣
9 KB, transaccional, 5 lecturas/s  
RCU = ceil(9 / 4) × 5 × 2 = 3 × 5 × 2 = **30 RCUs**

---

### 🔟
3 KB, fuerte, 60 lecturas/s  
RCU = ceil(3 / 4) × 60 × 1 = 1 × 60 × 1 = **60 RCUs**

---

> 💡 **Recuerda:**  
> - Cada 4 KB o fracción = 1 unidad base.  
> - Eventual → 0.5×  
> - Fuerte → 1×  
> - Transaccional → 2×  
> DynamoDB **cobra siempre redondeando hacia arriba**.
