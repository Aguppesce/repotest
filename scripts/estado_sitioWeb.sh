#!/usr/bin/env bash
URL="http://google.com"
HTTP_CODE=$(curl -o /dev/null -s -w "%{http_code}\n" "$URL")

while true
do
# Cada 60 segundos verifico si el sitio web responde
HTTP_CODE=$(curl -o /dev/null -s -w "%{http_code}\n" "$URL")
if [ "$HTTP_CODE" -eq 200 ]; then
    echo "El sitio web $URL está en línea. Código de estado HTTP: $HTTP_CODE"
else
    echo "El sitio web $URL no responde. Código de estado HTTP: $HTTP_CODE"
fi
sleep 60
done