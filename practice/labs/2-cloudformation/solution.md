# 🎁 **Solución:**

Oye oye... No veas la solución, ¿Ya lo intentaste tú antes? Recuerda que la práctica hace al maestro

![worried](https://content.imageresizer.com/images/memes/Kermit-worried-face-meme-7.jpg)

¿De verdad la vas a ver?

---

¿Segurito/a segurito/a?

---

Úsalo bajo tu propia responsabilidad:

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Laboratorio IAM Adventure"

Resources:
  GrootUser:
    Type: AWS::IAM::User
    Properties:
      UserName: groot
      Tags:
        - Key: Guardian
          Value: "Galaxia"

  VengadoresGroup:
    Type: AWS::IAM::Group

  GrupoMembership:
    Type: AWS::IAM::UserToGroupAddition
    Properties:
      GroupName: !Ref VengadoresGroup
      Users:
        - !Ref GrootUser

  PoliticaPersonalizada:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: S3ListBucketsPolicy
      Groups:
        - !Ref VengadoresGroup
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Action: s3:ListAllMyBuckets
            Resource: "*"

```

---

## 📌 **¿Qué evaluar en este laboratorio?**

- El alumno entiende cómo crear usuarios, grupos, políticas y roles desde una única plantilla IaC.
- Maneja correctamente AWS CLI para verificar los recursos creados.
- Comprende la seguridad y los permisos en AWS IAM.

---

## 🥳 **Conclusión divertida para el laboratorio:**

> _"¡Ahora ya controlas la galaxia IAM con CloudFormation! Eres como el Nick Fury del IaC."_ 😎

**Meme final:** Busca "Nick Fury - I'm here to talk about the Avengers Initiative".

---

**¡Éxito total con tu laboratorio!** 🥳🚀
