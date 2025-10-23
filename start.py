import os
import subprocess
import sys

port = os.getenv("PORT", "10000")

print(f"🚀 Starting Reflex on port: {port}")

os.environ["PYTHONUNBUFFERED"] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

# Ejecutar Reflex sin levantar frontend dev
subprocess.run([
    "reflex", "run",
    "--env", "prod",
    "--backend-host", "0.0.0.0",
    "--backend-port", port,
    "--loglevel", "info"
])