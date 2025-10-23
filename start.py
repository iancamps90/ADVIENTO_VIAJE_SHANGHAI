import os
import subprocess

# Render inyecta el puerto dinámicamente
port = os.getenv("PORT", "8000")  # Puerto por defecto si no se especifica

print(f"Starting Reflex on port: {port}")

subprocess.run([
    "reflex",
    "run",
    "--env", "prod",
    "--frontend-port", port,
    "--backend-port", port,
    "--backend-host", "0.0.0.0"
])
