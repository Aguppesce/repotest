#!/usr/bin/env python3
import shutil
import os
from datetime import datetime # Módulo para manejar fechas y horas

# Establecemos un límite para que active una alerta
LIMIT_USAGE=90

# Obtenemos el uso del disco en la partición raíz (/)
# shutil.disk_usage() devuelve una tupla con (total, used, free)
total, used, free = shutil.disk_usage("/")

# Calculamos el porcentaje de uso. Con round redondeamos el resultado a un número entero
percent_used = round((used / total) * 100)

# Definimos la ruta del archivo del log
log_file_path = "/home/ubuntu/Documents/disk_check.log"

# Creamos el mensaje de log
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Comparamos el porcentaje de uso con el límite establecido
if percent_used > LIMIT_USAGE:    
    message = f"[{timestamp}] ALERTA: El uso del disco ha superado el {LIMIT_USAGE}% -> Uso actual: {percent_used}%. Por favor, libera espacio en el disco"    
else:
    # Si no, imprimimos el uso actual
    message = f"[{timestamp}] Uso del disco: {percent_used}% - Todo en orden."

# Escribimos el mensjae en el archivo de log
try:
    with open(log_file_path, "a") as f: # Abrimos el archivo en modo "append" para no sobrescribir
        f.write(message + "\n")
        # Para hacer una depuración, también podemos imprimir en la consola
        # print(message)
except Exception as e:
    # Manejamos errores de escritura en el log
    print(f"[{timestamp}] ERROR: No se pudo escribir en el archivo de log: {e}")


# Abrir crontab con: crontab -e

# Añadir la siguiente línea al final del archivo:
# * * * * * /home/ubuntu/Downloads/GIT/repotest/scripts/Ejercicios/Disk_check.py

# Configurar crontab para que envie un email en caso de error
# MAILTO="tu_email@ejemplo.com"
# * * * * * /home/ubuntu/Downloads/GIT/repotest/scripts/Ejercicios/Disk_check.py