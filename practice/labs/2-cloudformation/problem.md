# 🧪 **Laboratorio IAM Adventure: "IAM, tu propio guardián de la nube"**

## 🎯 **Objetivo del laboratorio**

Crear y gestionar recursos de AWS IAM usando exclusivamente plantillas de CloudFormation.

---

## 📚 **Contenido del laboratorio:**

### 📌 **Parte 1 - "IAM Groot" (Crear un usuario)** ****🌱

- Crea una plantilla YAML sencilla para generar un usuario IAM llamado `groot`.
- Bonus: Añadir etiquetas (tags) como `Guardian: Galaxia` o `Tipo: Flora Coloso`.
- Verifica la creación del usuario desde AWS CLI (`aws iam get-user`).

![iam groot](https://alvaro8317-udemy-courses.s3.us-east-1.amazonaws.com/aws-developer-serverless/images/iam+groot.png)

---

### 📌 **Parte 2 - "Avengers Assemble" (Crear un grupo)** 🛡️

- Actualiza la plantilla anterior para crear un grupo IAM llamado `Vengadores`.
- Agrega el usuario `groot` al grupo `Vengadores`.
- Verifica los miembros del grupo con AWS CLI (`aws iam get-group`).

![avengers group](https://alvaro8317-udemy-courses.s3.us-east-1.amazonaws.com/aws-developer-serverless/images/avengers+group.png)

---

### 📌 **Parte 3 - "With great power…" (Política IAM personalizada)** 🕷️

- Crea una política IAM personalizada que permita únicamente listar buckets de S3 (`s3:ListAllMyBuckets`).
- Asocia esa política al grupo `Vengadores`.
- Desde la consola AWS o CLI, verifica que la política esté correctamente adjunta.

![great power](https://alvaro8317-udemy-courses.s3.us-east-1.amazonaws.com/aws-developer-serverless/images/great-power.png)

---

### 📌 **Parte 4 - "Snap! Eliminar recursos" (Destruir el Stack)** ✨

- Finalmente, destruye todos los recursos creados mediante CloudFormation con AWS CLI (`aws cloudformation delete-stack`).
- Verifica desde AWS CLI que los recursos ya no existan.

![thanos snap](https://alvaro8317-udemy-courses.s3.us-east-1.amazonaws.com/aws-developer-serverless/images/thanos+cloudformation.png)

---

## 📝 **Checklist:**

- [x] Crear usuario IAM con tags personalizados.
- [x] Crear grupo IAM y asociar usuario.
- [x] Crear política IAM personalizada y asociarla al grupo.
- [ ] Eliminar todo el stack y confirmar que se eliminaron los recursos.

---
