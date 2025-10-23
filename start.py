import os
import subprocess

# Obtener el puerto (Render asigna automáticamente PORT)
port = os.getenv("PORT", "8000")

print(f"🚀 Starting Reflex on port: {port}")

# Configuración optimizada
os.environ["PYTHONUNBUFFERED"] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

# Comando actualizado (sin --no-frontend)
cmd = [
    "reflex", "run",
    "--env", "prod",
    "--backend-host", "0.0.0.0",
    "--backend-port", port,
    "--loglevel", "warning"
]

# Ejecutar Reflex
subprocess.run(cmd, check=True)
