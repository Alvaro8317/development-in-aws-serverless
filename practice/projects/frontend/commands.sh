# Comandos para copiar el frontend al bucket

aws s3 cp index.html s3://expense-app-manager-frontend-sam/
aws s3 cp dist s3://expense-app-manager-frontend-sam/ --recursive

# Cuando estés en src/

npm install # Instala todas las dependencias