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

# Build the frontend
RUN python -m reflex export --frontend-only

# Copy static files to the correct location
RUN cp -r web/_static/* /app/

# Expose port
EXPOSE 8000

# Start the application
CMD ["python", "-m", "reflex", "run", "--env", "prod", "--port", "8000", "--host", "0.0.0.0"]
