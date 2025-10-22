FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js 20 (Recomendado por Reflex >=0.6)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade reflex

# Copy the application
COPY . .

# Build the frontend (static export)
RUN python -m reflex export --frontend-only

# Collect exported site into a stable path
RUN mkdir -p /srv/site \
    && if [ -d .web/_static ]; then cp -r .web/_static/* /srv/site/; \
    elif [ -d web/_static ]; then cp -r web/_static/* /srv/site/; \
    elif [ -d public ]; then cp -r public/* /srv/site/; \
    fi \
    && ls -la /srv/site || true

# Expose port
EXPOSE 8000

# Serve the exported static site
CMD ["sh", "-c", "cd /srv/site && python -m http.server ${PORT:-8000}"]
