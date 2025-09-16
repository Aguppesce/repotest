#!/usr/bin/env python3
"""
Script para contar conexiones por IP desde access.log
"""
import requests
import re
from collections import defaultdict
import sys

def main():
    url = "http://13.220.176.197/access.log"
    try:
        print("Descargando el archivo access.log")
        response = requests.get(url)
        response.raise_for_status()  # Verifica si hubo error HTTP

        # Expresión regular para detectar una IP en una línea de texto
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        ip_counter = defaultdict(int)
        ip_total = 0

        print("Procesando conexiones por IP...")
        print("=" * 40)
        print(f"{'IP':<15} | {'Conexiones':>10}")
        print("=" * 40)

        # Contar IPs línea por línea
        for line in response.text.split('\n'):
            ips = re.findall(ip_pattern, line)
            for ip in ips:  # Contar las IPs de cada línea de texto                
                ip_counter[ip] += 1
                ip_total += 1

        # Ordenar y mostrar resultados
        for ip, count in sorted(ip_counter.items(), key=lambda x: x[1], reverse=True):
            print(f"{ip:<15} | {count:>10}")
        
        print("=" * 40)
        print(f"{'TOTAL':<15} | {ip_total:>10}")
        print("=" * 40)
        print("Procesamiento completado.")

    except requests.RequestException as e:
        print(f"Error al descargar el archivo: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()