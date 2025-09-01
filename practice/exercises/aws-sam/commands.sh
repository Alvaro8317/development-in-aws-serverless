export PWD_DB="MyUltraMegaSecretPassword"

aws ssm put-parameter \
    --name "/sam/app/hello/world/java/db-password" \
    --value "$PWD_DB" \
    --type String \
    --overwrite
