import os
import subprocess
import sys

# Obtener el puerto dinámico que Railway asigna automáticamente
port = os.getenv("PORT", "8080")

print(f"🚀 Starting Reflex backend on port {port}")

# Configuración básica para evitar escritura innecesaria
os.environ["PYTHONUNBUFFERED"] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

# Comando para ejecutar Reflex solo con backend
cmd = [
    "reflex",
    "run",
    "--env", "prod",
    "--backend-host", "0.0.0.0",
    "--backend-port", port,
    "--loglevel", "warning"   # Menos logs = menos memoria
]

subprocess.run(cmd, check=True)
