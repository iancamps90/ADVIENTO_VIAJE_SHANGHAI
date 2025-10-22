FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade reflex

# Copy the application
COPY . .

# Build the frontend (static export handled by Reflex; no manual copy needed)
RUN python -m reflex export --frontend-only

# List contents to see where the export went
RUN ls -la web/ || echo "web directory not found"
RUN find . -name "*.html" -type f | head -10 || echo "No HTML files found"

# Expose port
EXPOSE 8000

# Start a simple static server for the exported app
CMD ["sh", "-c", "cd web && python -m http.server ${PORT:-8000}"]
