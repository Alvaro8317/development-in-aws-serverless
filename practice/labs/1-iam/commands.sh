#!/bin/bash

# Creación de usuarios

aws iam create-user --user-name pepito
aws iam create-user --user-name pepito2
aws iam create-user --user-name pepito3

# Asociación de permisos

aws iam attach-user-policy --user-name pepito --policy-arn arn:aws:iam::aws:policy/AdministratorAccess