import os
import subprocess

port = os.getenv("PORT", "10000")  # Render usa 10000 por defecto

subprocess.run([
    "reflex",
    "run",
    "--env", "prod",
    "--frontend-port", port,
    "--backend-port", port,
    "--frontend-host", "0.0.0.0",
    "--backend-host", "0.0.0.0"
])
