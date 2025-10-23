FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl unzip \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

WORKDIR /app

# Copiar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar archivos del proyecto
COPY adeviento_web/ ./adeviento_web/
COPY assets/ ./assets/
COPY rxconfig.py .
COPY start.py .

# Variables de entorno
ENV PYTHONPATH=/app
ENV REFLEX_ENV=prod
ENV PORT=10000
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Exponer puerto del backend Reflex
EXPOSE 10000

# Healthcheck para que Render detecte el puerto
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:10000/ || exit 1

# Comando principal
CMD ["python", "start.py"]
