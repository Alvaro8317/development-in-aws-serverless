# 🧮 Ejercicios de práctica — Cálculo de WCUs (Write Capacity Units)

A continuación, calcula cuántas WCUs requiere cada caso.  
Recuerda considerar:
- Redondeo hacia arriba por cada 1 KB.
- Escrituras transaccionales consumen el doble.
- Cada escritura estándar de hasta 1 KB = 1 WCU.

---

### 1️⃣
Cada ítem pesa **0.5 KB**, escritura **estándar**, **25 escrituras por segundo**.  
¿Cuántas WCUs se requieren?

---

### 2️⃣
Ítems de **2.2 KB**, escritura **transaccional**, **10 escrituras por segundo**.  
¿Cuántas WCUs necesitas?

---

### 3️⃣
Tus registros pesan **3 KB**, escritura **estándar**, **80 escrituras por segundo**.  
¿Cuántas WCUs debes provisionar?

---

### 4️⃣
Tienes objetos de **1 KB**, escritura **transaccional**, **15 operaciones por segundo**.  
¿Cuántas WCUs son necesarias?

---

### 5️⃣
Cada registro pesa **4.5 KB**, escritura **estándar**, **50 escrituras por segundo**.  
¿Cuántas WCUs se requieren?

---

### 6️⃣
Ítems de **0.9 KB**, escritura **transaccional**, **40 escrituras por segundo**.  
¿Cuántas WCUs necesitas?

---

### 7️⃣
Registros de **6 KB**, escritura **estándar**, **12 operaciones por segundo**.  
¿Cuántas WCUs corresponden?

---

### 8️⃣
Cada ítem pesa **2 KB**, escritura **transaccional**, **5 escrituras por segundo**.  
¿Cuántas WCUs se requieren?

---

### 9️⃣
Objetos de **0.3 KB**, escritura **estándar**, **60 escrituras por segundo**.  
¿Cuántas WCUs debes tener disponibles?

---

### 🔟
Ítems de **1.2 KB**, escritura **transaccional**, **100 escrituras por segundo**.  
¿Cuántas WCUs necesitas?

---

> 💡 **Tip:** Recuerda aplicar `ceil(tamaño / 1 KB)` para redondear hacia arriba antes de multiplicar por el número de escrituras por segundo y por 2 si es transaccional.
