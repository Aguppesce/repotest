#!/bin/bash

#Contador de IPs desde access.log

URL="http://13.220.176.197/access.log"
TEMP_FILE="/tmp/access.log"

echo "Descargando access.log"
wget -q "$URL" -O "$TEMP_FILE"

if [ $? -ne 0 ]; then
	echo "Error: no se pudo descargar el archivo desde $URL"
	exit 1
fi

echo "Procesando conexiones por IP... "
echo "================================"
echo "IP		| Conexiones	"
grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' "$TEMP_FILE" | \
sort | \
uniq -c | \
sort -nr | \
while read count ip; do
    printf "%-15s | %d\n" "$ip" "$count"
done

rm -f "$TEMP_FILE"
echo "======================================"
echo "Procesamiento completado."
