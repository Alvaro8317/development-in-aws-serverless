aws ssm put-parameter \
  --name "/expense-app-manager/auth/username" \
  --type String \
  --value "miusuario" \
  --overwrite

aws ssm put-parameter \
  --name "/expense-app-manager/auth/password" \
  --type SecureString \
  --value "micontraseñaSuperSecreta123" \
  --overwrite
