# Laboratorio: Crea tu refugio de mascotas serverless

## Escenario

Tu equipo ha recibido una solicitud para construir una **API RESTful de gestión de mascotas**. La empresa _AdoptaConAmor.com_ quiere lanzar una app donde la gente pueda registrar mascotas perdidas y rescatadas.

Ya tienes una API Gateway configurada con varias integraciones MOCK (simuladas) y una sola integración real usando Lambda en el método GET.

Sin embargo, ahora es momento de dejar la simulación atrás y **conectar el método POST con una función Lambda que sí guarde mascotas** en memoria. Como buen _serverless developer_, lo vas a hacer **sin necesidad de usar una base de datos**, sino simplemente usando una estructura en memoria (diccionario u objeto literal).

## Objetivo del desafío

Habilita la integración real del método `POST /pet` con una función Lambda que reciba los datos de una mascota (por ejemplo: `nombre`, `especie`, `edad`) y los guarde en un diccionario temporal

La función también debe devolver un mensaje de éxito **junto con los datos de la mascota almacenada**, para poder visualizarlo en Postman o curl.

## Requisitos técnicos

- Usar una variable global en la función para almacenar las mascotas en memoria. (_Sí, se reinicia con cada cold start, pero está bien para este laboratorio._)
- Modificar el OpenAPI para que el método POST use la nueva función Lambda, y no MOCK.
- Probar la API usando el botón **Test** en API Gateway y después confirmar que se ve bien en Postman.
- La petición `POST /pet` debe enviar un JSON como este:

```json
{
  "name": "Pelusa",
  "type": "Cat",
  "age": 2
}
```

Y el Lambda debe devolver una respuesta así:

```json
{
  "message": "Mascota registrada con éxito",
  "data": {
    "nombre": "Pelusa",
    "especie": "Gato",
    "edad": 2
  }
}
```

## Tips (pero sin spoilear mucho)

- Puedes usar `json.loads(event["body"])` para obtener el cuerpo del request si llega por API Gateway si estás en python.
- Recuerda que `event` tiene una forma distinta si es invocado desde test-invoke en lambda vs directamente desde la API, te recomiendo que lo pruebes desde lambda o busca en test-invoke, una plantilla de API Gateway.

## ✅ Entrega final del laboratorio – ¿Qué se espera?

El recurso `/pet` debe exponer dos métodos completamente integrados con **una única función Lambda compartida**:

- El método **`GET`** debe retornar un listado con todas las mascotas registradas.
- El método **`POST`** debe permitir crear una nueva mascota, generando automáticamente:

  - Un identificador único (`id`) para cada mascota.
  - Un campo `created_at` con la fecha y hora de creación (en formato ISO 8601).

Ambos métodos deben devolver respuestas en formato JSON bien estructurado.
El almacenamiento de las mascotas debe mantenerse en memoria usando una variable global, para así observar cómo se comporta frente a cold y warm starts.
