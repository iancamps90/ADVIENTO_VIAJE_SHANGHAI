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

# Debug: see what was created
RUN echo "=== Current directory structure ==="
RUN ls -la
RUN echo "=== Looking for HTML files ==="
RUN find . -name "*.html" -type f | head -10 || echo "No HTML files found"
RUN echo "=== Looking for any web directory ==="
RUN find . -name "web" -type d || echo "No web directory found"

# Expose port
EXPOSE 8000

# Serve the exported static site. Prefer .web/_static, fallback to web/_static or public
CMD ["sh", "-c", "DIR=.web/_static; [ -d $DIR ] || DIR=web/_static; [ -d $DIR ] || DIR=public; cd $DIR && python -m http.server ${PORT:-8000}"]
