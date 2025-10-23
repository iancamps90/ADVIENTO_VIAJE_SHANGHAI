FROM python:3.11-slim

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY adeviento_web/ ./adeviento_web/
COPY assets/ ./assets/
COPY rxconfig.py .
COPY start.py .

# Variables de entorno
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV REFLEX_ENV=prod

# Railway usará este puerto
EXPOSE 8080

# Comando de arranque
CMD ["python", "start.py"]