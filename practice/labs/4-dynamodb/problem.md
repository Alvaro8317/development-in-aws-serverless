# 🎨 Laboratorio - PlasticWorld: Índices, consultas y creatividad con DynamoDB

¡Bienvenido/a a **PlasticWorld**! 🌈  
Un universo donde los artistas crean **figuras de plastilina** y suben sus obras al marketplace más tierno del mundo.

Tu misión: **crear y consultar una tabla DynamoDB** que gestione estas obras maestras de plastilina.

---

## 🧠 Contexto

Cada creador tiene un perfil y varias figuras publicadas.  
Tu tabla debe guardar los siguientes datos:

| Atributo | Tipo | Descripción |
|-----------|------|-------------|
| `artistId` | String | Identificador del artista |
| `creationId` | String | ID único de la figura |
| `color` | String | Color predominante |
| `category` | String | Tipo de figura (`Animal`, `Comida`, `Superhéroe`, etc.) |
| `likes` | Number | Likes recibidos |
| `createdAt` | String | Fecha ISO de creación |

### Llave principal:
- **Partition key:** `artistId`
- **Sort key:** `creationId`

---

## 🎯 Pasos del laboratorio

1. Crear una tabla DynamoDB con serverless framework con una **llave compuesta** y *un LSI* llamado *LikesIndex*, el cuál su llave de ordenación va a ser el atributo *likes* tomando de base la llave principal mencionada en el contexto. **IMPORTANTE: Recuerda que los LSIs solo se pueden crear al crear la tabla, no vayas a crear la tabla sin el LSI.**
2. Insertar 5 items individuales y 15 en lote (put-item y batch-write-item), puedes tomar de base el siguiente JSON:
```json
{
    "artistId": {"S": "A-001"},
    "creationId": {"S": "C-1001"},
    "category": {"S": "Animal"},
    "color": {"S": "Azul"},
    "likes": {"N": "45"},
    "createdAt": {"S": "2025-11-03T10:00:00Z"}
}
```
3. Crea unos comandos con AWS CLI usando estas APIs: `GetItem`, `Query`, `Scan`.
4. Crear un nuevo **GSI** en base a la categoria de las obras y otro **GSI** en base al color.
5. Crea unos comandos usando `Query` apuntando a los índices para traer información de las obras en base a:
- Cantidad de likes (LSI)
- Categoria: Animal (GSI)
- Color: Azul (GSI)
6. *(Opcional)* construir un pequeño backend que exponga las consultas a estos índices.
7. *(Opcional para los pros)* construir un pequeño frontend que consulte el backend.
8. *(Opcional)* Etiquetarme en LinkedIn con este laboratorio finalizado siempre y cuando hayas creado el back y el front + la tabla en DynamoDB