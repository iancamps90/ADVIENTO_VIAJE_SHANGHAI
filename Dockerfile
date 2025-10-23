FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl unzip \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar proyecto
COPY adeviento_web/ ./adeviento_web/
COPY assets/ ./assets/
COPY rxconfig.py .
COPY start.py .

# Variables de entorno
ENV PYTHONPATH=/app
ENV REFLEX_ENV=prod
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PORT=10000

EXPOSE 10000

# Render solo necesita el backend escuchando
CMD ["reflex", "run", "--env", "prod", "--backend-host", "0.0.0.0", "--backend-port", "10000", "--backend-only"]

