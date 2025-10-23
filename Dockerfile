FROM python:3.11-slim

# Instalar dependencias básicas del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

WORKDIR /app

# Copiar e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de archivos del proyecto
COPY adeviento_web/ ./adeviento_web/
COPY rxconfig.py .
COPY start.py .

# Variables de entorno
ENV PYTHONPATH=/app
ENV REFLEX_ENV=prod
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Render inyecta $PORT dinámicamente
EXPOSE 10000

# Lanzar Reflex escuchando en 0.0.0.0 y el puerto de Render
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["reflex run --env prod --backend-host 0.0.0.0 --backend-port ${PORT:-10000} --frontend-port ${PORT:-10000} --no-frontend"]
