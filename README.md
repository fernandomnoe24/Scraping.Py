# 📄 Script de Descarga de PDFs

Este script en Python descarga automáticamente archivos PDF desde una lista de enlaces y los organiza en carpetas según la estructura de la URL.

⚙️ Cómo funciona

Lectura de enlaces desde links.txt (uno por línea).

User-Agent personalizado en todas las peticiones para simular un navegador real.

Carpetas dinámicas creadas según segmentos de la URL (pdf_descargados/carpeta1/carpeta2/archivo.pdf).

Si la URL no tiene la profundidad suficiente → se guarda en otros/sin_nombre/.

Descarga de PDFs con requests, controlando errores (404, 500, timeout).

Pausas aleatorias (8–15 s) entre descargas para no saturar el servidor.

🚀 Uso

Crear links.txt con los enlaces de los PDFs.

Ejecutar:

python *App-3.py*


Los archivos se guardarán en pdf_descargados/.
