# 🧮 Ejercicios de práctica — Cálculo de RCUs (Read Capacity Units)

A continuación, calcula cuántas RCUs requiere cada caso.  
Recuerda:
- Las lecturas se redondean a bloques de 4 KB.  
- Las lecturas eventualmente consistentes cuestan la mitad (×0.5).  
- Las transaccionales cuestan el doble (×2).

---

### 1️⃣
Ítems de **2 KB**, lectura **eventualmente consistente**, **50 lecturas por segundo**.  
¿Cuántas RCUs se requieren?

---

### 2️⃣
Cada ítem pesa **8 KB**, lectura **fuertemente consistente**, **20 lecturas por segundo**.  
¿Cuántas RCUs necesitas?

---

### 3️⃣
Ítems de **3 KB**, lectura **transaccional**, **10 lecturas por segundo**.  
¿Cuántas RCUs corresponden?

---

### 4️⃣
Registros de **5 KB**, lectura **eventualmente consistente**, **80 lecturas por segundo**.  
¿Cuántas RCUs se requieren?

---

### 5️⃣
Ítems de **1 KB**, lectura **fuertemente consistente**, **200 lecturas por segundo**.  
¿Cuántas RCUs debes provisionar?

---

### 6️⃣
Objetos de **4 KB**, lectura **transaccional**, **25 lecturas por segundo**.  
¿Cuántas RCUs se necesitan?

---

### 7️⃣
Registros de **6 KB**, lectura **fuertemente consistente**, **15 lecturas por segundo**.  
¿Cuántas RCUs se requieren?

---

### 8️⃣
Ítems de **2.5 KB**, lectura **eventualmente consistente**, **100 lecturas por segundo**.  
¿Cuántas RCUs necesitas?

---

### 9️⃣
Objetos de **9 KB**, lectura **transaccional**, **5 lecturas por segundo**.  
¿Cuántas RCUs corresponden?

---

### 🔟
Registros de **3 KB**, lectura **fuertemente consistente**, **60 lecturas por segundo**.  
¿Cuántas RCUs se requieren?

---

> 💡 **Tip:**  
> Fórmula general:  
> RCU = ceil(tamaño en KB ÷ 4) × lecturas por segundo × factor de tipo  
> (0.5 = eventual, 1 = fuerte, 2 = transaccional)
