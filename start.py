import os
import subprocess
import sys

# Render inyecta el puerto automáticamente
port = os.getenv("PORT")

print(f"Starting Reflex on port: {port} (optimized memory mode)")

# Configuración optimizada para memoria
os.environ["PYTHONUNBUFFERED"] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

# Ejecutar Reflex con optimizaciones de memoria
subprocess.run([
    sys.executable, "-m", "reflex",
    "run",
    "--env", "prod",
    "--backend-host", "0.0.0.0",
    "--backend-port", port,
    "--frontend-port", port,
    "--no-frontend",
    "--loglevel", "warning"  # Reducir logs para ahorrar memoria
])
