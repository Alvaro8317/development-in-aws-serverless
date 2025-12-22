sls deploy --param="nameBucket=alvaro8317"

# Actualización de una única función
sls deploy function -f hello

# Invocar una lambda
sls invoke --function hello

# Hacerlo explicito, pero es opcional
sls plugin install -n serverless-python-requirements

# Desinstalar el plugin
sls plugin uninstall -n serverless-python-requirements

# Despliega resumen del service de sls
sls info

# Despliega más información del service de sls en json
sls info --json

# Sube archivos fake al bucket s3

# Ejemplos:
# Nombre del bucket: bucket-csv-images-alvaro8317dev-dev
# Ubicación del archivo: data/fake_data_20251221_184835_1.csv

aws s3 cp ../data/fake_data_20251221_223605_2.csv s3://bucket-csv-images-alvaro8317dev-dev --profile local

# Lista archivos de un bucket

aws s3 ls bucket-csv-images-alvaro8317dev-dev --profile local

# Revisar logs de una lambda

sls logs --function hello