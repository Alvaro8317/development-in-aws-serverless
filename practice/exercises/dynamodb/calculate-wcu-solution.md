# ✅ Soluciones — Cálculo de WCUs (Write Capacity Units)

---

### 1️⃣
Cada ítem pesa **0.5 KB**, escritura **estándar**, **25 escrituras por segundo**.

**Cálculo:**
ceil(0.5 / 1) × 25 = 1 × 25 = **25 WCUs**

**Explicación:**  
Cada ítem ocupa menos de 1 KB, pero se cobra como 1 unidad completa por operación.

---

### 2️⃣
Ítems de **2.2 KB**, escritura **transaccional**, **10 escrituras por segundo**.

**Cálculo:**
ceil(2.2 / 1) × 10 × 2 = 3 × 10 × 2 = **60 WCUs**

**Explicación:**  
Cada ítem requiere 3 unidades (por redondeo), y las transacciones duplican el consumo.

---

### 3️⃣
Tus registros pesan **3 KB**, escritura **estándar**, **80 escrituras por segundo**.

**Cálculo:**
ceil(3 / 1) × 80 = 3 × 80 = **240 WCUs**

**Explicación:**  
Cada ítem usa 3 bloques de 1 KB y hay 80 operaciones por segundo.

---

### 4️⃣
Tienes objetos de **1 KB**, escritura **transaccional**, **15 operaciones por segundo**.

**Cálculo:**
ceil(1 / 1) × 15 × 2 = 1 × 15 × 2 = **30 WCUs**

**Explicación:**  
Cada escritura consume 1 unidad, pero las transacciones duplican el uso.

---

### 5️⃣
Cada registro pesa **4.5 KB**, escritura **estándar**, **50 escrituras por segundo**.

**Cálculo:**
ceil(4.5 / 1) × 50 = 5 × 50 = **250 WCUs**

**Explicación:**  
DynamoDB cobra por bloques de 1 KB, así que 4.5 KB se redondea a 5 unidades.

---

### 6️⃣
Ítems de **0.9 KB**, escritura **transaccional**, **40 escrituras por segundo**.

**Cálculo:**
ceil(0.9 / 1) × 40 × 2 = 1 × 40 × 2 = **80 WCUs**

**Explicación:**  
Aunque el ítem pesa menos de 1 KB, cada transacción cuenta como 2 WCUs.

---

### 7️⃣
Registros de **6 KB**, escritura **estándar**, **12 operaciones por segundo**.

**Cálculo:**
ceil(6 / 1) × 12 = 6 × 12 = **72 WCUs**

**Explicación:**  
Cada registro ocupa 6 bloques de 1 KB, multiplicado por 12 operaciones.

---

### 8️⃣
Cada ítem pesa **2 KB**, escritura **transaccional**, **5 escrituras por segundo**.

**Cálculo:**
ceil(2 / 1) × 5 × 2 = 2 × 5 × 2 = **20 WCUs**

**Explicación:**  
Cada ítem ocupa 2 KB y cada escritura transaccional cuesta el doble.

---

### 9️⃣
Objetos de **0.3 KB**, escritura **estándar**, **60 escrituras por segundo**.

**Cálculo:**
ceil(0.3 / 1) × 60 = 1 × 60 = **60 WCUs**

**Explicación:**  
Aunque pesan menos de 1 KB, DynamoDB siempre redondea al KB completo.

---

### 🔟
Ítems de **1.2 KB**, escritura **transaccional**, **100 escrituras por segundo**.

**Cálculo:**
ceil(1.2 / 1) × 100 × 2 = 2 × 100 × 2 = **400 WCUs**

**Explicación:**  
El ítem se redondea a 2 KB y se multiplica por 2 por ser transaccional.

---

> 💡 **Regla general:**
> - Cada 1 KB (o fracción) escrita = 1 WCU  
> - Multiplica por las escrituras por segundo  
> - Multiplica por 2 si es transaccional  
> - DynamoDB siempre cobra el KB completo, no fracciones.
