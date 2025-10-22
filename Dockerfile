# Use Python 3.11 slim image
FROM python:3.11-slim

# Instalar bash y dependencias del sistema
RUN apt-get update && apt-get install -y \
    bash \
    unzip \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copiar requirements y instalarlos primero (mejor caché)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables
ENV PYTHONPATH=/app
ENV REFLEX_ENV=prod
ENV ALLOWED_HOSTS=*

# Expose port
EXPOSE 8000

# Start the application
CMD ["bash", "-c", "reflex run --env prod --frontend-port ${PORT:-8000} --backend-port ${PORT:-8000}"]

