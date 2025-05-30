import boto3
import os
import logging

# Configuración
bucket = "urban-mobility"
local_path = "data/processed/usuarios_ecobici_limpio.csv"
remote_path = "usuarios/usuarios_ecobici_limpio.csv"

# Cliente S3 para MinIO
s3 = boto3.client(
    "s3",
    endpoint_url="http://minio:9000",
    aws_access_key_id="admin",
    aws_secret_access_key="admin123"
)

# Crear bucket si no existe
existing_buckets = [b['Name'] for b in s3.list_buckets()['Buckets']]
if bucket not in existing_buckets:
    s3.create_bucket(Bucket=bucket)
    logging.info(f"Bucket '{bucket}' creado.")
else:
    logging.info(f"Bucket '{bucket}' ya existe.")

# Subir archivos
if os.path.isdir(local_path):
    # Modo carpeta (como output de Spark CSV)
    for root, dirs, files in os.walk(local_path):
        for file in files:
            full_path = os.path.join(root, file)
            key_path = os.path.join(remote_path, file).replace("\\", "/")
            s3.upload_file(full_path, bucket, key_path)
            logging.info(f"Subido: {full_path} → s3://{bucket}/{key_path}")
elif os.path.isfile(local_path):
    # Modo archivo único
    s3.upload_file(local_path, bucket, remote_path)
    logging.info(f"Subido: {local_path} → s3://{bucket}/{remote_path}")
else:
    logging.error(f"Ruta local no encontrada: {local_path}")

