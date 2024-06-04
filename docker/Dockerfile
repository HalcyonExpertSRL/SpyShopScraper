# Utilizar una imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos requirements.txt y scraper.py al contenedor
COPY requirements.txt requirements.txt
COPY scraper.py scraper.py

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Definir el comando por defecto para ejecutar el script
CMD ["python", "scraper.py"]
