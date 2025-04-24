# CRUD Básico con FastAPI

Esta es una aplicación CRUD básica desarrollada con FastAPI siguiendo el patrón MVC.

## Instalación

1. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar la aplicación:

   ```bash
   uvicorn main:app --reload
   ```

## Ejemplo de uso

Para crear un nuevo item:

```bash
curl -X POST "http://localhost:8000/items/" -H "Content-Type: application/json" -d '{"name": "Item 1", "description": "Descripción del item 1"}'
```

Para obtener todos los items:

```bash
curl "http://localhost:8000/items/"
```
