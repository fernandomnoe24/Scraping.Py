import requests
import time
import os
import sys
import random

# Archivo con los enlaces
archivo_links = "links.txt"

# Carpeta base
carpeta_base = "pdf_descargados"
os.makedirs(carpeta_base, exist_ok=True)

# Headers con User-Agent personalizado
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Leer links
with open(archivo_links, "r") as f:
    links = [line.strip() for line in f if line.strip()]

print(f"Se encontraron {len(links)} enlaces para descargar.\n")

for i, url in enumerate(links, start=1):
    try:
        print(f"[{i}/{len(links)}] Descargando: {url}")

        # Dividir la URL en partes
        partes = url.split("/")

        # Extraer carpetas dinámicas
        if len(partes) >= 9:
            carpeta1 = partes[6]
            carpeta2 = partes[7]
        else:
            carpeta1 = "otros"
            carpeta2 = "sin_nombre"

        # Crear ruta final
        ruta_carpeta = os.path.join(carpeta_base, carpeta1, carpeta2)
        os.makedirs(ruta_carpeta, exist_ok=True)

        # Nombre del archivo
        nombre_archivo = partes[-1]
        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)

        # Descargar PDF con User-Agent
        respuesta = requests.get(url, headers=headers, timeout=30)
        respuesta.raise_for_status()

        # Guardar archivo
        with open(ruta_archivo, "wb") as pdf:
            pdf.write(respuesta.content)

        print(f"✅ Guardado en: {ruta_archivo}")

    except Exception as e:
        print(f"❌ Error al descargar {url}: {e}")

    # Espera aleatoria entre 8 y 12 segundos
    if i < len(links):
        tiempo_espera = random.randint(8, 15)
        print(f"Esperando {tiempo_espera} segundos para la próxima descarga:")
        for t in range(tiempo_espera, 0, -1):
            sys.stdout.write(f"\r⏳ {t} segundos restantes...")
            sys.stdout.flush()
            time.sleep(1)
        print("\n")

print("✔ Descargas finalizadas.")
