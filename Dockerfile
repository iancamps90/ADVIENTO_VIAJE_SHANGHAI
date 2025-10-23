FROM python:3.11-slim

# Instalar solo dependencias mínimas necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

WORKDIR /app

# Copiar solo archivos necesarios para reducir tamaño de imagen
COPY requirements.txt .
RUN pip install --no-cache-dir --no-deps -r requirements.txt

# Copiar solo archivos esenciales
COPY adeviento_web/ ./adeviento_web/
COPY rxconfig.py .
COPY start.py .

# Variables de entorno para optimizar memoria
ENV PYTHONPATH=/app
ENV REFLEX_ENV=prod
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# No exponer puerto específico - Render lo maneja
EXPOSE 8000

# Usar start.py que ya tiene la configuración optimizada
CMD ["python", "start.py"]