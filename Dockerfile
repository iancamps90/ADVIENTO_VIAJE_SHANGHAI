# ✅ Dockerfile funcional para Reflex en Railway
FROM python:3.11-slim

# Instalar bash y dependencias básicas
RUN apt-get update && apt-get install -y \
    bash \
    curl \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Variables necesarias
ENV PYTHONPATH=/app
ENV REFLEX_ENV=prod
ENV ALLOWED_HOSTS=*

# Exponer puerto (opcional, Railway lo inyecta)
EXPOSE 8000

# 🧠 Ejecutamos Reflex con el puerto expandido dinámicamente
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["reflex run --env prod --backend-port ${PORT:-8000} --frontend-port ${PORT:-8000}"]

