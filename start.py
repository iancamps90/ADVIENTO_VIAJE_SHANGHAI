import os
import subprocess

# Render inyecta el puerto dinámicamente
port = os.getenv("PORT", "10000")  # Puerto por defecto si no se especifica

print(f"Starting Reflex on port: {port} (no-frontend mode)")

subprocess.run([
    "reflex",
    "run",
    "--env", "prod",
    "--backend-host", "0.0.0.0",
    "--backend-port", port,
    "--frontend-port", port,
    "--no-frontend"
])
