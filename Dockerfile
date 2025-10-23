FROM python:3.11-slim

# Imagen base ligera
FROM python:3.11-slim

# Instalar dependencias del sistema necesarias para Reflex
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl unzip \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY adeviento_web/ ./adeviento_web/
COPY assets/ ./assets/
COPY rxconfig.py .
COPY start.py .

# Variables de entorno globales
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV REFLEX_ENV=prod

# Railway usa el puerto 8080 por defecto
EXPOSE 8080

# Ejecutar Reflex
CMD ["python", "start.py"]
