#!/bin/bash

# Establecemos un límite para que active una alerta
LIMIT_USAGE=50

# df -h: Muestra el uso del disco en formato legible
# grep "/$" busca la línea que termina con "/"
# awk '{print $5}' extrae el porcentaje de uso del disco
# sed 's/%//' elimina el símbolo de porcentaje para poder comparar
USAGE=$(df -h | grep "/$" | awk '{print $5}' | sed 's/%//')

# Obtenemos la fecha y hora actual en un formato estándar
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Definimos el arhcivo de log.
LOG_FILE="/home/ubuntu/Documents/disk_usage.log"

# Comparamos el uso actual con el límite establecido
if [ "$USAGE" -gt "$LIMIT_USAGE" ]; then # -gt significa "greater than" (mayor que)
    MESSAGE="[${TIMESTAMP}] ALERTA: Uso del disco Ha superado el ${LIMIT_USAGE}% - Uso actual: ${USAGE}%. Desde Disk_check.sh"
else
    MESSAGE="[${TIMESTAMP}] Uso del disco: ${USAGE}% - Todo en orden. Desde Disk_check.sh"
fi

# Escribimos el mensaje en el archivo de log añadiendo una nueva línea
echo "$MESSAGE" >> "$LOG_FILE"

# Abrir crontab con: crontab -e
# Añadir la siguiente línea al final del archivo, para ejecutarla cada 5 minutos:
# * * * * * /bin/bash /home/ubuntu/Documents/Ejercicios/Disk_check.sh