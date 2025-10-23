FROM python:3.11-slim

RUN apt-get update && apt-get install -y unzip curl wget && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV PYTHONPATH=/app
ENV REFLEX_ENV=prod

EXPOSE 10000

# Usa solo backend: Reflex no recompila frontend cada vez
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["reflex run --env prod --backend-host 0.0.0.0 --backend-port ${PORT:-10000} --frontend-port ${PORT:-10000} --no-frontend"]