FROM python:3.11-slim

# Instalar dependencias mínimas del sistema (incluido unzip)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

WORKDIR /app

# Copiar e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de archivos del proyecto
COPY adeviento_web/ ./adeviento_web/
COPY assets/ ./assets/
COPY public/ ./public/
COPY rxconfig.py .
COPY start.py .

# Variables de entorno
ENV PYTHONPATH=/app
ENV REFLEX_ENV=prod
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Render inyecta $PORT dinámicamente
EXPOSE 10000

# Ejecutar el script de inicio
CMD ["python", "start.py"]
