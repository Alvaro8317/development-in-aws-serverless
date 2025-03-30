# 🛠️ **Laboratorio 1 - Gestión de IAM con AWS CLI (SOLUCIÓN)**

**¡Hey! Espera** ⏳, antes de seguir… ¿Ya lo intentaste por tu cuenta?

![thinking kid](https://alvaro8317-udemy-courses.s3.us-east-1.amazonaws.com/aws-developer-serverless/images/156fb3a41134efe9020a49b68bfeccbf.gif)
💡 Recuerda que **la práctica hace al maestro** y que lo mejor es intentarlo primero. Si te estancaste, puedes leer los pasos hasta donde necesites, pero te recomiendo que vuelvas a intentarlo **antes de bajar más**.

¿Seguro/a que quieres ver la solución? 🤨

**¿Última palabra?**

🚨 **¡NO HAY VUELTA ATRÁS!** 🚨

⬇️ ⬇️ ⬇️ ⬇️ ⬇️

⬇️ ⬇️ ⬇️ ⬇️ ⬇️

⬇️ ⬇️ ⬇️ ⬇️ ⬇️

⬇️ ⬇️ ⬇️ ⬇️ ⬇️

🛑 **Última oportunidad para arrepentirte...** 🛑

![confused travolta](https://media2.giphy.com/media/6uGhT1O4sxpi8/giphy.gif?cid=6c09b952fn1drd40s6ivxd1cnw6eiwcqhv84vx04vtr57nny&ep=v1_gifs_search&rid=giphy.gif&ct=g)

## 📌 **Pasos a seguir**

### **1️⃣ Crear los usuarios en IAM**

Ejecuta los siguientes comandos en la terminal para crear los usuarios:

```sh
aws iam create-user --user-name DevUser1
aws iam create-user --user-name DevUser2
aws iam create-user --user-name DevUser3
```

📌 **Tip:** Puedes verificar que los usuarios fueron creados con:

```sh
aws iam list-users
```

---

### **2️⃣ Asignar permisos de solo lectura en IAM**

AWS tiene una política predefinida llamada **IAMReadOnlyAccess**, que da permisos de solo lectura sobre IAM. Debes adjuntar esta política a los usuarios:

```sh
aws iam attach-user-policy --user-name DevUser1 --policy-arn arn:aws:iam::aws:policy/IAMReadOnlyAccess
aws iam attach-user-policy --user-name DevUser2 --policy-arn arn:aws:iam::aws:policy/IAMReadOnlyAccess
aws iam attach-user-policy --user-name DevUser3 --policy-arn arn:aws:iam::aws:policy/IAMReadOnlyAccess
```

![iam the one who reads meme](https://alvaro8317-udemy-courses.s3.us-east-1.amazonaws.com/aws-developer-serverless/images/iam.jpg)

Verifica que la política fue aplicada:

```sh
aws iam list-attached-user-policies --user-name DevUser1
aws iam list-attached-user-policies --user-name DevUser2
aws iam list-attached-user-policies --user-name DevUser3
```

---

### **3️⃣ Validar que los permisos funcionan**

Para confirmar que los usuarios solo pueden **leer** y no modificar nada en IAM, podrías hacer una prueba con uno de ellos.

🚀 **Simula que inicias sesión con el usuario `DevUser1` (usando credenciales temporales o un perfil) y ejecuta:**

```sh
aws iam list-users
```

✅ Debería permitirte ver los usuarios en la cuenta.

🚨 Ahora intenta crear un nuevo usuario:

```sh
aws iam create-user --user-name UsuarioPrueba
```

❌ **Debe fallar** con un error de permisos, ya que solo tiene acceso de lectura.

---

## 🔥 **Preguntas de reflexión**

1. ¿Cómo podrías eliminar uno de los usuarios creados?
2. ¿Qué pasaría si en vez de `IAMReadOnlyAccess` asignaras `AdministratorAccess`?
3. ¿Cómo listarías todas las políticas de IAM disponibles en la cuenta?

---

## 🎭 **Meme sugerido**

📌 _"I AM the one who reads" (Walter White con permisos de solo lectura en IAM 😂)"_

---

Esto ayudará a los alumnos a **entender IAM desde la terminal** con un caso realista. ¿Te gustaría que agregue más retos o alguna variación? 🚀
