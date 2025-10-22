FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    python3-pip bash curl wget unzip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV PYTHONPATH=/app
ENV REFLEX_ENV=prod
ENV ALLOWED_HOSTS=*
EXPOSE 10000

CMD ["python", "start.py"]