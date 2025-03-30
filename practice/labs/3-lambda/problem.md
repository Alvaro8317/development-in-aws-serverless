# Laboratorio Lambda

## 🎯 **Objetivo del Laboratorio**

- Crear una **Lambda URL con autenticación AWS_IAM** que simula un contador.
- El contador **se incrementa** con cada invocación y **se reinicia a 0** si la Lambda pasa por un **cold start**.
- Observar cómo las invocaciones frías y calientes afectan el comportamiento del contador.

---

## 📚 **Paso 1: Crear el Código de la Lambda**

- Crea un archivo controlador (handler) en tu lenguaje de programación que desees que contenga el código para:
  - Definir un **contador** fuera del `lambda_handler`(o la función que definas que va a gestionar cada invocación lambda) para mantener su valor en _invocaciones calientes_.
  - El contador aumentará en 1 por cada invocación mientras que la lambda esté caliente.
  - Retornar el valor del contador con el mensaje "Está haciendo frío, ¿no?" si la lambda está en estado "cold start".

---

## 📚 **Paso 2: Crear el Archivo ZIP para la Lambda**

- Comprime el código en un archivo llamado `lambda_cold_start.zip`.
- Este archivo será subido al bucket de S3 para ser usado por la Lambda.

---

## 📚 **Paso 3: Subir el Archivo ZIP a S3**

- Sube `lambda_cold_start.zip` al bucket de S3 que usarás para desplegar la Lambda con AWS CLI, usando el comando **aws s3 cp** que ya se ha visto en clases pasadas.

---

## 📚 **Paso 4: Crear la Plantilla de CloudFormation**

- Crea un archivo llamado `cold-start-lambda-lab.yaml` para:
  - Definir la **Lambda**.
  - Crear una **Lambda URL** autenticada para invocar la función.
  - Asignar permisos para que la URL pueda invocar la Lambda.
  - Crea el rol que asumirá la función lambda.

---

## 📚 **Paso 5: Desplegar CloudFormation**

- Usa `aws cloudformation create-stack` o `aws cloudformation deploy` para crear la Lambda y su URL (Te recomiendo que investigues acerca de la diferencia entre create-stack y deploy 😁).
- Asegúrate de usar `CAPABILITY_NAMED_IAM` para permitir la creación de roles nombrados.

---

## 📚 **Paso 6: Obtener la URL de la Lambda**

- Una vez desplegada la plantilla, obtén la URL de la Lambda usando `aws lambda get-function-url-config`.

---

## 📚 **Paso 7: Invocar la Lambda URL**

- Usa `awscurl` para invocar la URL:
  - La **primera invocación** mostrará un mensaje indicando que hubo un **cold start**.
  - Las siguientes invocaciones **incrementarán el contador**.
  - Si la Lambda se queda inactiva por un tiempo y entra en **cold start** nuevamente, el contador se reiniciará.

---

## 📚 **Paso 8: Simular Cold Start y Error 502**

- Opcionalmente, reduce el timeout de la Lambda para forzar un error 502 si tarda demasiado en responder.

---

## 📚 **Paso 9: Limpiar los Recursos**

- Una vez finalizado el laboratorio, elimina el stack de CloudFormation para evitar costos.

---

## 🔥 **Reto Extra para los Estudiantes**

- Modificar el código para agregar una fecha de la última invocación al resultado en caso que la lambda esté caliente.
