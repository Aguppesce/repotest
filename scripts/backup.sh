#!/bin/bash
# Backup simple de archivos para ejecutar con "cron"

# Defino el directorio a respaldar
SOURCE_DIR="/home/ubuntu/Downloads/GIT" 
# Defino el directorio de destino
BACKUP_DIR="/home/ubuntu/Backups"
# Fecha en la que se crea el backup (Formato ISO 8601)
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
# Nombre del archivo de backup
BACKUP_FILE="backup-git_${TIMESTAMP}.tar.gz"
# Navegamos al directorio destino
cd $BACKUP_DIR
# Creamos el backup comprimido
tar -czvf $BACKUP_FILE $SOURCE_DIR
# Imprimimos un mensaje de confirmación
echo "Backup creado: $BACKUP_DIR/$BACKUP_FILE"
# Listamos los archivos en el directorio de backup
ls -lh $BACKUP_DIR
# Fin del script
