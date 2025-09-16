import os
import subprocess
# No se utiliza un comando directo de Boto3 o gcloud porque requiere configuración de credenciales
# En su lugar utilizamos el comando de la CLI del proveedor.

def upload_to_cloud(file_path, bucket_name):
    # AWS S3
    command = f"aws s3 cp {file_path} s3://{bucket_name}/"
    subprocess.run(command, shell=True, check=True)
    print(f"Archivo subido a S3: {file_path}")

# Ejemplo de uso
backup_file = "proyectos_2025-09-10_15-42-46.tar.gz"
cloud_bucket = "mi-bucket-de-backups-unico"

# Esta función llama a la CLI de AWS
upload_to_cloud(backup_file, cloud_bucket)
